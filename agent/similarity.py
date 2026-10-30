"""Transaction Similarity and Cryptographic Hashing Engine.
Generates deterministic transaction hashes (TxHash), virtual payment addresses (VPA),
and clusters transactions based on behavioral similarity and duplicate patterns.
"""
import hashlib
from typing import Dict, List, Any


def generate_tx_hash(txn_id: str, timestamp: str, sender_bank: str, receiver_bank: str, amount: float) -> str:
    """Generates a cryptographic Ethereum-style transaction hash (0x + SHA-256)."""
    raw = f"{txn_id}:{timestamp}:{sender_bank}:{receiver_bank}:{round(amount, 2)}"
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    return f"0x{digest}"


def generate_vpa(prefix: str, identifier: str, bank: str) -> str:
    """Generates deterministic Virtual Payment Address (e.g. user_del_82@sbi)."""
    clean_bank = (bank or "upi").lower().replace(" ", "")
    clean_id = hashlib.md5(f"{prefix}_{identifier}".encode("utf-8")).hexdigest()[:6]
    return f"{prefix}_{clean_id}@{clean_bank}"


class SimilarityEngine:
    """Calculates behavioral similarity and unique transaction metrics."""

    @staticmethod
    def compute_similarity(t1: Dict[str, Any], t2: Dict[str, Any]) -> float:
        """Computes a multi-factor similarity score [0.0 - 1.0] between two transactions."""
        score = 0.0

        # Exact amount match: 40%
        amt1 = float(t1.get("amount", 0.0))
        amt2 = float(t2.get("amount", 0.0))
        if amt1 == amt2:
            score += 0.40
        elif abs(amt1 - amt2) / (max(amt1, amt2) or 1.0) <= 0.05:
            score += 0.25

        # Merchant category match: 25%
        if t1.get("merchant_category") == t2.get("merchant_category"):
            score += 0.25

        # Bank routing match: 20%
        if t1.get("sender_bank") == t2.get("sender_bank") and t1.get("receiver_bank") == t2.get("receiver_bank"):
            score += 0.20
        elif t1.get("sender_bank") == t2.get("sender_bank"):
            score += 0.10

        # Transaction type match: 15%
        if t1.get("transaction_type") == t2.get("transaction_type"):
            score += 0.15

        return round(score, 3)

    @classmethod
    def find_similar_clusters(cls, transactions: List[Dict[str, Any]], threshold: float = 0.85) -> List[Dict[str, Any]]:
        """Clusters similar and duplicate transactions."""
        clusters = []
        visited = set()

        for i, t1 in enumerate(transactions):
            if i in visited:
                continue
            group = [t1]
            visited.add(i)

            for j in range(i + 1, min(i + 100, len(transactions))):
                if j in visited:
                    continue
                t2 = transactions[j]
                sim = cls.compute_similarity(t1, t2)
                if sim >= threshold:
                    group.append(t2)
                    visited.add(j)

            if len(group) > 1:
                clusters.append({
                    "cluster_id": f"SIM-CLUSTER-{t1.get('transaction_id', i)}",
                    "similarity_score": threshold,
                    "items_count": len(group),
                    "category": t1.get("merchant_category", "Unknown"),
                    "sample_amount": t1.get("amount", 0.0),
                    "transactions": [t.get("transaction_id") for t in group]
                })

        return clusters
