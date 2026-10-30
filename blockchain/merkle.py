"""Cryptographic Merkle Tree implementation for verifiable transaction blocks."""
import hashlib
import json


def sha256_hash(data: str) -> str:
    """Computes standard SHA-256 hash of a string."""
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


class MerkleTree:
    """Calculates Merkle Root and generates cryptographic inclusion proofs."""

    def __init__(self, elements):
        self.elements = [
            json.dumps(e, sort_keys=True) if isinstance(e, (dict, list)) else str(e)
            for e in elements
        ]
        self.leaves = [sha256_hash(e) for e in self.elements]
        if not self.leaves:
            self.leaves = [sha256_hash("empty_block")]
        self.root = self._build_tree(self.leaves)

    def _build_tree(self, nodes):
        if not nodes:
            return sha256_hash("empty_block")
        if len(nodes) == 1:
            return nodes[0]

        next_level = []
        for i in range(0, len(nodes), 2):
            left = nodes[i]
            right = nodes[i + 1] if i + 1 < len(nodes) else left  # duplicate last node if odd
            combined = left + right
            next_level.append(sha256_hash(combined))

        return self._build_tree(next_level)

    def get_root(self) -> str:
        return self.root

    def generate_proof(self, index: int):
        """Generates Merkle audit trail proof for element at index."""
        if index < 0 or index >= len(self.leaves):
            return None

        proof = []
        current_nodes = list(self.leaves)
        idx = index

        while len(current_nodes) > 1:
            next_level = []
            is_odd = len(current_nodes) % 2 != 0
            if is_odd:
                current_nodes.append(current_nodes[-1])

            sibling_idx = idx + 1 if idx % 2 == 0 else idx - 1
            sibling = current_nodes[sibling_idx]
            position = "right" if idx % 2 == 0 else "left"
            proof.append({"position": position, "hash": sibling})

            for i in range(0, len(current_nodes), 2):
                combined = current_nodes[i] + current_nodes[i + 1]
                next_level.append(sha256_hash(combined))

            idx = idx // 2
            current_nodes = next_level

        return proof

    @staticmethod
    def verify_proof(leaf: str, proof: list, root: str) -> bool:
        """Verifies if a leaf belongs to the Merkle root via proof path."""
        current = leaf
        for p in proof:
            if p["position"] == "right":
                current = sha256_hash(current + p["hash"])
            else:
                current = sha256_hash(p["hash"] + current)
        return current == root
