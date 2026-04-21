# Moomoo API Skills Setup

## Skills Installed (Global)

Source: [MoomooOpen/moomoo-agent-hub](https://github.com/MoomooOpen/moomoo-agent-hub)

| Skill | Name | Description |
|-------|------|-------------|
| `install-opend` | OpenD Installation Assistant | Auto-downloads and installs moomoo/Futu OpenD and upgrades Python SDK. Supports Windows, macOS, Linux. |
| `moomooapi` | Market Data & Trading Assistant | Query quotes, K-lines, order book, options; place/cancel/modify orders; manage accounts and positions. |

Installed to: `~/.claude/skills/`

## Python SDK Installed

| Package | Version |
|---------|---------|
| moomoo-api | 10.3.6308 |
| backtrader | 1.9.78.123 |
| matplotlib | 3.10.8 |
| pandas | 3.0.2 |
| numpy | 2.4.4 |

## moomoo OpenD

moomoo OpenD is a desktop GUI application that must be installed on your **local machine**.

**Download:** https://www.moomoo.com/download/OpenAPI

**Setup steps:**
1. Download the GUI version for your OS (`moomoo_OpenD`, with underscore)
2. Install and launch it
3. Log in with your moomoo account
4. Confirm API port is `11111` (default)

**Invoke the install skill:** `/install-opend mm`

## Usage

Once OpenD is running, use `/moomooapi` in Claude Code to query market data or execute trades.

```python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
ret, data = quote_ctx.get_global_state()
if ret == RET_OK:
    print('Connected:', data)
quote_ctx.close()
```

**API Docs:** https://openapi.moomoo.com/moomoo-api-doc/en/intro/intro.html
