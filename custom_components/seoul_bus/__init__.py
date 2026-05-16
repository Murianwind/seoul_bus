import logging
from datetime import datetime, timedelta
import xmltodict
import async_timeout

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.const import CONF_API_KEY, Platform
from homeassistant.util import dt as dt_util
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from .const import DOMAIN, CONF_STATION_ID, CONF_INCLUDE_BUSES

_LOGGER = logging.getLogger(__name__)
PLATFORMS = [Platform.SENSOR, Platform.BUTTON, Platform.SWITCH]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    async def async_update_data():
        conf = {**entry.data, **entry.options}
        
        # 스위치가 꺼져있으면 API 호출을 건너뜀
        if not getattr(coordinator, "api_enabled", False):
            _LOGGER.debug("Seoul Bus update skipped: Switch is OFF")
            return {"status": "waiting", "items": coordinator.data.get("items", []) if coordinator.data else []}

        api_key = conf[CONF_API_KEY]
        station_id = conf[CONF_STATION_ID]
        url = f"http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?ServiceKey={api_key}&arsId={station_id}"
        
        try:
            async with async_timeout.timeout(15):
                session = async_get_clientsession(hass)
                async with session.get(url) as response:
                    res_text = await response.text()
                    data = xmltodict.parse(res_text)
                    items = data.get('ServiceResult', {}).get('msgBody', {}).get('itemList', [])
                    if not isinstance(items, list): items = [items] if items else []
                        
                    # 2.3: 버스 필터링
                    include_str = conf.get(CONF_INCLUDE_BUSES, "")
                    if include_str:
                        targets = [x.strip() for x in include_str.split(",")]
                        items = [i for i in items if i.get("rtNm") in targets or i.get("busRouteId") in targets]
                        
                    # 마지막 업데이트 시간 기록
                    coordinator.last_update_success_time = dt_util.now()
                    return {"status": "active", "items": items}
        except Exception as err:
            # 로그 출력 시 URL에서 API 키 마스킹
            safe_url = url.replace(api_key, "********")
            raise UpdateFailed(f"API Error at {safe_url}: {err}")

    coordinator = DataUpdateCoordinator(
        hass, _LOGGER, name=f"{DOMAIN}_{entry.data[CONF_STATION_ID]}",
        update_method=async_update_data,
        update_interval=timedelta(seconds=60),
    )
    
    # 최초 1회는 데이터를 강제로 불러와서 센서 목록을 생성하고 유지합니다.
    coordinator.api_enabled = True
    coordinator.last_update_success_time = dt_util.now()
    
    await coordinator.async_config_entry_first_refresh()

    # 초기 데이터 확보 후 기본값은 OFF로 설정 (스위치의 RestoreEntity가 실제 저장된 값을 복구함)
    coordinator.api_enabled = False

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    
    entry.async_on_unload(entry.add_update_listener(lambda h, e: h.config_entries.async_reload(e.entry_id)))
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
