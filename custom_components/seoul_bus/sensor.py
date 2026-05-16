from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.restore_state import RestoreEntity
from homeassistant.helpers.device_registry import DeviceInfo
from .const import DOMAIN, CONF_STATION_ID, CONF_STATION_NAME

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    station_id = entry.data[CONF_STATION_ID]
    station_name = entry.data.get(CONF_STATION_NAME) or f"정류장 {station_id}"
    
    async_add_entities([SeoulBusActiveSwitch(coordinator, station_id, station_name)])

class SeoulBusActiveSwitch(SwitchEntity, RestoreEntity):
    """API 업데이트 활성화/비활성화를 제어하는 스위치"""
    def __init__(self, coordinator, station_id, station_name):
        self._coordinator = coordinator
        self._station_id = station_id
        self._station_name = station_name
        self._attr_name = f"{station_name} 업데이트 활성화"
        self._attr_unique_id = f"{DOMAIN}_{station_id}_api_active_switch"
        self._attr_is_on = False

    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
            identifiers={(DOMAIN, self._station_id)},
            name=self._station_name,
            manufacturer="Seoul Bus",
        )

    async def async_added_to_hash(self) -> None:
        """이전 상태 복구"""
        await super().async_added_to_hash()
        last_state = await self.async_get_last_state()
        if last_state:
            self._attr_is_on = last_state.state == "on"
            self._coordinator.api_enabled = self._attr_is_on

    async def async_turn_on(self, **kwargs):
        """스위치 ON: API 업데이트 활성화"""
        self._attr_is_on = True
        self._coordinator.api_enabled = True
        await self._coordinator.async_request_refresh()
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs):
        """스위치 OFF: API 업데이트 중단"""
        self._attr_is_on = False
        self._coordinator.api_enabled = False
        self.async_write_ha_state()
