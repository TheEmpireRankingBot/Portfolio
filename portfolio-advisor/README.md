# 📈 Portfolio Advisor

A beginner-friendly trading-portfolio tracker that doesn't just show you numbers —
it **coaches** you. It tells you whether you're **investing with calculated risk
or drifting into gambling**, points out your portfolio's weaknesses in plain
English, surfaces recent good/bad news, and teaches you the concepts as you go.

> ⚠️ **Educational tool only — not financial advice.** It helps you understand
> your own portfolio and learn; it does not tell you what to buy or sell.

---

## What it does

| Feature | What you get |
|---|---|
| **📊 Dashboard** | Total value, cost basis, profit/loss, and allocation pies by holding and by sector. |
| **💼 My Holdings** | Add / edit / remove positions. Saved locally to `data/portfolio.json`. |
| **🎲 Risk & Discipline** | A **0–100 Discipline Score** — the core "gambling vs calculated risk" gauge — with every point deduction explained and a fix for each. |
| **🔍 Weaknesses** | A health-check (diversification, concentration, sector balance, volatility, stock-vs-fund mix) that teaches each concept. |
| **📰 News** | Recent headlines per holding, auto-tagged 🟢 good / 🔴 bad / ⚪ neutral. |
| **🧑‍🏫 AI Coach** | Optional natural-language coaching from Claude (falls back to a transparent rules summary with no API key). |
| **🎓 Learn** | Short lessons + a glossary of every term used in the app. |

## The Discipline Score (gambling vs calculated risk)

Every portfolio starts at **100**. Points come off for habits that turn investing
into gambling — and **every deduction is shown to you** with *why it matters* and
*what a disciplined investor does instead*:

- Betting too much on one position (concentration)
- Owning too few holdings (thin diversification)
- Piling into a single sector
- Chasing very high volatility / high-beta names
- Oversized speculative (e.g. crypto) allocations

| Score | Verdict |
|---|---|
| 80–100 | **Calculated risk-taker** — this is investing. |
| 60–79 | Mostly calculated, a few gaps. |
| 40–59 | Mixed, leaning risky. |
| 0–39 | **Leaning toward gambling** — fixable, fast. |

---

## Quick start (live data, on your own machine)

```bash
git clone <your-repo-url>
cd portfolio-advisor
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Then open the URL it prints (usually <http://localhost:8501>). On first run it
seeds an example portfolio — edit it on the **My Holdings** tab. Supported
tickers include US stocks (`AAPL`), ETFs (`VOO`), Singapore/SGX (`D05.SI`), and
crypto (`BTC-USD`).

### Optional: enable the AI Coach

```bash
cp .env.example .env
# edit .env and paste your Anthropic API key
```

Without a key the app still works fully — the AI Coach simply shows the
transparent rules-based summary instead.

### Demo / offline mode

If live market data can't be reached (no internet, or a sandbox with a network
allowlist), the app automatically switches to **Demo mode** with bundled sample
data so every page still works. A banner makes it clear when you're seeing
illustrative numbers.

---

## Project layout

```
app.py                 Streamlit UI (one function per tab)
advisor/
  data_fetch.py        yfinance live data + offline sample fallback
  metrics.py           returns, volatility, beta, drawdown, HHI, allocations
  risk_score.py        the 0-100 Discipline Score + explained red flags
  weaknesses.py        teaching health-check findings
  news.py              headlines + offline VADER sentiment tagging
  education.py         glossary (tooltips) + lessons
  ai_coach.py          optional Claude coaching, rules fallback
sample_data/           demo quotes & news for offline mode
tests/                 pytest unit tests (metrics + risk score)
```

## Running the tests

```bash
pip install pytest
pytest -q
```

## Tech

Python · Streamlit · yfinance · pandas/numpy · Plotly · vaderSentiment · Anthropic (optional)
