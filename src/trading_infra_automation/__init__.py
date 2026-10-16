"""Public package interface for the VegaTrade infrastructure SDK."""

from .client import TradingInfraAutomationClient, VegaTradeClient

__all__ = ["VegaTradeClient", "TradingInfraAutomationClient"]
__version__ = "0.1.0"
SUPPORTED_PYTHON_VERSIONS = (3, 9, 10, 11, 12, 13)
