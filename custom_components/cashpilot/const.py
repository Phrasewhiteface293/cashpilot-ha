"""Constants for the CashPilot integration."""

from typing import Final

DOMAIN: Final = "cashpilot"
MANUFACTURER: Final = "CashPilot"

CONF_URL: Final = "url"
CONF_USERNAME: Final = "username"
CONF_PASSWORD: Final = "password"

DEFAULT_URL: Final = "http://localhost:8080"
DEFAULT_SCAN_INTERVAL: Final = 300  # 5 minutes

DATA_SUMMARY: Final = "summary"
DATA_BREAKDOWN: Final = "breakdown"
DATA_SERVICES: Final = "services"
DATA_HEALTH: Final = "health"
DATA_FLEET: Final = "fleet"
