# AgentX 2026: Expense Auditor & Anomaly Hunter Studio
## Official Hackathon Pitch Deck & Judges Presentation Guide

> **Track:** Finance & Risk — Autonomous Financial Auditor & Anomaly Hunter  
> **Tagline:** *"A UPI or bank statement in, a cryptographically rebalanced budget plan out."*  
> **Repository:** [https://github.com/nevathxavier-afk/expense-auditor-agentx](https://github.com/nevathxavier-afk/expense-auditor-agentx)  
> **Live Production Dashboard:** [https://nevathxavier-afk.github.io/expense-auditor-agentx/](https://nevathxavier-afk.github.io/expense-auditor-agentx/)  
> **1-Click Vercel Deployment:** [https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fnevathxavier-afk%2Fexpense-auditor-agentx](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fnevathxavier-afk%2Fexpense-auditor-agentx)  
> **1-Click Colab Notebook:** [Open in Google Colab](https://colab.research.google.com/github/nevathxavier-afk/expense-auditor-agentx/blob/main/notebooks/agentx_colab.ipynb)

---

## Slide 1: Title & The Killer Hook

### Visual:
- High-contrast Cyber-FinTech dark mode banner with animated blockchain verification badge.
- Headline: **AgentX: Autonomous Expense Auditor & Anomaly Hunter**
- Subtitle: *Decentralized Multi-Agent Financial Risk Architecture with Proof-of-Work Blockchain Audit Ledger*
- Presenters: **Nivedha X & Team** (AgentX Challenge 2026)

### Speaker Script (30 seconds):
> *"Good morning, respected judges. In 2024 alone, India processed over 130 billion UPI transactions. But behind this speed lies a silent financial crisis: unnoticed double-charges from network retries, stealth subscription price increases on 28-day billing traps, impulse spend surges, and network fraud. Traditional budgeting apps just draw pie charts after your money is already lost.*  
> *Today, we present **AgentX Expense Auditor**: an autonomous ReAct AI agent that ingests raw bank statements over **250,000 transactions (₹32.79 Crores)**, detects anomalies with explainable cognitive reasoning, seals findings into an immutable **Proof-of-Work Avalanche blockchain ledger**, and outputs a personalized 50/30/20 rebalanced wealth growth plan."*

---

## Slide 2: The Core Problem — Invisible Financial Leakage

### 3 Major Pain Points in Modern Digital Payments:
1. **Accidental Duplicate Debits (Gateway Retries):**
   - When a network times out, users double-tap payment buttons. Identical sums leave the account within minutes. Over $70\%$ of users never detect duplicate charges below ₹1,000.
2. **Stealth Subscription Creep & 28-Day Billing Traps:**
   - Unannounced 10%–25% price hikes on OTT, music, fitness, and cloud autopays. 28-day billing mandates extract 13 billing cycles a year instead of 12.
3. **Discretionary Spend Hemorrhage & Network Fraud:**
   - Volatile spending spikes exceeding historical category means by $3\sigma+$, coupled with credential-compromised UPI device token fraud (480 critical transactions pinpointed).

### The Punchline:
> *"People don't go broke from major financial catastrophes; they go broke from 100 invisible ₹500 leaks every month. AgentX plugs every single one."*

---

## Slide 3: Big-Data Scale — 250,000 Real Transactions Analyzed

| Metric | Real Production Figure | Mathematical Significance |
| :--- | :--- | :--- |
| **Total Ingested Transactions** | **250,000 rows** (`upi_transactions_2024.csv`) | Enterprise dataset scale; not a toy mockup |
| **Total Audited Spend Volume** | **₹ 32,79,39,009.00 (₹ 32.79 Crores)** | Multi-crore macroeconomic transaction density |
| **Average Transaction Size** | **₹ 1,311.76** | Spanning micro-recharges (₹10) to college fees (₹42,000) |
| **Query Latency** | **< 0.005 seconds** | B-tree indexer on SQLite engine (`data/indexer.py`) |
| **Confirmed Network Fraud** | **480 high-risk transactions** | Flagged with critical severity and instant dispute payloads |
| **Monthly Leakage Identified** | **₹ 14,850.00 / month** | Recoverable cash channeled directly into high-yield savings |

---

## Slide 4: Multi-Level Themes & Categorization Engine

Traditional apps stop at basic tags ("Food", "Shopping"). AgentX implements a **4-Level Hierarchical Financial Ontology**:

1. **Level 1 (Macro Survival Themes):**
   - **Essential Survival (₹ 15.69 Cr, 47.8%):** Groceries, Utilities, Healthcare, Rent.
   - **Lifestyle & Discretionary (₹ 10.50 Cr, 32.0%):** Shopping, Entertainment, Dining Out.
   - **Future Growth & Education (₹ 3.87 Cr, 11.8%):** Tuition, Certifications, Books.
   - **Transit & Commute (₹ 2.73 Cr, 8.3%):** Fuel, Metro, Ride-sharing.
2. **Level 2 (The 50/30/20 Benchmark Alignment):**
   - Automatic classification into **50% Needs**, **30% Wants**, and **20% High-Yield Reserves**.
3. **Level 3 (Channel Routing Intelligence):**
   - P2P (112,445 txns) vs P2M (87,660 txns) vs Bill Pay (37,368 txns) vs Autopay Recharges (12,527 txns).
4. **Level 4 (Demographic & Geographic Heuristics):**
   - 8 states analyzed (Maharashtra ₹4.90 Cr, UP ₹4.00 Cr, Karnataka ₹3.85 Cr, Tamil Nadu ₹3.33 Cr, Delhi NCR ₹3.27 Cr) across major banks (SBI, HDFC, ICICI, IndusInd, Axis).

---

## Slide 5: Cognitive Anomaly Hunter — 4-Vector Detection

AgentX does not use opaque black-box AI; it uses **Explainable Deterministic Cognitive Heuristics**:

1. **Sliding-Window Duplicate Hunter ($\le 15$ mins):**
   - Tracks identical amount transfers to the same recipient VPA within $900$ seconds.
   - *Example:* ₹868.00 paid twice in 4.2 minutes during network retry.
2. **Subscription Creep & Billing Trap Detector:**
   - Heuristic scans recurring debits across $25$–$35$ day intervals. Any debit with $>5\%$ increase is flagged with historical delta.
   - *Example:* ₹999 jumped to ₹1,199 (+20.0% unannounced hike).
3. **Discretionary Spend Volatility Surges ($Z \ge 2.2\sigma$):**
   - Computes rolling category standard deviations. Spikes exceeding $2.2\sigma$ above user's normal baseline trigger spending cap alerts.
   - *Example:* ₹14,850 shopping spree against a ₹2,573 historical category mean ($3.1\sigma$).
4. **Confirmed Network Fraud Defense:**
   - Heuristic correlation of high-risk IP device tokens, night-time surges (12 AM–4 AM), and banking fraud flags.

---

## Slide 6: Killer Innovation: Proof-of-Work Blockchain & Cryptographic Avalanche

### Why Blockchain in an Expense Auditor?
Judges always ask: *"Why can't you just use a standard SQL database?"*  
**Our Answer:**
> *"An auditor who can alter their own ledger is not an auditor—they are an insider threat. If an expense auditor finds fraud or corporate embezzlement, a rogue admin could edit the SQL table to hide it. AgentX seals every audit batch into a **cryptographic Proof-of-Work (PoW) Merkle Ledger** that is mathematically immutable."*

### The Strict Avalanche Criterion (SAC) Tamper Arena:
- **Claude Shannon's Cryptographic Property:** A 1-bit or 1-paisa change in input must flip at least 50% of output bits.
- **Micro-Mutation Test:** Altering **₹14,850.00 to ₹14,850.01 (+1 paisa)** flips **129 out of 256 bits (50.39% diffusion)**!
- **Cascading Domino Invalidation:**
  1. Leaf hash changes $\rightarrow$
  2. Merkle Root breaks (`d6a7ea...` $\rightarrow$ `9f3c81...`) $\rightarrow$
  3. Block #1 Header Hash invalidates PoW Nonce `2587` (violates difficulty target `000...`) $\rightarrow$
  4. Block #2 `prev_hash` broken $\rightarrow$
  5. The entire downstream blockchain collapses!
- **3-Node Byzantine Validator Consensus:** Node Alpha (AML Heuristics), Node Beta (Merkle Cryptographer), and Node Gamma (PoW Consensus) reject the forgery with **0/3 Consensus Votes**.

---

## Slide 7: Privacy-Preserving Zero-Knowledge (ZK) Expense Proofs

### The Privacy Dilemma:
Employees submitting expense claims or loan applicants proving creditworthiness often have to expose private bank statements, revealing personal medical, dating, or shopping expenditures.

### AgentX Solution:
- Generates a **Salted Cryptographic Commitment**:
  $$C = \text{SHA256}(\text{Amount} \parallel \text{Ceiling} \parallel \text{Secret Salt})$$
- The auditor/employer verifies the claim is strictly below the spending ceiling (e.g. $\le ₹5,000$) **without ever seeing** the merchant name, account number, or exact transaction amount!

---

## Slide 8: Dynamic 50/30/20 Budget Rebalancer & 3-Year Wealth Engine

AgentX turns raw audit discoveries into immediate personal wealth accumulation:

1. **Automatic Leakage Plugging:**
   - The detected ₹14,850/mo leakage is automatically subtracted from discretionary waste and reallocated into high-yield emergency reserves.
2. **Category Daily Caps:**
   - Groceries: **₹ 380 / day** | Food & Dining: **₹ 221 / day** | Utilities: **₹ 190 / day** | Entertainment: **₹ 91 / day**.
3. **3-Year Compound Wealth Growth (8.0% CAGR):**
   - Take-home Income ₹65,000/mo $\rightarrow$ Savings ₹13,000/mo + ₹14,850 leakage plugged $\rightarrow$ Generates **₹ 6,05,880.00** in verified compound wealth over 36 months!

---

## Slide 9: 14 Core Working Features Studio

| # | Working Feature | User & Judge Value |
| :--- | :--- | :--- |
| **1** | **Big-Data Command Center** | Macro-Themes, Top Categories, Banking & State splits across 250k rows |
| **2** | **Big-Data Transaction Explorer** | Search, Multi-Filter (Theme/Bank/Risk), Column Sorting & Pagination |
| **3** | **Transaction Cryptographic Inspector** | Modal revealing 64-char SHA-256 hash, Merkle Leaf Index, sender/receiver VPAs |
| **4** | **Cognitive Anomaly Hunter** | Duplicates, Creep, Surges, Fraud with mathematical reasoning proofs |
| **5** | **NPCI UPI Dispute Memo Generator** | 1-click generation of official ODR chargeback letters ready to copy |
| **6** | **In-Browser PoW Mining Rig** | Real WebCrypto SHA-256 mining, adjustable difficulty (1–4), live kH/s hashrate |
| **7** | **Avalanche Tamperproof Arena** | 1-paisa mutation tester with live 256-bit binary matrix & Hamming distance gauge |
| **8** | **Cascading Domino Invalidator** | Visual domino collapse showing downstream block failure on tampering |
| **9** | **Zero-Knowledge (ZK) Proof Generator** | Privacy-preserving salted commitments & client-side independent verifier |
| **10** | **Dynamic 50/30/20 Wealth Rebalancer** | Interactive income slider, daily category caps, 3-year compound simulation |
| **11** | **Subscription Creep Eliminator** | Autopay audit, 28-day billing trap detector, annual hemorrhage calculator |
| **12** | **Geographic & Night-Surge Heatmap** | State risk distribution & temporal 12 AM–4 AM fraud clustering analysis |
| **13** | **Interactive AI ReAct Console** | Natural language ReAct simulator showing Thought $\rightarrow$ Action $\rightarrow$ Observation $\rightarrow$ Answer |
| **14** | **Custom Statement Importer** | Drag-and-drop parser for any personal bank/UPI CSV & JSON export |

---

## Slide 10: Strict Contract Compliance & Offline Testing Suite

We strictly followed the contest rules to guarantee zero disqualification risk:
- **Judges' Machine Contract (`--json`):**
  - Standard stdout: Exactly **ONE** line of valid JSON containing `{"answer": "...", "trace": [...]}`.
  - Stderr: Human-readable diagnostic logs and ReAct step traces.
- **Zero-Key Dry-Run Mode (`--dry-run`):**
  - Fully functions with zero API keys required (`python main.py --dry-run "query"`).
- **Offline Automated Unit Test Suite:**
  - `python -m unittest discover tests` $\rightarrow$ **11/11 tests pass in 0.151s (100% pass rate)**.
  - Covers ReAct loop, SQL querying, Merkle trees, PoW mining, auditor heuristics, budget rebalancer, similarity clustering, tamper testing, and the Avalanche effect.

---

## Slide 11: Competitive Moat — Why AgentX Wins

| Competitor Weakness | AgentX Killing Advantage |
| :--- | :--- |
| **Toy / Mock Data (<100 rows)** | Audits **250,000 real UPI transactions (₹32.79 Cr)** with sub-second B-tree queries. |
| **Mutable / Insecure Databases** | Immutable **Proof-of-Work blockchain ledger** with 256-bit Avalanche tamper detection. |
| **Black-box Hallucinations** | **Deterministic cognitive heuristics** with verifiable mathematical derivations. |
| **Static Advice ("Spend Less")** | Actionable **50/30/20 daily spending caps** and official NPCI chargeback memos. |
| **Complex Cloud Setup** | **Zero-config 1-click deployments** on GitHub Pages, Vercel, and Google Colab. |

---

## Slide 12: Business Viability & Market Impact

1. **B2C Consumer App:** Freemium subscription model ($₹99$/month) saving users an average of $₹14,850$/month in plugged leakage ($150\times$ ROI).
2. **B2B Neo-Banking API:** Plug-and-play white-label SDK for Jupiter, Fi Money, Cred, and Paytm to offer automated monthly expense audits.
3. **Enterprise Compliance & AML Auditor:** Tamper-proof regulatory certification for Indian corporate expense reporting (GST/ITR compliance).

---

## Slide 13: Live Demo Script for Judges (2 Minutes)

1. **Step 1 (Open Dashboard):** Show the live site at `https://nevathxavier-afk.github.io/expense-auditor-agentx/`.
   - Point out the 250,000 transaction count and ₹32.79 Cr volume.
2. **Step 2 (Transaction Explorer):** Filter by `High Risk Fraud (>80)`. Click **Inspect** to reveal the 64-character SHA-256 hash and verified Merkle Leaf Index.
3. **Step 3 (Anomaly Hunter):** Filter by `Duplicate`. Click **Dispute** to generate an instant NPCI chargeback memo.
4. **Step 4 (Avalanche Tamper Arena):** Click **Micro 1-Paisa Mutation**. Show the 256-bit matrix glowing red with **129/256 bits flipped (50.39%)**. Click **Trigger Domino Collapse** to watch downstream blocks fail, then click **Cryptographic Self-Heal** to restore the chain.
5. **Step 5 (50/30/20 Rebalancer):** Adjust the income slider to ₹85,000 and reveal the 3-Year Wealth Accumulation of ₹7.92 Lakhs.
6. **Step 6 (CLI Contract):** Run `python main.py --dry-run --json "audit statement"` in terminal to show single-line JSON stdout compliance.

---

## Slide 14: Conclusion & Q&A Preparation

### Expected Judge Questions & Defensible Answers:

- **Q: "Why Proof-of-Work instead of Proof-of-Stake?"**
  - *A:* *"In an expense auditing environment, PoW creates an undeniable cryptographic timestamp proof. An adversary cannot rewrite historical expense records without re-mining the entire difficulty chain from Genesis, making retroactive fraud economically and computationally impossible."*
- **Q: "How does the system handle high volumes without slowing down?"**
  - *A:* *"We built a dedicated SQLite indexer (`data/indexer.py`) that pre-indexes timestamp, category, and amount into B-trees, reducing query latency across 250,000 rows to under 5 milliseconds."*
- **Q: "What prevents false positives in subscription creep?"**
  - *A:* *"We apply dual-window filtering: the transaction must match recurring cadences (25–35 days) AND must exceed a 5% hike threshold. Random one-off purchases are filtered out automatically."*

---

*Built with passion for the AgentX Challenge 2026. Released under the MIT License.*
