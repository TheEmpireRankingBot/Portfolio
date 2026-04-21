"""Minimal moomoo OpenAPI quick-start.

Prereqs:
  1. moomoo OpenD is running locally (default 127.0.0.1:11111) and logged in.
  2. `pip install -r requirements.txt`

Run:
  python quickstart.py
"""

import os

from moomoo import OpenQuoteContext, RET_OK


OPEND_HOST = os.environ.get("MOOMOO_OPEND_HOST", "127.0.0.1")
OPEND_PORT = int(os.environ.get("MOOMOO_OPEND_PORT", "11111"))


def main() -> int:
    quote_ctx = OpenQuoteContext(host=OPEND_HOST, port=OPEND_PORT)
    try:
        ret, data = quote_ctx.get_market_snapshot(["HK.00700"])
        if ret != RET_OK:
            print(f"get_market_snapshot failed: {data}")
            return 1
        print(data)
        return 0
    finally:
        quote_ctx.close()


if __name__ == "__main__":
    raise SystemExit(main())
