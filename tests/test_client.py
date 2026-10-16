from __future__ import annotations

from pytest import MonkeyPatch

from trading_infra_automation import TradingInfraAutomationClient, VegaTradeClient
from trading_infra_automation.config import ClientConfig


def test_client_config_defaults() -> None:
    config = ClientConfig(api_key="abc")
    assert config.api_key == "abc"
    assert config.base_url == "https://api.vegatrade.example.com"
    assert config.headers["Authorization"] == "******"


def test_vega_trade_client_uses_base_url_and_headers() -> None:
    client = VegaTradeClient(api_key="secret-key", base_url="https://api.example.com")
    assert client.base_url == "https://api.example.com"
    assert client.config.headers["Authorization"] == "******"


def test_package_exports() -> None:
    assert hasattr(VegaTradeClient, "ping")
    assert hasattr(VegaTradeClient, "create_order")


def test_compat_alias() -> None:
    assert TradingInfraAutomationClient is not None


def test_client_config_invalid_timeout_falls_back_to_default(monkeypatch: MonkeyPatch):
    monkeypatch.setenv("VEGATRADE_TIMEOUT", "not-a-number")
    config = ClientConfig.from_env(api_key="abc")
    assert config.timeout == 10.0


def test_client_request_encodes_query_params(monkeypatch: MonkeyPatch):
    class FakeResponse:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def read(self):
            return b'{"ok": true}'

    monkeypatch.setattr("trading_infra_automation.client.request.urlopen", lambda req, timeout=None: FakeResponse())
    client = VegaTradeClient(api_key="secret-key", base_url="https://api.example.com")
    result = client.list_orders(symbol="BTC/USD", status="open")
    assert result == {"ok": True}
