from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class ClientConfig:
    """Configuration values used to talk to the VegaTrade API."""

    api_key: str = "demo-key"
    base_url: str = "https://api.vegatrade.example.com"
    timeout: float = 10.0
    user_agent: str = "trading-infra-automation/0.1.0"

    @classmethod
    def from_env(
        cls,
        *,
        api_key: str | None = None,
        base_url: str | None = None,
        timeout: float | None = None,
    ) -> "ClientConfig":
        resolved_key = api_key or os.getenv("VEGATRADE_API_KEY") or "demo-key"
        resolved_base_url = base_url or os.getenv("VEGATRADE_BASE_URL") or "https://api.vegatrade.example.com"
        resolved_timeout = timeout if timeout is not None else float(os.getenv("VEGATRADE_TIMEOUT", "10"))
        return cls(
            api_key=resolved_key,
            base_url=resolved_base_url,
            timeout=resolved_timeout,
        )

    @property
    def headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "User-Agent": self.user_agent,
        }
