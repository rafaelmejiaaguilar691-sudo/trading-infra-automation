# trading-infra-automation

Python SDK for the VegaTrade trading API with automation helpers.

## Supported Python versions

This project supports Python 3.9 through 3.13 and includes CI coverage for each supported release.

## Installation

```bash
python -m pip install -e .[test]
```

## Usage

```python
from trading_infra_automation import VegaTradeClient

client = VegaTradeClient(api_key="your-api-key")
print(client.ping())
```

## Project layout

- `src/trading_infra_automation/` - Python SDK package
- `src/vega_trade/` - compatibility import path
- `.github/workflows/ci.yml` - GitHub Actions matrix for Python versions
- `tox.ini` - local multi-version test configuration

