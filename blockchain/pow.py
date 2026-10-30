"""Proof-of-Work (PoW) consensus simulation engine for financial audit validation."""
import hashlib
import time


def calculate_hash(index: int, prev_hash: str, timestamp: float, merkle_root: str, data_summary: str, nonce: int) -> str:
    """Computes SHA-256 block hash for proof-of-work header."""
    header = f"{index}:{prev_hash}:{timestamp}:{merkle_root}:{data_summary}:{nonce}"
    return hashlib.sha256(header.encode("utf-8")).hexdigest()


def mine_block(index: int, prev_hash: str, merkle_root: str, data_summary: str, difficulty: int = 3):
    """Mines a block by solving the Proof-of-Work cryptographic challenge.
    
    Finds a nonce such that SHA-256(header) starts with `0` repeated `difficulty` times.
    Returns: (nonce, block_hash, duration_seconds, hash_count)
    """
    target_prefix = "0" * max(1, difficulty)
    nonce = 0
    start_time = time.time()
    timestamp = time.time()

    while True:
        current_hash = calculate_hash(index, prev_hash, timestamp, merkle_root, data_summary, nonce)
        if current_hash.startswith(target_prefix):
            duration = max(0.001, time.time() - start_time)
            hash_rate = int(nonce / duration) if nonce > 0 else 1
            return {
                "nonce": nonce,
                "hash": current_hash,
                "timestamp": timestamp,
                "duration_seconds": round(duration, 4),
                "hash_count": nonce + 1,
                "hash_rate_hps": hash_rate,
                "difficulty": difficulty,
                "target_prefix": target_prefix
            }
        nonce += 1


def verify_pow(index: int, prev_hash: str, timestamp: float, merkle_root: str, data_summary: str, nonce: int, expected_hash: str, difficulty: int) -> bool:
    """Verifies that a mined block's proof-of-work is mathematically valid."""
    target_prefix = "0" * difficulty
    calculated = calculate_hash(index, prev_hash, timestamp, merkle_root, data_summary, nonce)
    return calculated == expected_hash and calculated.startswith(target_prefix)
