# Expense Auditor & Anomaly Hunter Studio

[![AgentX 2026](https://img.shields.io/badge/AgentX-Challenge_2026-6366f1.svg)](https://github.com/nevathxavier-afk/demo)
[![Finance & Risk](https://img.shields.io/badge/Track-Finance_%26_Risk-10b981.svg)]()
[![Proof-of-Work Blockchain](https://img.shields.io/badge/Audit_Trail-PoW_Blockchain-f59e0b.svg)]()
[![Offline Tests](https://img.shields.io/badge/Tests-10%20Passing%20(100%25)-06b6d4.svg)]()
[![Volume Audited](https://img.shields.io/badge/Volume-250%2C000%20Txns%20(%E2%82%B932.79%20Cr)-8b5cf6.svg)]()
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nevathxavier-afk/expense-auditor-agentx/blob/main/notebooks/agentx_colab.ipynb)

**A UPI or bank statement in, a rebalanced budget plan out.**

Autonomous Finance & Risk agent built for the **AgentX Challenge 2026** (SRMIST Tiruchirappalli). Analyzes UPI and bank statements over **250,000 transactions (₹ 32.79 Crores)**, multi-level auto-categorizes purchases across survival and lifestyle themes, hunts duplicate debits, detects creeping subscriptions, flags spend surges with cognitive reasoning, seals audit findings into an immutable **Proof-of-Work (PoW) Blockchain Ledger**, and outputs a personalized 50/30/20 rebalanced budget plan.

---

## Key Features

1. **250,000 Transactions Ingested & Analyzed**:
   - Total Spend Volume: **₹ 327,939,009.00 (₹ 32.79 Crores)** across 250,000 transactions.
   - Average Transaction: **₹ 1,311.76**.
   - Sub-second SQL querying via indexed B-trees on timestamp, amount, and category.
2. **Multi-Level Financial Themes & Categorization**:
   - **Level 1 (Macro Themes)**: Essential Survival (₹15.69 Cr), Lifestyle & Discretionary (₹10.50 Cr), Future Growth & Education (₹3.87 Cr), Transit & Commute (₹2.73 Cr).
   - **Level 2 (50/30/20 Needs vs Wants)**: Needs (50%), Wants (30%), High-Yield Savings (20%).
   - **Level 3 (Channel Routing)**: P2P (112,445 txns), P2M (87,660 txns), Bill Payments (37,368 txns), Autopay Recharges (12,527 txns).
   - **Level 4 (Demographics & Geography)**: Age groups, 8 major states (Maharashtra, UP, Karnataka, Tamil Nadu, Delhi), and 8 major banks (SBI, HDFC, ICICI, IndusInd, Axis).
3. **Cognitive Anomaly Hunter**:
   - **Duplicate Detection**: Identical amounts to same recipient within sliding 15-min window (accidental double-clicks / network retries).
   - **Subscription Creep**: Recurring 25–35 day debits with silent price increases ($>5\%$).
   - **Discretionary Spend Surges**: Rolling Z-scores ($Z \ge 2.2\sigma$) and volatility modeling flagging discretionary budget hemorrhages.
   - **Confirmed Network Fraud**: Pinpointed 480 high-risk fraudulent transactions with critical severity tags.
4. **Cryptographic Transaction Hashes & VPAs**:
   - Every transaction receives an Ethereum-style SHA-256 hash (`0x...`).
   - Generates privacy-preserving pseudo-VPAs (e.g. `user_mh_26@sbi` $\rightarrow$ `merchant_grocery@hdfc`).
5. **Interactive Tamper Testing Arena & Multi-Node Verification**:
   - Injects adversarial alterations into audit blocks (e.g., mutating amounts or recipients).
   - Real-time verification detects Merkle Root mismatch, Proof-of-Work nonce invalidation, and broken chain links.
   - Streams live consensus logs from 3 simulated validator nodes (**Node Alpha: Fraud Validator**, **Node Beta: Merkle Auditor**, **Node Gamma: PoW Consensus**).
   - One-click cryptographic self-healing restores certified on-chain ledger state.
6. **Dynamic 50/30/20 Budget Rebalancer**:
   - Plugs detected leakage directly into high-yield emergency reserves.
   - Category-by-category daily spending limits and 3-year compound wealth growth projections ($8.0\%$ CAGR).

---

## Dataset Profile (250,000 Transactions)

| Dimension | Metric / Distribution |
| :--- | :--- |
| **Total Transactions** | 250,000 rows |
| **Total Volume** | ₹ 327,939,009.00 (₹ 32.79 Cr) |
| **Top Categories by Volume** | Shopping (₹7.68 Cr), Grocery (₹5.83 Cr), Utilities (₹5.27 Cr), Fuel (₹3.90 Cr), Education (₹3.87 Cr) |
| **Top Banking Channels** | SBI (62,693), HDFC (37,485), ICICI (29,769), IndusInd (25,173), Axis (25,042) |
| **Top States** | Maharashtra (37,427 txns), Uttar Pradesh (30,125 txns), Karnataka (29,756 txns), Tamil Nadu (25,367 txns) |
| **Network Fraud Flags** | 480 critical transactions flagged |

---

## Run It (3 Steps)

```bash
# 1. Clone & enter repository
git clone https://github.com/nevathxavier-afk/expense-auditor-agentx.git && cd expense-auditor-agentx

# 2. Set up virtual environment & install dependencies
python3 -m venv venv && source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                                   # Add GEMINI_API_KEY or GROQ_API_KEY (both free)

# 3. Test setup with zero API keys required (Dry-Run mode)
python main.py --dry-run "Audit the UPI statement and propose a rebalanced budget"

# 4. Run real agent
python main.py "Audit sample_transactions.csv, find duplicate charges, and mine an audit block"

# 5. Launch the interactive Cyber-FinTech Dashboard & REST API
python serve.py
# Opens dashboard at http://localhost:8000
```

---

## Layout

```
main.py                 entry point + the judges' contract (--json & --dry-run)
serve.py                high-performance REST API & Cyber-FinTech dashboard server
agent/core.py           the ReAct loop, step cap, repeat guard, error recovery
agent/llm.py            Gemini / Groq wrapper with 429 retry + DryRunLLM
agent/prompt_builder.py system prompt with Finance & Risk Auditor ROLE
agent/auditor.py        multi-level anomaly detection engine (duplicates, creep, surges, fraud)
agent/similarity.py     transaction similarity engine, 0x TxHashes, and VPA addresses
agent/budget.py         50/30/20 dynamic personalized budget rebalancer
blockchain/ledger.py    tamper-evident audit blockchain & certificate issuer
blockchain/merkle.py    SHA-256 Merkle tree & inclusion proof verifier
blockchain/pow.py       Proof-of-Work consensus mining engine
blockchain/zk_proofs.py zero-knowledge style verifiable expense proofs
blockchain/tamper_test.py tamper testing arena with multi-node consensus telemetry
tools/                  registry (__init__.py), data_query, calculator, web_search,
                        auditor_tool, blockchain_tool, budget_tool
config/__init__.py      models, MAX_ITERATIONS, data folder, PoW difficulty
data/                   UPI transactions dataset (250,000 rows) + sample files + audit_ledger.json
data/indexer.py         high-speed SQLite indexer for 250,000 rows
dashboard/              cyber-fintech dashboard with live PoW animation & tamper testing
tests/test_agent.py     offline unit tests (10 tests, 100% pass): python -m unittest discover tests
notebooks/              Google Colab notebook with 1-click execution
```

---

## The Judges' Contract (`--json`)

Judges evaluate the agent using the machine flag `--json`:
- **Stdout**: Exactly ONE line of valid JSON:
  ```json
  {"answer": "...", "trace": [{"thought": "...", "tool": "...", "args": {...}, "observation": "..."}]}
  ```
- **Stderr**: Diagnostic logs and step traces (clean separation).
- **Offline test suite**:
  ```bash
  python -m unittest discover tests
  # Ran 10 tests in 0.348s -> OK
  ```

---

## Simulated Proof-of-Work Audit Flow

```
[ UPI Statement In (250,000 Transactions) ]
                    │
                    ▼
[ Expense Auditor & Anomaly Hunter ]
  ├─ Auto-categorize & assign Themes (Survival, Lifestyle, Growth, Transit)
  ├─ Detect Duplicates (<= 15 min sliding window)
  ├─ Detect Subscription Creep (> 5% hike in 25-35 days)
  ├─ Detect Spend Surges (Z-Score >= 2.2 sigma)
  └─ Generate 0x TxHashes & VPAs
                    │
                    ▼
[ Merkle Tree Aggregation ] ──► Computes Merkle Root
                    │
                    ▼
[ PoW Mining Engine ] ────────► Solves SHA-256 nonce challenge (Difficulty >= 3)
                    │
                    ▼
[ Multi-Node Consensus ] ─────► Alpha, Beta, Gamma Auditor Signatures
                    │
                    ▼
[ Tamper-Proof Audit Certificate & Rebalanced 50/30/20 Budget Plan Out ]
```

---

## License

Built for the **AgentX Challenge 2026**. Released under the MIT License.
