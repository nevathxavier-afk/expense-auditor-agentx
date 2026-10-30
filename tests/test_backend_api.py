"""Unit tests for the Cyber-FinTech Backend REST API, dispute engine, and ZK proofs."""
import json
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agent.dispute import generate_npci_dispute_memo
from blockchain.zk_proofs import generate_commitment, verify_commitment
from blockchain.tamper_test import compute_avalanche_effect
from blockchain.pow import mine_block, verify_pow

class BackendAPITests(unittest.TestCase):
    def test_dispute_memo_generation(self):
        memo = generate_npci_dispute_memo(
            dispute_type="DUPLICATE",
            transaction_id="TXN0000000001",
            amount=868.0,
            merchant="Swiggy",
            sender_bank="HDFC",
            receiver_bank="Axis",
            reason="Double debit on gateway timeout"
        )
        self.assertEqual(memo["status"], "DISPUTE_FILED")
        self.assertTrue(memo["dispute_urn"].startswith("DISP-UPI-"))
        self.assertEqual(memo["sla_resolution_hours"], 24)
        self.assertIn("NATIONAL PAYMENTS CORPORATION OF INDIA", memo["formal_memorandum_text"])
        self.assertIn("TXN0000000001", memo["formal_memorandum_text"])

    def test_zk_expense_commitment_and_verification(self):
        proof = generate_commitment(1499.0, "Entertainment", "TXN_ZK_001")
        self.assertEqual(len(proof["commitment_hash"]), 64)
        self.assertEqual(len(proof["salt"]), 32)
        
        # Valid verification
        valid = verify_commitment(proof["commitment_hash"], 1499.0, "Entertainment", "TXN_ZK_001", proof["salt"])
        self.assertTrue(valid)
        
        # Invalid amount fails verification
        tampered_amt = verify_commitment(proof["commitment_hash"], 1500.0, "Entertainment", "TXN_ZK_001", proof["salt"])
        self.assertFalse(tampered_amt)

    def test_avalanche_effect_shannon_criterion(self):
        orig = "TXN001:amount=14850.00:user=user_del_25@axis"
        mut = "TXN001:amount=14850.01:user=user_del_25@axis"
        res = compute_avalanche_effect(orig, mut)
        
        self.assertEqual(len(res["original_hash"]), 64)
        self.assertEqual(len(res["modified_hash"]), 64)
        self.assertGreater(res["hamming_distance"], 100)
        self.assertGreaterEqual(res["avalanche_percentage"], 45.0)
        self.assertLessEqual(res["avalanche_percentage"], 55.0)
        self.assertTrue(res["is_avalanche_ideal"])

    def test_pow_mining_and_verification(self):
        res = mine_block(index=2, prev_hash="000abc" + "0"*58, merkle_root="a"*64, data_summary="Block #2", difficulty=2)
        self.assertTrue(res["hash"].startswith("00"))
        self.assertTrue(verify_pow(2, "000abc" + "0"*58, res["timestamp"], "a"*64, "Block #2", res["nonce"], res["hash"], difficulty=2))

if __name__ == "__main__":
    unittest.main()
