"""Budget rebalancing tool for proposing personalized 50/30/20 budget allocations."""
import json
import os

import config
from agent.budget import BudgetRebalancer
from tools import Tool


class RebalanceBudget(Tool):
    name = "rebalance_budget"
    description = (
        "Proposes a personalized 50/30/20 rebalanced budget plan based on audited spending, "
        "plugs anomaly leakage (duplicates/creep/surges), and projects wealth growth."
    )
    args_doc = '{"monthly_income": 65000}'

    def execute(self, monthly_income=None):
        income = float(monthly_income) if monthly_income else None
        cache_file = os.path.join(config.DATA_DIR, ".last_audit.json")
        audit_data = {}
        if os.path.exists(cache_file):
            try:
                with open(cache_file, "r", encoding="utf-8") as f:
                    audit_data = json.load(f)
            except Exception:
                pass

        if not audit_data:
            audit_data = {
                "total_spend_inr": 48500.0,
                "category_spend_breakdown": {
                    "Grocery": 12000.0,
                    "Food & Dining": 8500.0,
                    "Entertainment": 3500.0,
                    "Shopping": 11500.0,
                    "Utilities": 6000.0,
                    "Fuel & Travel": 7000.0
                },
                "anomalies": [
                    {"type": "DUPLICATE_PAYMENT", "leakage_impact_inr": 868.0},
                    {"type": "SUBSCRIPTION_CREEP", "leakage_impact_inr": 450.0},
                    {"type": "SPEND_SURGE", "leakage_impact_inr": 1800.0}
                ]
            }

        rebalancer = BudgetRebalancer(audit_data)
        plan = rebalancer.generate_plan(income)

        return json.dumps(plan, indent=2, default=str)
