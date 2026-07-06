import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.const import CONF_API_KEY
from homeassistant.helpers import selector
from .const import DOMAIN, CONF_STATION_ID, CONF_STATION_NAME, CONF_INCLUDE_BUSES

class SeoulBusConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            await self.async_set_unique_id(user_input[CONF_STATION_ID])
            self._abort_if_unique_id_configured()
            return self.async_create_entry(
                title=user_input.get(CONF_STATION_NAME) or f"정류장 {user_input[CONF_STATION_ID]}", 
                data=user_input
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_API_KEY): selector.TextSelector(selector.TextSelectorConfig(type=selector.TextSelectorType.PASSWORD)),
                vol.Required(CONF_STATION_ID): str,
                vol.Optional(CONF_STATION_NAME): str,
                vol.Optional(CONF_INCLUDE_BUSES): str,
            }),
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return SeoulBusOptionsFlowHandler(config_entry)

class SeoulBusOptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self._config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            # PASSWORD 타입 입력창은 기존 값이 있어도 화면엔 빈칸으로 보이므로,
            # 사용자가 다시 입력하지 않고 저장하면 빈 문자열로 덮어써질 수 있다.
            # 이 경우 기존에 저장된 API 키를 그대로 유지한다.
            if not user_input.get(CONF_API_KEY):
                existing = {**self._config_entry.data, **self._config_entry.options}
                user_input[CONF_API_KEY] = existing.get(CONF_API_KEY, "")
            return self.async_create_entry(title="", data=user_input)

        conf = {**self._config_entry.data, **self._config_entry.options}
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required(CONF_API_KEY, default=conf.get(CONF_API_KEY, "")): selector.TextSelector(selector.TextSelectorConfig(type=selector.TextSelectorType.PASSWORD)),
                vol.Required(CONF_STATION_ID, default=conf.get(CONF_STATION_ID, "")): str,
                vol.Optional(CONF_STATION_NAME, default=conf.get(CONF_STATION_NAME, "")): str,
                vol.Optional(CONF_INCLUDE_BUSES, default=conf.get(CONF_INCLUDE_BUSES, "")): str,
            }),
        )
