"""Public package interface for the VegaTrade infrastructure SDK."""

from .client import TradingInfraAutomationClient, VegaTradeClient
from .config import ClientConfig, DEFAULT_BASE_URL, DEFAULT_TIMEOUT

__all__ = [
    "ClientConfig",
    "DEFAULT_BASE_URL",
    "DEFAULT_TIMEOUT",
    "VegaTradeClient",
    "TradingInfraAutomationClient",
]
__version__ = "0.1.0"
SUPPORTED_PYTHON_VERSIONS = (3, 9, 10, 11, 12, 13, 14)
