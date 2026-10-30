"""High-performance SQLite indexer for 250,000+ UPI Statement rows."""
import csv
import os
import sqlite3
import sys
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
CSV_PATH = os.path.join(DATA_DIR, "upi_transactions_2024.csv")
DB_PATH = os.path.join(DATA_DIR, "transactions.db")


def build_index():
    if not os.path.exists(CSV_PATH):
        print(f"Dataset not found at {CSV_PATH}")
        return

    print("Building high-speed SQLite index for 250,000 UPI transactions...")
    t0 = time.time()
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id TEXT PRIMARY KEY,
            timestamp TEXT,
            transaction_type TEXT,
            merchant_category TEXT,
            amount REAL,
            transaction_status TEXT,
            sender_age_group TEXT,
            receiver_age_group TEXT,
            sender_state TEXT,
            sender_bank TEXT,
            receiver_bank TEXT,
            device_type TEXT,
            network_type TEXT,
            fraud_flag INTEGER,
            hour_of_day INTEGER,
            day_of_week TEXT,
            is_weekend INTEGER
        )
    """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_cat ON transactions(merchant_category)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_ts ON transactions(timestamp)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_amt ON transactions(amount)")

    with open(CSV_PATH, "r", encoding="utf-8", errors="ignore") as f:
        reader = csv.reader(f)
        header = next(reader)
        batch = []
        count = 0
        for row in reader:
            if len(row) >= 17:
                batch.append((
                    row[0], row[1], row[2], row[3], float(row[4] or 0), row[5],
                    row[6], row[7], row[8], row[9], row[10], row[11], row[12],
                    int(row[13] or 0), int(row[14] or 0), row[15], int(row[16] or 0)
                ))
                count += 1
                if len(batch) >= 10000:
                    cur.executemany("INSERT OR IGNORE INTO transactions VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", batch)
                    batch = []
        if batch:
            cur.executemany("INSERT OR IGNORE INTO transactions VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", batch)
    conn.commit()
    conn.close()
    print(f"Successfully indexed {count} transactions into {DB_PATH} in {time.time()-t0:.2f}s")


if __name__ == "__main__":
    build_index()
