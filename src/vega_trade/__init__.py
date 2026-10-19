"""Compatibility import for the VegaTrade SDK."""

from trading_infra_automation import (
    ClientConfig,
    DEFAULT_BASE_URL,
    DEFAULT_TIMEOUT,
    TradingInfraAutomationClient,
    VegaTradeClient,
)

__all__ = [
    "ClientConfig",
    "DEFAULT_BASE_URL",
    "DEFAULT_TIMEOUT",
    "VegaTradeClient",
    "TradingInfraAutomationClient",
]
__version__ = "0.1.0"
