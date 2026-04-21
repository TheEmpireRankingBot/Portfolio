# Moomoo API Skills Setup

Source: [MoomooOpen/moomoo-agent-hub](https://github.com/MoomooOpen/moomoo-agent-hub)

## Skills Installed (Global `~/.claude/skills/`)

| Skill | Description | Status |
|-------|-------------|--------|
| `install-opend` | OpenD Installation Assistant — auto-downloads and installs moomoo OpenD + Python SDK. Supports Windows, macOS, Ubuntu, CentOS. | ✅ Installed |
| `moomooapi` | Market Data & Trading Assistant — quotes, K-lines, order book, options chain, place/cancel/modify orders, account & positions. Includes 57 Python scripts. | ✅ Installed |

> **Note:** Content Skills (News Search, Stock Briefing, Sentiment Gauge) referenced in the README at `anthropics/futu-agent-hub` are not yet publicly available (repo returns 404 as of April 2026).

## Python Packages Installed

| Package | Version | Purpose |
|---------|---------|---------|
| moomoo-api | 10.3.6308 | Moomoo OpenAPI Python SDK |
| backtrader | 1.9.78.123 | Strategy backtesting framework |
| matplotlib | 3.10.8 | Chart plotting |
| pandas | 3.0.2 | Data analysis |
| numpy | 2.4.4 | Numerical computation |

## moomoo OpenD (Manual Step Required)

moomoo OpenD is a desktop GUI application — it must be installed on your **local machine**, not this server.

**Download:** https://www.moomoo.com/download/OpenAPI

**Steps:**
1. Download the GUI version for your OS (`moomoo_OpenD`, with underscore — not `moomooOpenD`)
2. Install and launch it
3. Log in with your moomoo account (complete questionnaire assessment on first login)
4. Confirm API port is `11111` and listen address is `127.0.0.1`

**Or let the skill handle it** — run `/install-opend mm` in Claude Code to auto-install.

## Usage

Once OpenD is running locally:

```python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
ret, data = quote_ctx.get_global_state()
if ret == RET_OK:
    print('Connected:', data)
quote_ctx.close()
```

Use `/moomooapi` in Claude Code to query market data or execute trades in natural language.

**API Docs:** https://openapi.moomoo.com/moomoo-api-doc/en/intro/intro.html
**Permission Guide:** https://openapi.futunn.com/futu-api-doc/intro/authority.html
