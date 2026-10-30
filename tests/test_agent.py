"""Offline tests (no API key). Run: python -m unittest discover tests"""
import json
import os
import subprocess
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agent.core import AgentExecutor, parse_json
from agent.auditor import ExpenseAuditor
from agent.budget import BudgetRebalancer
from blockchain.ledger import BlockchainLedger
from blockchain.merkle import MerkleTree
from blockchain.pow import mine_block, verify_pow
from tools import build_tools


class Scripted:
    def __init__(self, replies):
        self.replies = list(replies)

    def generate(self, system, messages):
        return self.replies.pop(0) if self.replies else '{"final_answer": "done"}'


class AgentTests(unittest.TestCase):
    def test_parse_json_handles_fences(self):
        self.assertEqual(parse_json('text ```json\n{"a": 1}\n``` more'), {"a": 1})

    def test_tool_call_then_final(self):
        llm = Scripted([
            '{"thought":"t","action":"read_file","args":{"filename":"scores.csv"}}',
            '{"thought":"t","final_answer":"recursion is weak"}'
        ])
        answer, trace = AgentExecutor(llm, build_tools()).run("q")
        self.assertEqual(answer, "recursion is weak")
        self.assertEqual(trace[0]["tool"], "read_file")
        self.assertIn("recursion", trace[0]["observation"])

    def test_tool_error_becomes_observation(self):
        llm = Scripted([
            '{"action":"read_file","args":{"filename":"nope.csv"}}',
            '{"final_answer":"x"}'
        ])
        _, trace = AgentExecutor(llm, build_tools()).run("q")
        self.assertTrue(trace[0]["observation"].startswith("ERROR"))

    def test_iteration_cap(self):
        llm = Scripted(['{"action":"list_files","args":{}}'] * 20)
        answer, trace = AgentExecutor(llm, build_tools(), max_iterations=3).run("q")
        self.assertLessEqual(len(trace), 3)

    def test_sql_and_calculator(self):
        t = build_tools()
        self.assertIn("recursion", t["sql_query"].execute(filename="scores.csv", sql="SELECT topic FROM data WHERE score < 40"))
        self.assertEqual(t["calculator"].execute(expression="2+2*10"), 22)

    def test_cli_contract(self):
        out = subprocess.run([sys.executable, "main.py", "--json", "--dry-run", "hi"], capture_output=True, text=True)
        d = json.loads(out.stdout.strip().splitlines()[-1])
        self.assertTrue(d["answer"] and len(d["trace"]) >= 2)

    def test_blockchain_merkle_and_pow(self):
        txns = ["TXN1:868:Food", "TXN2:1011:Grocery", "TXN3:477:Entertainment"]
        tree = MerkleTree(txns)
        root = tree.get_root()
        self.assertTrue(len(root) == 64)

        mining = mine_block(index=1, prev_hash="0"*64, merkle_root=root, data_summary="test", difficulty=2)
        self.assertTrue(mining["hash"].startswith("00"))
        self.assertTrue(verify_pow(1, "0"*64, mining["timestamp"], root, "test", mining["nonce"], mining["hash"], difficulty=2))

    def test_expense_auditor_and_budget(self):
        sample_rows = [
            {"transaction id": "T1", "timestamp": "2024-01-01 10:00:00", "merchant_category": "Food", "amount (INR)": "500", "sender_bank": "SBI", "receiver_bank": "HDFC"},
            {"transaction id": "T2", "timestamp": "2024-01-01 10:04:00", "merchant_category": "Food", "amount (INR)": "500", "sender_bank": "SBI", "receiver_bank": "HDFC"},
            {"transaction id": "T3", "timestamp": "2024-01-02 12:00:00", "merchant_category": "Shopping", "amount (INR)": "15000", "sender_bank": "ICICI", "receiver_bank": "Axis"},
        ]
        auditor = ExpenseAuditor(sample_rows)
        res = auditor.run_full_audit()
        self.assertGreaterEqual(res["duplicates_count"], 1)

        rebalancer = BudgetRebalancer(res)
        plan = rebalancer.generate_plan(50000)
        self.assertEqual(plan["status"], "OPTIMIZED")
        self.assertGreater(plan["projected_monthly_savings_inr"], 0)


if __name__ == "__main__":
    unittest.main()
