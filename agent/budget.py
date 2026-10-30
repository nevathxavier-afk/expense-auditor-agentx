"""Personalized Dynamic Budget Rebalancer Engine.
Translates raw audited expenses into an optimized, leak-free financial budget plan.
Adheres to the 50/30/20 framework with real-time anomaly leakage plugging.
"""
from typing import Dict, List, Any


class BudgetRebalancer:
    """Computes personalized rebalanced budget allocations and projected savings."""

    def __init__(self, audit_results: Dict[str, Any]):
        self.audit = audit_results
        self.category_spend = audit_results.get("category_spend_breakdown", {})
        self.total_spend = audit_results.get("total_spend_inr", 0.0)
        self.anomalies = audit_results.get("anomalies", [])

    def generate_plan(self, monthly_income: float = None) -> Dict[str, Any]:
        """Proposes a personalized rebalanced budget plan with leakage cuts."""
        if monthly_income is None or monthly_income <= 0:
            monthly_income = max(10000.0, self.total_spend * 1.18)

        # 1. Categorize into Needs, Wants, Savings
        needs_categories = ["Grocery", "Utilities", "Fuel & Travel", "Healthcare"]
        wants_categories = ["Food & Dining", "Shopping", "Entertainment", "Discretionary Other"]
        
        current_needs = sum(self.category_spend.get(c, 0.0) for c in needs_categories)
        current_wants = sum(self.category_spend.get(c, 0.0) for c in wants_categories)
        current_savings = max(0.0, monthly_income - (current_needs + current_wants))

        # 2. Compute Direct Leakage Savings from Auditor Findings
        duplicate_waste = sum(a.get("leakage_impact_inr", 0.0) for a in self.anomalies if a.get("type") == "DUPLICATE_PAYMENT")
        creep_waste = sum(a.get("leakage_impact_inr", 0.0) for a in self.anomalies if a.get("type") == "SUBSCRIPTION_CREEP")
        surge_waste = sum(a.get("leakage_impact_inr", 0.0) for a in self.anomalies if a.get("type") == "SPEND_SURGE") * 0.50
        total_leakage_plugged = duplicate_waste + creep_waste + surge_waste

        # 3. Target 50/30/20 Ideal Allocations
        target_needs = monthly_income * 0.50
        target_wants = monthly_income * 0.30
        target_savings = monthly_income * 0.20

        # 4. Rebalanced Dynamic Allocation
        rebalanced_needs = max(0.0, current_needs - duplicate_waste)
        rebalanced_wants = max(0.0, current_wants - (creep_waste + surge_waste))
        rebalanced_savings = max(target_savings, monthly_income - (rebalanced_needs + rebalanced_wants))

        # 5. Category-level daily spending limits
        category_caps = {}
        for cat, spend in self.category_spend.items():
            if cat in needs_categories:
                rebalanced_cat_monthly = spend * 0.95
            elif cat in wants_categories:
                rebalanced_cat_monthly = spend * 0.78
            else:
                rebalanced_cat_monthly = spend * 0.85
            category_caps[cat] = {
                "current_spend_inr": round(spend, 2),
                "rebalanced_monthly_inr": round(rebalanced_cat_monthly, 2),
                "recommended_daily_cap_inr": round(rebalanced_cat_monthly / 30.0, 2)
            }

        # 6. Projected Wealth Accumulation Impact
        monthly_freed_cashflow = max(total_leakage_plugged, round(self.total_spend * 0.15, 2), 500.0)
        annual_savings = monthly_freed_cashflow * 12.0
        three_year_wealth_impact = annual_savings * 3.4

        return {
            "status": "OPTIMIZED",
            "benchmark_model": "50/30/20 Adaptive Rebalancer",
            "monthly_income_baseline_inr": round(monthly_income, 2),
            "current_breakdown": {
                "needs_inr": round(current_needs, 2),
                "needs_pct": round((current_needs / monthly_income) * 100, 1),
                "wants_inr": round(current_wants, 2),
                "wants_pct": round((current_wants / monthly_income) * 100, 1),
                "savings_inr": round(current_savings, 2),
                "savings_pct": round((current_savings / monthly_income) * 100, 1)
            },
            "rebalanced_breakdown": {
                "needs_inr": round(rebalanced_needs, 2),
                "needs_pct": round((rebalanced_needs / monthly_income) * 100, 1),
                "wants_inr": round(rebalanced_wants, 2),
                "wants_pct": round((rebalanced_wants / monthly_income) * 100, 1),
                "savings_inr": round(rebalanced_savings, 2),
                "savings_pct": round((rebalanced_savings / monthly_income) * 100, 1)
            },
            "leakage_plugged_monthly_inr": round(total_leakage_plugged, 2),
            "projected_monthly_savings_inr": round(monthly_freed_cashflow, 2),
            "projected_annual_savings_inr": round(annual_savings, 2),
            "projected_3yr_compounded_impact_inr": round(three_year_wealth_impact, 2),
            "category_rebalancing_caps": category_caps,
            "strategic_recommendations": [
                f"Eliminate duplicate payment leakage: Save INR {round(duplicate_waste, 2)} immediately.",
                f"Prune creeping subscriptions: Save INR {round(creep_waste, 2)} recurring monthly.",
                f"Cap category spend surges: Recovers INR {round(surge_waste, 2)} in discretionary bandwidth.",
                f"Auto-transfer freed INR {round(monthly_freed_cashflow, 2)} to liquid emergency reserve on payday."
            ]
        }
