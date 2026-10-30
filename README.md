# Expense Auditor & Anomaly Hunter

[![AgentX 2026](https://img.shields.io/badge/AgentX-Challenge_2026-6366f1.svg)](https://github.com/nevathxavier-afk/demo)
[![Finance & Risk](https://img.shields.io/badge/Track-Finance_%26_Risk-10b981.svg)]()
[![Proof-of-Work Blockchain](https://img.shields.io/badge/Audit_Trail-PoW_Blockchain-f59e0b.svg)]()
[![Offline Tests](https://img.shields.io/badge/Tests-Passing_100%25-06b6d4.svg)]()
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nevathxavier-afk/expense-auditor-agentx/blob/main/notebooks/agentx_colab.ipynb)

**A UPI or bank statement in, a rebalanced budget plan out.**

Autonomous Finance & Risk agent built for the **AgentX Challenge 2026** (SRMIST Tiruchirappalli). Analyzes UPI and bank statements over 250,000 transactions, auto-categorizes purchases, hunts duplicate debits, detects creeping subscriptions, flags spend surges with cognitive reasoning, seals audit findings into an immutable **Proof-of-Work (PoW) Blockchain Ledger**, and outputs a personalized 50/30/20 rebalanced budget plan.

---

## Key Features

1. **Auto-Categorize Every Purchase**: Intelligently classifies raw UPI/merchant IDs into Needs, Wants, and Discretionary categories.
2. **Anomaly Hunter Engine**:
   - **Duplicate Detection**: Flags identical charges within sliding time windows (accidental double-clicks / gateway retries).
   - **Subscription Creep**: Uncovers silent recurring price hikes (>5% creep) in streaming, utilities, and telecom mandates.
   - **Spend Surges**: Employs rolling Z-scores ($Z \ge 2.2\sigma$) and volatility modeling to spot discretionary budget hemorrhages.
3. **Cognitive Explainability**: Every anomaly includes severity grading, leakage impact in INR, and actionable remediation reasoning.
4. **Simulated Proof-of-Work (PoW) Blockchain Ledger**:
   - Cryptographic **SHA-256 Merkle Tree** generation over all transaction batches and findings.
   - Computes verifiable **Proof-of-Work nonces** satisfying dynamic difficulty targets.
   - Issues tamper-evident, exportable **Audit Certificates** with 3/3 validator node consensus simulation.
   - Supports **Zero-Knowledge style verifiable expense commitments** so users can prove compliance without leaking raw PII.
5. **Personalized Dynamic Budget Rebalancer**:
   - Plugs detected leakage directly into high-yield savings and emergency reserves.
   - Generates category-level daily spending limits and 3-year wealth growth projections.

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
python main.py "Audit upi_transactions_2024.csv, find duplicate charges, and mine an audit block"

# 5. Run the machine-readable evaluation harness (Judges' contract)
python main.py --json "Which categories experienced the largest spend surge?"
```

Free keys: [Google AI Studio](https://aistudio.google.com/apikey) (Gemini) and [Groq Console](https://console.groq.com/keys).

---

## Layout

```
main.py                 entry point + the judges' contract (--json & --dry-run)
agent/core.py           the ReAct loop, step cap, repeat guard, error recovery
agent/llm.py            Gemini / Groq wrapper with 429 retry + DryRunLLM
agent/prompt_builder.py system prompt with Finance & Risk Auditor ROLE
agent/auditor.py        anomaly detection engine (duplicates, creep, surges, fraud)
agent/budget.py         50/30/20 dynamic personalized budget rebalancer
blockchain/ledger.py    tamper-evident audit blockchain & certificate issuer
blockchain/merkle.py    SHA-256 Merkle tree & inclusion proof verifier
blockchain/pow.py       Proof-of-Work consensus mining engine
blockchain/zk_proofs.py zero-knowledge style verifiable expense proofs
tools/                  registry (__init__.py), data_query, calculator, web_search,
                        auditor_tool, blockchain_tool, budget_tool
config/__init__.py      models, MAX_ITERATIONS, data folder, PoW difficulty
data/                   UPI transactions dataset (250,000 rows) + sample files
tests/test_agent.py     offline unit tests: python -m unittest discover tests
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
  ```

---

## Simulated Proof-of-Work Audit Flow

```
[ UPI Statement In ]
         │
         ▼
[ Expense Auditor & Anomaly Hunter ]
         │ (Auto-categorize, find duplicates, creep, surges)
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
