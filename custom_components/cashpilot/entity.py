"""Base entity for the CashPilot integration."""

from __future__ import annotations

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, MANUFACTURER
from .coordinator import CashPilotCoordinator


class CashPilotEntity(CoordinatorEntity[CashPilotCoordinator]):
    """Base class for CashPilot entities."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: CashPilotCoordinator,
        entry_id: str,
    ) -> None:
        """Initialize the base entity."""
        super().__init__(coordinator)
        self._entry_id = entry_id

    @property
    def device_info(self) -> DeviceInfo:
        """Return device info for the main CashPilot device."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._entry_id)},
            name="CashPilot",
            manufacturer=MANUFACTURER,
            entry_type=None,
        )


class CashPilotServiceEntity(CoordinatorEntity[CashPilotCoordinator]):
    """Base class for per-service CashPilot entities."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: CashPilotCoordinator,
        entry_id: str,
        slug: str,
        service_name: str,
    ) -> None:
        """Initialize the per-service entity."""
        super().__init__(coordinator)
        self._entry_id = entry_id
        self._slug = slug
        self._service_name = service_name

    @property
    def device_info(self) -> DeviceInfo:
        """Return device info for this service."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._slug)},
            name=self._service_name,
            manufacturer=MANUFACTURER,
            model="Passive Income Service",
            via_device=(DOMAIN, self._entry_id),
        )
