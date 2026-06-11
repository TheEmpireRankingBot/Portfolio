"""Unit tests for the terminal command parser (pure functions, no network)."""

from advisor.terminal import FRED_SERIES, Command, parse


def test_empty_input_is_none():
    assert parse("").kind == "none"
    assert parse("   ").kind == "none"


def test_help_variants():
    assert parse("help").kind == "help"
    assert parse("HELP").kind == "help"
    assert parse("?").kind == "help"


def test_bare_ticker_is_quote():
    cmd = parse("aapl")
    assert cmd == Command("quote", symbol="AAPL")


def test_chart_default_and_custom_days():
    assert parse("AAPL H") == Command("chart", symbol="AAPL", arg=60)
    assert parse("nvda h 120") == Command("chart", symbol="NVDA", arg=120)
    # days clamp to [10, 252]
    assert parse("AAPL H 5").arg == 10
    assert parse("AAPL H 9999").arg == 252


def test_news_and_fundamentals_functions():
    assert parse("TSLA N") == Command("news", symbol="TSLA")
    assert parse("TSLA news") == Command("news", symbol="TSLA")
    assert parse("voo f") == Command("fundamentals", symbol="VOO")


def test_crypto_and_suffixed_tickers_parse():
    assert parse("BTC").kind == "quote"
    assert parse("BTC-USD H").kind == "chart"
    assert parse("D05.SI").symbol == "D05.SI"


def test_macro_aliases_and_years():
    cmd = parse("MACRO CPI")
    assert cmd.kind == "macro" and cmd.symbol == "CPI" and cmd.arg == 10
    assert parse("fed unrate 5").arg == 5
    assert parse("ECON GDP 99").arg == 50  # clamps to 50 years
    assert parse("MACRO").kind == "error"  # series required


def test_market_news_and_port():
    assert parse("NEWS").kind == "market_news"
    assert parse("port").kind == "port"
    assert parse("PORTFOLIO").kind == "port"


def test_unknown_function_errors_helpfully():
    cmd = parse("AAPL X")
    assert cmd.kind == "error"
    assert "HELP" in cmd.error


def test_garbage_ticker_rejected():
    assert parse("@@@@").kind == "error"
    assert parse("WAYTOOLONGTICKER123").kind == "error"


def test_fred_catalog_integrity():
    for alias, (fred_id, title, transform) in FRED_SERIES.items():
        assert alias == alias.upper()
        assert fred_id and isinstance(fred_id, str)
        assert title
        assert transform in (None, "yoy12")
