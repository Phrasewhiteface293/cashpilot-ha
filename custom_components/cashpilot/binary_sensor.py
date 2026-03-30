"""Binary sensor platform for the CashPilot integration."""

from __future__ import annotations

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DATA_SERVICES, DOMAIN
from .coordinator import CashPilotConfigEntry, CashPilotCoordinator
from .entity import CashPilotServiceEntity


async def async_setup_entry(
    hass: HomeAssistant,
    entry: CashPilotConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up CashPilot binary sensor entities."""
    coordinator: CashPilotCoordinator = hass.data[DOMAIN][entry.entry_id]
    entry_id = entry.entry_id
    entities: list[BinarySensorEntity] = []

    services = coordinator.data.get(DATA_SERVICES, [])
    for svc in services:
        slug = svc.get("slug", "")
        name = svc.get("name", slug)
        if not slug:
            continue
        entities.append(
            CashPilotServiceRunningSensor(coordinator, entry_id, slug, name)
        )

    async_add_entities(entities)


class CashPilotServiceRunningSensor(
    CashPilotServiceEntity, BinarySensorEntity
):
    """Whether a specific service container is running."""

    _attr_translation_key = "service_running"
    _attr_device_class = BinarySensorDeviceClass.RUNNING

    def __init__(
        self,
        coordinator: CashPilotCoordinator,
        entry_id: str,
        slug: str,
        service_name: str,
    ) -> None:
        super().__init__(coordinator, entry_id, slug, service_name)
        self._attr_unique_id = f"{entry_id}_{slug}_running"

    @property
    def is_on(self) -> bool | None:
        for svc in self.coordinator.data.get(DATA_SERVICES, []):
            if svc.get("slug") == self._slug:
                status = svc.get("container_status", "")
                return status.lower() == "running"
        return None
