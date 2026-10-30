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

## 13 Core Working Features & Interactive Capabilities

1. **Big-Data Command Center (250,000 Transactions Ingested & Audited)**:
   - Full ₹ 32.79 Cr volume audit across 250,000 UPI transactions.
   - Real-time macro-themes breakdown: Essential Survival (₹15.69 Cr), Lifestyle & Wants (₹10.50 Cr), Future Growth & Education (₹3.87 Cr), Transit & Commute (₹2.73 Cr).
   - Top merchant category shares and banking distribution across 5 major gateways (SBI, HDFC, ICICI, IndusInd, Axis).
2. **Big-Data Transaction Explorer (Search, Multi-Filter, Sort & Pagination)**:
   - Real-time multi-filter by Theme, Category, Bank, and Risk Tier (<50 Low, 50-80 Medium, >80 Critical Fraud).
   - Dynamic column sorting by TxID, Category, Amount, and Risk Score.
   - Interactive transaction inspection modal revealing 64-character SHA-256 hash, verified Merkle Leaf Index, sender/recipient VPAs, and risk factors.
3. **Cognitive AI Anomaly Hunter & Reasoning Engine**:
   - Duplicate debit detection (sliding window $\le 15$ min accidental double-taps).
   - Subscription creep monitoring ($>5\%$ stealth hikes across 25–35 day billing cycles).
   - Discretionary spend surges ($Z \ge 2.2\sigma$) exceeding rolling volatility bounds.
   - 480 confirmed network fraud flags with instant "Explainable AI" reasoning.
4. **Official NPCI UPI Dispute & Chargeback Generator**:
   - 1-click generator for official NPCI ODR-compliant chargeback memos containing transaction ID, cryptographic hash, and heuristic justification ready to submit to banking portals.
5. **Live In-Browser Proof-of-Work (PoW) Mining Station**:
   - Configurable mining difficulty slider (Difficulty 1 to 4: `0...` to `0000...`).
   - Live browser-based WebCrypto SHA-256 mining rig computing real nonces, displaying kH/s hashrate, time elapsed, and dynamically appending mined blocks to the live blockchain.
6. **Adversarial Tamper Testing Arena & Multi-Node Consensus Sandbox**:
   - Adversary simulator injecting fraudulent amounts (e.g. ₹14,850 $\rightarrow$ ₹86,800) into audited blocks.
   - 3 independent validator nodes (**Node Alpha: Fraud Heuristics**, **Node Beta: Merkle Tree Cryptographer**, **Node Gamma: PoW Nonce Validator**).
   - Streaming terminal telemetry showing consensus rejection of tampering.
   - One-click cryptographic self-healing restoring certified on-chain records.
7. **Zero-Knowledge (ZK) Expense Proof Generator & Independent Verifier**:
   - Generates privacy-preserving salted cryptographic commitments: $C = \text{SHA256}(\text{Amount} \parallel \text{Ceiling} \parallel \text{Salt})$.
   - Proves budget compliance to auditors/employers without revealing merchant identities, account numbers, or exact spend balances.
8. **Dynamic 50/30/20 Personalized Budget Rebalancer & 3-Year Wealth Engine**:
   - Interactive income slider (₹20,000 to ₹3,00,000/month).
   - Real-time 50/30/20 rebalancing channeling detected leakage (₹14,850/mo) into compound savings.
   - Dynamic category-by-category daily spending limits (Grocery, Food & Dining, Utilities, Entertainment).
   - 3-Year compound wealth accumulation calculator at $8.0\%$ CAGR.
9. **Smart Subscription Creep Eliminator & Autopay Auditor**:
   - Dedicated subscription monitor tracking Netflix, Spotify, Gym, Utilities, and SaaS.
   - 28-day billing trap detector (identifying 13 billing cycles/year).
   - Annual leakage drag calculator with 1-click "Cancel Mandate" recommendations.
10. **Geographic Risk & Temporal Night-Surge Heatmap**:
    - State-by-state volume and fraud incidence matrix across 5 major regions (Maharashtra, UP, Karnataka, Tamil Nadu, Delhi).
    - Temporal night-surge index analyzing fraud concentration during late-night hours (12 AM - 4 AM).
11. **Interactive Natural Language AI Auditor ReAct Console**:
    - Browser-based ReAct agent terminal.
    - Demonstrates full multi-step agent trajectory: `Thought` $\rightarrow$ `Action (SqlQuery/Calculator/Auditor)` $\rightarrow$ `Observation` $\rightarrow$ `Final Answer`.
12. **Custom Statement Importer & Real-Time Parser**:
    - Drag-and-drop or file upload for custom user bank/UPI CSV & JSON statements.
    - Instant in-browser parsing, anomaly identification, and spending totals.
13. **Cryptographic Immutability Certificate Generator (JSON / Print)**:
    - Generates downloadable tamper-evident certificate (`CERT-AGX-2026-9F42B`) signed by 3 consensus nodes with Merkle Root and Block Header Hash.

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
