"""Zero-Knowledge style Verifiable Expense Proofs.
Allows users to prove compliance, tax deductibility, or audit approval
without disclosing sensitive PII or raw bank details.
"""
import hashlib
import json
import secrets


def generate_commitment(amount: float, category: str, transaction_id: str, salt: str = None) -> dict:
    """Generates a cryptographic commitment hash for an expense item.
    
    Commitment = SHA256(transaction_id || amount || category || salt)
    """
    if salt is None:
        salt = secrets.token_hex(16)
    
    payload = f"{transaction_id}:{round(amount, 2)}:{category}:{salt}"
    commitment_hash = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    
    return {
        "commitment_hash": commitment_hash,
        "salt": salt,
        "masked_id": f"TXN...{transaction_id[-4:]}" if len(transaction_id) > 4 else transaction_id,
        "category": category,
        "amount_range": _get_amount_bracket(amount)
    }


def verify_commitment(commitment_hash: str, amount: float, category: str, transaction_id: str, salt: str) -> bool:
    """Verifies that an opening of a commitment matches the claimed commitment hash."""
    payload = f"{transaction_id}:{round(amount, 2)}:{category}:{salt}"
    calculated = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    return calculated == commitment_hash


def _get_amount_bracket(amount: float) -> str:
    """Masks exact amount into private compliance bands for ZK reporting."""
    if amount < 500:
        return "< INR 500 (Micro-expense)"
    elif amount < 2000:
        return "INR 500 - 2,000 (Standard expense)"
    elif amount < 10000:
        return "INR 2,000 - 10,000 (Significant expense)"
    elif amount < 50000:
        return "INR 10,000 - 50,000 (High-value expense)"
    else:
        return "> INR 50,000 (Whale transaction)"
