"""
AgentX 2026 - Dataset Ingestion & Update Utility
Allows developers, users, and judges to easily update or ingest any UPI/bank statement CSV into the audit engine.

Usage:
    python update_dataset.py --csv path/to/transactions.csv
    python update_dataset.py --dry-run
"""

import os
import sys
import csv
import json
import hashlib
import argparse
from typing import List, Dict, Any

def sha256_hash(data: str) -> str:
    return hashlib.sha256(data.encode("utf-8")).hexdigest()

def compute_merkle_root(tx_hashes: List[str]) -> str:
    if not tx_hashes:
        return sha256_hash("EMPTY_LEDGER")
    current_level = tx_hashes[:]
    while len(current_level) > 1:
        next_level = []
        for i in range(0, len(current_level), 2):
            left = current_level[i]
            right = current_level[i+1] if i+1 < len(current_level) else left
            next_level.append(sha256_hash(left + right))
        current_level = next_level
    return current_level[0]

def update_dataset(csv_path: str, dry_run: bool = False):
    print("=" * 65)
    print("  AGENTX 2026: DATASET INGESTION & CRYPTOGRAPHIC UPDATE PIPELINE")
    print("=" * 65)
    
    if not os.path.exists(csv_path):
        print(f"[-] Error: Specified file '{csv_path}' does not exist.")
        sys.exit(1)
        
    print(f"[*] Ingesting and validating stream from: {csv_path}")
    
    records = []
    tx_hashes = []
    total_volume = 0.0
    categories: Dict[str, float] = {}
    banks: Dict[str, int] = {}
    anomalies = []
    
    with open(csv_path, "r", encoding="utf-8", errors="ignore") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tx_id = row.get("transaction_id", f"TXN_{len(records)+1}")
            date = row.get("date", "2024-01-01 00:00")
            try:
                amt = float(row.get("amount", 0.0))
            except ValueError:
                amt = 0.0
            merch = row.get("merchant", "Unknown Merchant")
            cat = row.get("category", "Uncategorized")
            bank = row.get("bank", "Default Bank")
            vpa = row.get("vpa", f"{merch.lower().replace(' ', '')}@{bank.lower()}")
            
            # Compute leaf hash
            raw_payload = f"{tx_id}|{date}|{amt:.2f}|{merch}|{cat}|{bank}|{vpa}"
            leaf_h = sha256_hash(raw_payload)
            
            records.append({
                "tx_id": tx_id,
                "date": date,
                "amount": amt,
                "merchant": merch,
                "category": cat,
                "bank": bank,
                "vpa": vpa,
                "hash": leaf_h
            })
            tx_hashes.append(leaf_h)
            total_volume += amt
            categories[cat] = categories.get(cat, 0.0) + amt
            banks[bank] = banks.get(bank, 0) + 1
            
            # Simple heuristic detection for sample
            if len(records) > 1:
                prev = records[-2]
                if prev["merchant"] == merch and abs(prev["amount"] - amt) < 0.01:
                    anomalies.append(f"Duplicate charge detected: {tx_id} identical to {prev['tx_id']} (₹{amt})")
            if amt > 15000:
                anomalies.append(f"Discretionary spend surge: {tx_id} (₹{amt:,.2f}) > ₹15,000 threshold")

    merkle_root = compute_merkle_root(tx_hashes)
    
    print(f"[+] Successfully Ingested: {len(records):,} transactions")
    print(f"[+] Total Audited Volume: INR {total_volume:,.2f}")
    print(f"[+] Computed SHA-256 Merkle Root: {merkle_root}")
    print(f"[+] Detected Heuristic Anomalies: {len(anomalies)} flags")
    print(f"[+] Category Count: {len(categories)} distinct buckets")
    print(f"[+] Top Gateway: {max(banks, key=banks.get) if banks else 'N/A'}")
    
    if not dry_run:
        summary_path = os.path.join("data", "last_ingestion_summary.json")
        os.makedirs("data", exist_ok=True)
        with open(summary_path, "w", encoding="utf-8") as f:
            json.dump({
                "source_file": csv_path,
                "transaction_count": len(records),
                "total_volume": round(total_volume, 2),
                "merkle_root": merkle_root,
                "anomaly_count": len(anomalies),
                "top_categories": sorted(categories.items(), key=lambda x: x[1], reverse=True)[:5]
            }, f, indent=2)
        print(f"[✓] Ingestion metadata saved to: {summary_path}")
        print("[✓] Ready for autonomous ReAct agent audit!")
    else:
        print("[*] Dry run mode completed. Zero persistent modifications made.")
    print("=" * 65)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AgentX Statement Update Utility")
    parser.add_argument("--csv", type=str, default="data/sample_transactions.csv", help="Path to CSV statement")
    parser.add_argument("--dry-run", action="store_true", help="Validate without writing state")
    args = parser.parse_args()
    
    update_dataset(args.csv, args.dry_run)
