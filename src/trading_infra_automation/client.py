from __future__ import annotations

import json
from typing import Any, Optional
from urllib import error, parse, request

from .config import ClientConfig


class VegaTradeClient:
    """Small, dependency-free client for VegaTrade REST endpoints."""

    def __init__(self, api_key: Optional[str] = None, *, base_url: Optional[str] = None, timeout: Optional[float] = None):
        self.config = ClientConfig.from_env(api_key=api_key, base_url=base_url, timeout=timeout)

    @property
    def base_url(self) -> str:
        return self.config.base_url.rstrip("/")

    def ping(self) -> dict[str, Any]:
        return self._request("GET", "/health")

    def get_account(self, account_id: Optional[str] = None) -> dict[str, Any]:
        path = "/account" if account_id is None else f"/account/{account_id}"
        return self._request("GET", path)

    def list_orders(self, **filters: Any) -> list[dict[str, Any]]:
        params = {key: value for key, value in filters.items() if value is not None}
        return self._request("GET", "/orders", params=params)

    def create_order(
        self,
        *,
        symbol: str,
        side: str,
        quantity: float,
        price: Optional[float] = None,
        order_type: str = "market",
    ) -> dict[str, Any]:
        payload = {
            "symbol": symbol,
            "side": side,
            "quantity": quantity,
            "type": order_type,
        }
        if price is not None:
            payload["price"] = price
        return self._request("POST", "/orders", payload=payload)

    def _request(self, method: str, path: str, *, params: Optional[dict[str, Any]] = None, payload: Optional[dict[str, Any]] = None) -> Any:
        endpoint = self.base_url + path
        if params:
            safe_params = {key: value for key, value in params.items() if value is not None}
            if safe_params:
                endpoint = f"{endpoint}?{parse.urlencode(safe_params, doseq=True)}"

        data = None
        headers = dict(self.config.headers)
        if payload is not None:
            data = json.dumps({key: value for key, value in payload.items() if value is not None}).encode("utf-8")

        req = request.Request(endpoint, data=data, headers=headers, method=method)
        try:
            with request.urlopen(req, timeout=self.config.timeout) as response:
                body = response.read().decode("utf-8")
                if not body:
                    return {}
                return json.loads(body)
        except error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"VegaTrade request failed ({exc.code}): {detail}") from exc


class TradingInfraAutomationClient(VegaTradeClient):
    """Backward-compatible alias for the base client."""

    pass
