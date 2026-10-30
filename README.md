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
6. **Cryptographic Avalanche Tamperproof Testing Arena & Cascading Domino Simulator**:
   - **Strict Avalanche Criterion (SAC) Analysis**: Proves that modifying 1 bit or 1 paisa (₹0.01) triggers a catastrophic **~50% bit flip (Hamming distance ~128/256 bits)** across the SHA-256 block header.
   - **Interactive 256-Bit Binary Diffusion Matrix**: Visualizes all 256 SHA-256 bits in real time, highlighting flipped bits in red and matching bits in green.
   - **Cascading Blockchain Invalidation Domino Effect**: Shows how tampering with a single leaf invalidates the Merkle Root, breaks the PoW nonce (target `000...`), breaks the `prev_hash` link of Block #2, and orphans the entire downstream ledger.
   - **3-Node Byzantine Consensus Telemetry**: Real-time streaming logs from **Node Alpha (AML/Fraud)**, **Node Beta (Merkle Cryptographer)**, and **Node Gamma (PoW Consensus)**, with 1-click **Cryptographic Self-Healing**.
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

## Local & Cloud Setup

You can clone the repository to your laptop, or run directly in Google Colab without downloading anything:

```bash
# 1. Clone the repository
git clone https://github.com/nevathxavier-afk/expense-auditor-agentx.git
cd expense-auditor-agentx

# 2. Set up virtual environment
python3 -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate

# 3. Install requirements
pip install -r requirements.txt

# 4. Initialize environment configuration
cp .env.example .env

# 5. Prove your setup works (no API key needed)
python main.py --dry-run "test"
```

Configure the `.env` file with free API credentials. We recommend Google AI Studio Gemini (`GEMINI_API_KEY`) or Groq Cloud (`GROQ_API_KEY`) for free, instant setup without credit cards.

---

## Template File Structure

The repository layout is organized logically to separate the agent reasoning logic from tools and environments:

```
expense-auditor-agentx/
├── agent/
│   ├── core.py           # ReAct loop, step cap, repeat guard, error recovery
│   ├── llm.py            # Gemini / Groq wrapper with 429 retry + DryRunLLM
│   ├── prompt_builder.py # System prompt: set your theme's ROLE here
│   ├── auditor.py        # Anomaly hunter (duplicates, creep, surges, fraud)
│   ├── similarity.py     # Transaction similarity, 0x TxHashes, VPAs
│   └── budget.py         # 50/30/20 dynamic personalized budget rebalancer
├── tools/
│   ├── __init__.py       # Tool base class + registry (add your tools here)
│   ├── calculator.py     # Safe arithmetic
│   ├── data_query.py     # list_files, read_file, sql_query over CSVs
│   ├── web_search.py     # DuckDuckGo search
│   ├── auditor_tool.py   # Autonomous transaction auditor
│   ├── blockchain_tool.py# PoW mining & ledger validator
│   └── budget_tool.py    # 50/30/20 rebalancer tool
├── blockchain/
│   ├── ledger.py         # Tamper-evident blockchain & digital certificate issuer
│   ├── merkle.py         # SHA-256 Merkle tree & inclusion proof verifier
│   ├── pow.py            # Proof-of-Work mining engine
│   ├── zk_proofs.py      # Salted zero-knowledge expense commitments
│   └── tamper_test.py    # Avalanche & cascading domino tamper simulator
├── config/__init__.py    # Models, MAX_ITERATIONS, AGENTX_DATA_DIR, PoW difficulty
├── data/                 # 250,000 UPI dataset + samples + audit_ledger.json
├── tests/test_agent.py   # Offline unit tests (11 tests, 100% pass, no API key needed)
├── notebooks/agentx_colab.ipynb # 1-click Google Colab execution
├── main.py               # Entry point + judging contract (--json & --dry-run)
├── serve.py              # Cyber-FinTech dashboard & REST API server
├── api/index.py          # Vercel serverless function
├── vercel.json           # Vercel deployment configuration
├── PITCH_DECK.md         # 14-slide presentation deck & judges script
├── .env.example          # GEMINI_API_KEY / GROQ_API_KEY template
├── requirements.txt
└── README.md
```

---

## Starter Agent Skeleton

Here is the core of the agent loop in `agent/core.py`:

```python
def run(self, query, verbose=False):
    messages = [{"role": "user", "content": query}]
    trace, seen = [], {}
    for step in range(self.max_iterations):  # hard step cap
        reply = self.llm.generate(self.system, messages)
        data = parse_json(reply)
        if "final_answer" in data:  # Decision: done
            return data["final_answer"], trace
        name, args = data["action"], data.get("args", {})
        observation = self._call_tool(name, args)  # Action -> Observation
        trace.append({"thought": data.get("thought"), "tool": name, "args": args, "observation": observation})
        messages += [
            {"role": "assistant", "content": json.dumps(data)},
            {"role": "user", "content": f"OBSERVATION: {observation}"}
        ]
    return self._wrap_up(messages), trace
```

Add a tool by subclassing `Tool` in `tools/` and registering it in `build_tools()`.

---

## The Judges' Contract (`--json`)

Judges evaluate the agent using the machine flag `--json`:
- **Stdout**: Exactly ONE line of valid JSON:
  ```json
  {"answer": "...", "trace": [{"thought": "...", "tool": "...", "args": {...}, "observation": "..."}]}
  ```
- **Stderr**: Diagnostic logs and step traces (clean separation).
- **Data Source**: Automatically reads from the `AGENTX_DATA_DIR` environment variable, falling back to local `data/`.
- See the official [Backend Contract](https://hackthonagentx.netlify.app/docs#contract).

### Offline Test Suite:
```bash
python -m unittest discover tests
# Ran 11 tests in 0.151s -> OK (100% Pass)
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
