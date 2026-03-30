"""Button platform for the CashPilot integration."""

from __future__ import annotations

import logging

from homeassistant.components.button import ButtonEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .api import CashPilotError
from .const import DATA_SERVICES, DOMAIN
from .coordinator import CashPilotConfigEntry, CashPilotCoordinator
from .entity import CashPilotEntity, CashPilotServiceEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: CashPilotConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up CashPilot button entities."""
    coordinator: CashPilotCoordinator = hass.data[DOMAIN][entry.entry_id]
    entry_id = entry.entry_id
    entities: list[ButtonEntity] = []

    # Dashboard-level button
    entities.append(CashPilotCollectButton(coordinator, entry_id))

    # Per-service restart buttons
    services = coordinator.data.get(DATA_SERVICES, [])
    for svc in services:
        slug = svc.get("slug", "")
        name = svc.get("name", slug)
        if not slug:
            continue
        entities.append(
            CashPilotServiceRestartButton(coordinator, entry_id, slug, name)
        )

    async_add_entities(entities)


class CashPilotCollectButton(CashPilotEntity, ButtonEntity):
    """Button to trigger a manual earnings collection."""

    _attr_translation_key = "collect_earnings"
    _attr_icon = "mdi:refresh"

    def __init__(
        self, coordinator: CashPilotCoordinator, entry_id: str
    ) -> None:
        super().__init__(coordinator, entry_id)
        self._attr_unique_id = f"{entry_id}_collect_earnings"

    async def async_press(self) -> None:
        """Trigger earnings collection."""
        try:
            await self.coordinator.client.async_collect_earnings()
        except CashPilotError:
            _LOGGER.exception("Failed to trigger earnings collection")
            return
        await self.coordinator.async_request_refresh()


class CashPilotServiceRestartButton(CashPilotServiceEntity, ButtonEntity):
    """Button to restart a service."""

    _attr_translation_key = "service_restart"
    _attr_icon = "mdi:restart"

    def __init__(
        self,
        coordinator: CashPilotCoordinator,
        entry_id: str,
        slug: str,
        service_name: str,
    ) -> None:
        super().__init__(coordinator, entry_id, slug, service_name)
        self._attr_unique_id = f"{entry_id}_{slug}_restart"

    async def async_press(self) -> None:
        """Restart the service."""
        try:
            await self.coordinator.client.async_restart_service(self._slug)
        except CashPilotError:
            _LOGGER.exception("Failed to restart service %s", self._slug)
            return
        await self.coordinator.async_request_refresh()
