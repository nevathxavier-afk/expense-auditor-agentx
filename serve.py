"""High-Performance Cyber-FinTech Backend Server & REST API.
Serves the interactive frontend and real-time JSON API endpoints over the 250,000 transaction dataset.
"""
import copy
import http.server
import json
import os
import sqlite3
import sys
import urllib.parse

# Ensure workspace root is in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config
from agent.auditor import ExpenseAuditor, THEMES, assign_theme
from agent.budget import BudgetRebalancer
from agent.similarity import generate_tx_hash, generate_vpa
from blockchain.ledger import BlockchainLedger
from blockchain.tamper_test import TamperTestingEnvironment

PORT = 8000
DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dashboard")
DB_PATH = os.path.join(config.DATA_DIR, "transactions.db")

# Global singleton tamper tester
tamper_env = TamperTestingEnvironment()


class FinTechAPIHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        if parsed.path == "/api/stats":
            self._send_json(self._get_stats())
        elif parsed.path == "/api/transactions":
            self._send_json(self._get_transactions(params))
        elif parsed.path == "/api/anomalies":
            self._send_json(self._get_anomalies())
        elif parsed.path == "/api/blockchain":
            self._send_json(self._get_blockchain())
        elif parsed.path == "/api/rebalance":
            income = float(params.get("income", [65000])[0])
            self._send_json(self._get_rebalance(income))
        else:
            super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length)) if length > 0 else {}

        if parsed.path == "/api/tamper/avalanche":
            orig = str(body.get("original", "TXN001:amount=14850.00:user=user_del_25@axis"))
            mut = str(body.get("mutated", "TXN001:amount=14850.01:user=user_del_25@axis"))
            from blockchain.tamper_test import compute_avalanche_effect
            res = compute_avalanche_effect(orig, mut)
            self._send_json(res)
        elif parsed.path == "/api/tamper/simulate":
            block_idx = int(body.get("block_index", 1))
            field = str(body.get("field", "amount"))
            forged_val = body.get("value", 86800.0)
            res = tamper_env.inject_tamper(block_idx, field, forged_val)
            self._send_json(res)
        elif parsed.path == "/api/tamper/verify":
            res = tamper_env.verify_with_consensus_telemetry()
            self._send_json(res)
        elif parsed.path == "/api/tamper/heal":
            res = tamper_env.reset_and_heal()
            self._send_json(res)
        else:
            self.send_error(404, "Endpoint not found")

    def _send_json(self, data, status=200):
        payload = json.dumps(data, default=str).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(payload)

    def _get_stats(self):
        if not os.path.exists(DB_PATH):
            return {"error": "Database not indexed yet"}
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        total = cur.execute("SELECT count(*), sum(amount), avg(amount) FROM transactions").fetchone()
        cats = cur.execute("SELECT merchant_category, count(*), sum(amount) FROM transactions GROUP BY merchant_category ORDER BY sum(amount) DESC").fetchall()
        types = cur.execute("SELECT transaction_type, count(*), sum(amount) FROM transactions GROUP BY transaction_type").fetchall()
        banks = cur.execute("SELECT sender_bank, count(*) FROM transactions GROUP BY sender_bank ORDER BY count(*) DESC LIMIT 6").fetchall()
        states = cur.execute("SELECT sender_state, count(*), sum(amount) FROM transactions GROUP BY sender_state ORDER BY count(*) DESC LIMIT 6").fetchall()
        fraud = cur.execute("SELECT count(*) FROM transactions WHERE fraud_flag = 1").fetchone()[0]
        conn.close()

        # Multi-level Themes Aggregation
        theme_map = {}
        for c, count, amt in cats:
            th = assign_theme(c)
            theme_map[th] = theme_map.get(th, 0.0) + amt

        return {
            "total_transactions": total[0],
            "total_spend_inr": round(total[1], 2),
            "average_spend_inr": round(total[2], 2),
            "confirmed_fraud_count": fraud,
            "themes_breakdown": {k: round(v, 2) for k, v in theme_map.items()},
            "categories_breakdown": [{"category": c, "count": cnt, "amount_inr": round(amt, 2)} for c, cnt, amt in cats],
            "types_breakdown": [{"type": t, "count": cnt, "amount_inr": round(amt, 2)} for t, cnt, amt in types],
            "top_banks": [{"bank": b, "count": cnt} for b, cnt in banks],
            "top_states": [{"state": s, "count": cnt, "amount_inr": round(amt, 2)} for s, cnt, amt in states]
        }

    def _get_transactions(self, params):
        if not os.path.exists(DB_PATH):
            return {"transactions": []}
        page = max(1, int(params.get("page", [1])[0]))
        limit = min(100, max(5, int(params.get("limit", [20])[0])))
        offset = (page - 1) * limit
        cat_filter = params.get("category", [""])[0]

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        if cat_filter:
            cur.execute("SELECT transaction_id, timestamp, merchant_category, transaction_type, amount, sender_bank, receiver_bank, sender_state, fraud_flag FROM transactions WHERE merchant_category = ? ORDER BY timestamp DESC LIMIT ? OFFSET ?", (cat_filter, limit, offset))
        else:
            cur.execute("SELECT transaction_id, timestamp, merchant_category, transaction_type, amount, sender_bank, receiver_bank, sender_state, fraud_flag FROM transactions ORDER BY timestamp DESC LIMIT ? OFFSET ?", (limit, offset))
        rows = cur.fetchall()
        conn.close()

        items = []
        for r in rows:
            txn_id, ts, cat, t_type, amt, s_bank, r_bank, state, fraud = r
            tx_hash = generate_tx_hash(txn_id, ts, s_bank, r_bank, amt)
            sender_vpa = generate_vpa("user", state[:3], s_bank)
            receiver_vpa = generate_vpa("merchant", cat, r_bank)
            items.append({
                "transaction_id": txn_id,
                "tx_hash": tx_hash,
                "sender_vpa": sender_vpa,
                "receiver_vpa": receiver_vpa,
                "timestamp": ts,
                "category": cat,
                "theme": assign_theme(cat),
                "type": t_type,
                "amount": amt,
                "fraud_flag": fraud
            })
        return {"page": page, "limit": limit, "transactions": items}

    def _get_anomalies(self):
        cache_file = os.path.join(config.DATA_DIR, ".last_audit.json")
        if os.path.exists(cache_file):
            try:
                with open(cache_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {"anomalies": []}

    def _get_blockchain(self):
        ledger = BlockchainLedger()
        return {
            "chain_length": len(ledger.chain),
            "difficulty": ledger.difficulty,
            "status": "CHAIN_SYNCHRONIZED",
            "blocks": [b.to_dict() for b in ledger.chain]
        }

    def _get_rebalance(self, income):
        rebalancer = BudgetRebalancer(self._get_anomalies())
        return rebalancer.generate_plan(income)


def start_server():
    print(f"\n=======================================================")
    print(f"🚀 Expense Auditor & Anomaly Hunter Studio")
    print(f"🌐 Dashboard & REST API live at: http://localhost:{PORT}")
    print(f"📡 API Endpoints:")
    print(f"   • GET  /api/stats")
    print(f"   • GET  /api/transactions")
    print(f"   • GET  /api/anomalies")
    print(f"   • GET  /api/blockchain")
    print(f"   • POST /api/tamper/simulate")
    print(f"   • POST /api/tamper/verify")
    print(f"   • POST /api/tamper/heal")
    print(f"=======================================================\n")
    with http.server.ThreadingHTTPServer(("", PORT), FinTechAPIHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")


if __name__ == "__main__":
    start_server()
