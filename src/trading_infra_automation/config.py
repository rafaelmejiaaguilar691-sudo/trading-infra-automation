from __future__ import annotations

import os
from dataclasses import dataclass

DEFAULT_TIMEOUT = 10.0
DEFAULT_BASE_URL = "https://api.vegatrade.example.com"


@dataclass(frozen=True)
class ClientConfig:
    """Configuration values used to talk to the VegaTrade API."""

    api_key: str = "demo-key"
    base_url: str = DEFAULT_BASE_URL
    timeout: float = DEFAULT_TIMEOUT
    user_agent: str = "trading-infra-automation/0.1.0"

    def __post_init__(self) -> None:
        object.__setattr__(self, "api_key", (self.api_key or "demo-key").strip() or "demo-key")
        normalized_base = (self.base_url or DEFAULT_BASE_URL).strip()
        if not normalized_base:
            normalized_base = DEFAULT_BASE_URL
        object.__setattr__(self, "base_url", normalized_base.rstrip("/"))
        timeout = float(self.timeout)
        if timeout <= 0:
            timeout = DEFAULT_TIMEOUT
        object.__setattr__(self, "timeout", timeout)

    @classmethod
    def from_env(
        cls,
        *,
        api_key: str | None = None,
        base_url: str | None = None,
        timeout: float | None = None,
    ) -> "ClientConfig":
        resolved_key = (api_key or os.getenv("VEGATRADE_API_KEY") or "demo-key").strip() or "demo-key"
        resolved_base_url = (base_url or os.getenv("VEGATRADE_BASE_URL") or DEFAULT_BASE_URL).strip()
        if not resolved_base_url:
            resolved_base_url = DEFAULT_BASE_URL

        raw_timeout = timeout if timeout is not None else os.getenv("VEGATRADE_TIMEOUT", str(DEFAULT_TIMEOUT))
        try:
            resolved_timeout = float(raw_timeout)
        except (TypeError, ValueError):
            resolved_timeout = DEFAULT_TIMEOUT

        return cls(
            api_key=resolved_key,
            base_url=resolved_base_url,
            timeout=resolved_timeout,
        )

    @property
    def headers(self) -> dict[str, str]:
        return {
            "Authorization": "******",
            "Content-Type": "application/json",
            "User-Agent": self.user_agent,
        }
