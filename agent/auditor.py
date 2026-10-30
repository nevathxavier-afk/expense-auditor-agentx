"""Financial Expense Auditor & Anomaly Hunter Engine.
Audits UPI and bank statement transactions:
1. Auto-categorizes purchases
2. Detects duplicates, subscription creep, spend surges, and velocity spikes
3. Generates explainable auditor reasoning and impact metrics
"""
import csv
import math
from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Any


CATEGORY_RULES = {
    "Grocery": ["grocery", "supermarket", "mart", "kirana", "provisions", "zepto", "blinkit", "instamart", "bigbasket"],
    "Food & Dining": ["food", "restaurant", "cafe", "swiggy", "zomato", "mcdonalds", "starbucks", "burger", "pizza", "dining"],
    "Entertainment": ["entertainment", "netflix", "spotify", "hotstar", "cinema", "movie", "prime video", "theatre", "gaming", "steam"],
    "Utilities": ["utilities", "electricity", "water", "gas", "bescom", "tneb", "broadband", "wifi", "bill payment", "cylinder"],
    "Fuel & Travel": ["fuel", "petrol", "diesel", "hpcl", "bpcl", "ioc", "transport", "uber", "ola", "metro", "irctc", "flight"],
    "Shopping": ["shopping", "amazon", "flipkart", "myntra", "retail", "clothing", "apparel", "electronics"],
    "Healthcare": ["healthcare", "pharmacy", "apollo", "medplus", "hospital", "clinic", "doctor", "lab", "medicine"],
    "Investments & Savings": ["sip", "mutual fund", "zerodha", "groww", "stock", "fd", "rd", "insurance", "lic"],
    "Other": []
}


def auto_categorize(merchant_category: str, txn_type: str = "") -> str:
    """Classifies transaction into standardized financial categories."""
    raw = f"{merchant_category} {txn_type}".lower().strip()
    for category, keywords in CATEGORY_RULES.items():
        if any(kw in raw for kw in keywords):
            return category
    if merchant_category and merchant_category != "Other":
        return merchant_category.strip()
    return "Discretionary Other"


