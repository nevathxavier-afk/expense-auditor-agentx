"""AuditTransactions tool for detecting financial anomalies, duplicates, and subscription creep."""
import csv
import json
import os

import config
from agent.auditor import ExpenseAuditor
from tools import Tool


def _path(filename):
    path = os.path.join(config.DATA_DIR, os.path.basename(filename))
    if not os.path.exists(path):
        raise FileNotFoundError(f"{filename} not found in {config.DATA_DIR}.")
    return path


class AuditTransactions(Tool):
    name = "audit_transactions"
    description = (
        "Audit a UPI/bank statement CSV: auto-categorizes expenses, hunts duplicate charges, "
        "detects subscription creep, and flags spend surges with cognitive reasoning."
    )
    args_doc = '{"filename": "sample_transactions.csv", "max_rows": 1000}'

    def execute(self, filename="sample_transactions.csv", max_rows=1000):
        filepath = _path(filename)
        rows = []
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            reader = csv.DictReader(f)
            for i, r in enumerate(reader):
                if i >= int(max_rows):
                    break
                rows.append(r)

        if not rows:
            return "ERROR: No transaction rows found in file."

        auditor = ExpenseAuditor(rows)
        results = auditor.run_full_audit()

        # Cache last audit for downstream blockchain mining / budget rebalancing
        cache_file = os.path.join(config.DATA_DIR, ".last_audit.json")
        try:
            with open(cache_file, "w", encoding="utf-8") as f:
                json.dump(results, f, default=str)
        except Exception:
            pass

        return json.dumps({
            "transactions_analyzed": results["transactions_analyzed"],
            "total_spend_inr": results["total_spend_inr"],
            "portfolio_risk_index": results["portfolio_risk_index"],
            "overall_risk_grade": results["overall_risk_grade"],
            "duplicates_count": results["duplicates_count"],
            "subscription_creep_count": results["subscription_creep_count"],
            "spend_surges_count": results["spend_surges_count"],
            "top_anomalies_sample": results["anomalies"][:5]
        }, indent=2, default=str)
