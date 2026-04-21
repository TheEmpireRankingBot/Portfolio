# Moomoo OpenAPI — Quick Start

A minimal scaffold for building against the [moomoo OpenAPI](https://openapi.moomoo.com/moomoo-api-doc/en/).

The moomoo API is a two-piece setup:

1. **OpenD** — a gateway program that runs on your machine (or cloud server) and relays requests to moomoo's servers.
2. **moomoo-api SDK** — the Python client that talks to your local OpenD over TCP.

Your script → (localhost:11111) → OpenD → moomoo servers.

---

## 1. Install and run OpenD

OpenD is a desktop/server binary — install it on the machine where you'll run your scripts. It cannot be `pip install`ed.

1. Download OpenD from the [official download page](https://openapi.moomoo.com/moomoo-api-doc/en/).
2. Install:
   - **Visualization OpenD** (GUI, recommended for first-time setup) — just run the installer.
   - **Command Line OpenD** — unzip and run the executable.
3. Launch OpenD and log in with your moomoo account.
4. Leave it running. It listens on `127.0.0.1:11111` by default.

More detail: [Visualization OpenD](https://openapi.moomoo.com/moomoo-api-doc/en/quick/opend-base.html) · [Command Line OpenD](https://openapi.moomoo.com/moomoo-api-doc/en/opend/opend-cmd.html).

## 2. Install the Python SDK

Requires Python 3.6+.

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 3. Run the sample

With OpenD running and logged in:

```bash
python quickstart.py
```

Expected output: a market snapshot row for `HK.00700` (Tencent).

### Overriding host/port

```bash
MOOMOO_OPEND_HOST=127.0.0.1 MOOMOO_OPEND_PORT=11111 python quickstart.py
```

---

## Troubleshooting

- **`ConnectionRefusedError` / hangs on connect** — OpenD isn't running, or it's on a different port. Check the OpenD window/log.
- **`Not login`** — log in inside the OpenD GUI (or via the CLI login flow) before calling the API.
- **No market data permission** — market-data subscriptions are tied to your moomoo account; some endpoints require a paid tier.

## Layout

```
.
├── quickstart.py       # Minimal OpenQuoteContext demo
├── requirements.txt    # moomoo-api
├── .gitignore
└── README.md
```

## References

- [moomoo OpenAPI docs](https://openapi.moomoo.com/moomoo-api-doc/en/)
- [moomoo-api on PyPI](https://pypi.org/project/moomoo-api/)
- [Program Samples](https://openapi.moomoo.com/moomoo-api-doc/en/quick/demo.html)
- [OpenD Overview](https://openapi.moomoo.com/moomoo-api-doc/en/opend/opend-intro.html)