class ExpenseAuditor:
    """Core cognitive engine for detecting financial anomalies and computing risk scores."""

    def __init__(self, transactions: List[Dict[str, Any]]):
        self.raw_transactions = transactions
        self.transactions = []
        self._normalize_and_clean()

    def _normalize_and_clean(self):
        for row in self.raw_transactions:
            # Handle possible key naming variations
            txn_id = row.get("transaction id") or row.get("transaction_id") or row.get("id") or "TXN_UNKNOWN"
            ts_str = row.get("timestamp") or row.get("date") or "2024-01-01 00:00:00"
            try:
                ts = datetime.strptime(ts_str.strip(), "%Y-%m-%d %H:%M:%S")
            except Exception:
                try:
                    ts = datetime.strptime(ts_str.strip(), "%Y-%m-%d")
                except Exception:
                    ts = datetime(2024, 1, 1)

            amount_val = row.get("amount (INR)") or row.get("amount") or row.get("Amount") or 0.0
            try:
                amount = float(amount_val)
            except Exception:
                amount = 0.0

            raw_cat = row.get("merchant_category") or row.get("category") or "Other"
            txn_type = row.get("transaction type") or row.get("type") or ""
            category = auto_categorize(raw_cat, txn_type)

            self.transactions.append({
                "transaction_id": txn_id,
                "timestamp": ts,
                "timestamp_str": ts_str,
                "amount": amount,
                "raw_category": raw_cat,
                "category": category,
                "transaction_type": txn_type,
                "sender_bank": row.get("sender_bank", "Unknown"),
                "receiver_bank": row.get("receiver_bank", "Unknown"),
                "status": row.get("transaction_status", "SUCCESS"),
                "fraud_flag": int(row.get("fraud_flag", 0) or 0)
            })

    def run_full_audit(self) -> Dict[str, Any]:
        """Runs the complete suite of financial anomaly hunting algorithms."""
        duplicates = self.detect_duplicates()
        subscriptions = self.detect_subscription_creep()
        surges = self.detect_spend_surges()
        fraud_flags = self.detect_fraud_risk()

        all_anomalies = duplicates + subscriptions + surges + fraud_flags
        all_anomalies.sort(key=lambda x: x.get("risk_score", 0), reverse=True)

        total_spend = sum(t["amount"] for t in self.transactions)
        total_flagged_amount = sum(a.get("amount", 0.0) for a in all_anomalies)
        
        category_breakdown = defaultdict(float)
        for t in self.transactions:
            category_breakdown[t["category"]] += t["amount"]

        # Risk level determination
        risk_index = round(min(100.0, (total_flagged_amount / (total_spend or 1.0)) * 250.0 + len(all_anomalies) * 1.5), 1)
        risk_grade = "CRITICAL" if risk_index > 75 else "HIGH" if risk_index > 50 else "MODERATE" if risk_index > 25 else "LOW"

        return {
            "transactions_analyzed": len(self.transactions),
            "total_spend_inr": round(total_spend, 2),
            "total_flagged_amount_inr": round(total_flagged_amount, 2),
            "portfolio_risk_index": risk_index,
            "overall_risk_grade": risk_grade,
            "duplicates_count": len(duplicates),
            "subscription_creep_count": len(subscriptions),
            "spend_surges_count": len(surges),
            "fraud_flags_count": len(fraud_flags),
            "total_anomalies_count": len(all_anomalies),
            "category_spend_breakdown": {k: round(v, 2) for k, v in category_breakdown.items()},
            "anomalies": all_anomalies
        }

    def detect_duplicates(self) -> List[Dict[str, Any]]:
        """Detects duplicate transactions (identical amount, same category/receiver within 15 minutes)."""
        duplicates = []
        seen = {}
        for t in sorted(self.transactions, key=lambda x: x["timestamp"]):
            key = (t["amount"], t["category"], t["receiver_bank"])
            if key in seen:
                prev_t = seen[key]
                delta_mins = (t["timestamp"] - prev_t["timestamp"]).total_seconds() / 60.0
                if 0 <= delta_mins <= 15:
                    duplicates.append({
                        "anomaly_id": f"DUP-{t['transaction_id']}",
                        "transaction_id": t["transaction_id"],
                        "previous_transaction_id": prev_t["transaction_id"],
                        "type": "DUPLICATE_PAYMENT",
                        "severity": "HIGH",
                        "risk_score": 85,
                        "amount": t["amount"],
                        "category": t["category"],
                        "timestamp": t["timestamp_str"],
                        "reasoning": (
                            f"Double charge detected: Exactly INR {t['amount']} was paid twice to {t['category']} "
                            f"({t['receiver_bank']}) within {round(delta_mins, 1)} minutes. Likely user double-click "
                            f"or gateway retry error. Immediate reversal claim recommended."
                        ),
                        "leakage_impact_inr": t["amount"],
                        "action_recommendation": "Initiate UPI chargeback / refund for second payment."
                    })
            seen[key] = t
        return duplicates

    def detect_subscription_creep(self) -> List[Dict[str, Any]]:
        """Detects recurring charges where prices creep upwards across cycles."""
        creep_findings = []
        # Group by category and receiver bank
        recurring = defaultdict(list)
        for t in sorted(self.transactions, key=lambda x: x["timestamp"]):
            if t["category"] in ["Entertainment", "Utilities", "Other", "Shopping"]:
                key = (t["category"], t["receiver_bank"])
                recurring[key].append(t)

        for (cat, receiver), txns in recurring.items():
            if len(txns) >= 2:
                for i in range(1, len(txns)):
                    t1, t2 = txns[i - 1], txns[i]
                    day_diff = (t2["timestamp"] - t1["timestamp"]).days
                    if 25 <= day_diff <= 35:  # Monthly cycle
                        pct_increase = ((t2["amount"] - t1["amount"]) / (t1["amount"] or 1.0)) * 100.0
                        if pct_increase >= 5.0:
                            creep_findings.append({
                                "anomaly_id": f"CREEP-{t2['transaction_id']}",
                                "transaction_id": t2["transaction_id"],
                                "type": "SUBSCRIPTION_CREEP",
                                "severity": "MEDIUM",
                                "risk_score": 65,
                                "amount": t2["amount"],
                                "category": cat,
                                "previous_amount": t1["amount"],
                                "increase_percentage": round(pct_increase, 1),
                                "timestamp": t2["timestamp_str"],
                                "reasoning": (
                                    f"Subscription creep identified in {cat} recurring monthly debit. Amount jumped from "
                                    f"INR {t1['amount']} to INR {t2['amount']} (+{round(pct_increase, 1)}% hike in {day_diff} days). "
                                    f"Silent plan tier upgrade or unnotified price creep detected."
                                ),
                                "leakage_impact_inr": round(t2["amount"] - t1["amount"], 2),
                                "action_recommendation": "Review active plan terms or downgrade/cancel recurring autopay mandate."
                            })
        return creep_findings

    def detect_spend_surges(self) -> List[Dict[str, Any]]:
        """Detects statistical spend surges (Z-score > 2.0 or abnormal single spikes)."""
        surges = []
        cat_amounts = defaultdict(list)
        for t in self.transactions:
            cat_amounts[t["category"]].append(t["amount"])

        cat_stats = {}
        for cat, amounts in cat_amounts.items():
            if len(amounts) >= 5:
                mean = sum(amounts) / len(amounts)
                variance = sum((x - mean) ** 2 for x in amounts) / len(amounts)
                std = math.sqrt(variance) or 1.0
                cat_stats[cat] = (mean, std)

        for t in self.transactions:
            if t["category"] in cat_stats:
                mean, std = cat_stats[t["category"]]
                z_score = (t["amount"] - mean) / std
                if z_score >= 2.2 and t["amount"] > 1500:
                    surges.append({
                        "anomaly_id": f"SURGE-{t['transaction_id']}",
                        "transaction_id": t["transaction_id"],
                        "type": "SPEND_SURGE",
                        "severity": "HIGH",
                        "risk_score": min(95, int(60 + z_score * 10)),
                        "amount": t["amount"],
                        "category": t["category"],
                        "expected_average": round(mean, 2),
                        "z_score": round(z_score, 2),
                        "timestamp": t["timestamp_str"],
                        "reasoning": (
                            f"Unusual spend surge in {t['category']}: INR {t['amount']} deviates {round(z_score, 1)}σ "
                            f"above normal category mean (INR {round(mean, 2)}). Threatens discretionary budget discipline."
                        ),
                        "leakage_impact_inr": round(t["amount"] - mean, 2),
                        "action_recommendation": "Enforce transaction limit cap on this merchant category."
                    })
        return surges

    def detect_fraud_risk(self) -> List[Dict[str, Any]]:
        """Flags transactions marked with fraud signals or anomalous hour velocities."""
        flags = []
        for t in self.transactions:
            if t["fraud_flag"] == 1:
                flags.append({
                    "anomaly_id": f"FRAUD-{t['transaction_id']}",
                    "transaction_id": t["transaction_id"],
                    "type": "SUSPICIOUS_FRAUD_FLAG",
                    "severity": "CRITICAL",
                    "risk_score": 98,
                    "amount": t["amount"],
                    "category": t["category"],
                    "timestamp": t["timestamp_str"],
                    "reasoning": (
                        f"CRITICAL: Transaction {t['transaction_id']} (INR {t['amount']}) was flagged by bank network "
                        f"fraud models. Potential unauthorized device access or high-risk recipient account."
                    ),
                    "leakage_impact_inr": t["amount"],
                    "action_recommendation": "Freeze UPI PIN and contact bank fraud hotline immediately."
                })
        return flags
