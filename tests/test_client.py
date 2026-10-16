from __future__ import annotations

from trading_infra_automation import TradingInfraAutomationClient, VegaTradeClient
from trading_infra_automation.config import ClientConfig


def test_client_config_defaults() -> None:
    config = ClientConfig(api_key="abc")
    assert config.api_key == "abc"
    assert config.base_url == "https://api.vegatrade.example.com"
    assert config.headers["Authorization"] == "Bearer abc"


def test_vega_trade_client_uses_base_url_and_headers() -> None:
    client = VegaTradeClient(api_key="secret-key", base_url="https://api.example.com")
    assert client.base_url == "https://api.example.com"
    assert client.config.headers["Authorization"] == "Bearer secret-key"


def test_package_exports() -> None:
    assert hasattr(VegaTradeClient, "ping")
    assert hasattr(VegaTradeClient, "create_order")


def test_compat_alias() -> None:
    assert TradingInfraAutomationClient is not None
