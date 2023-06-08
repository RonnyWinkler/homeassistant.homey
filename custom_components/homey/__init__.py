import asyncio
import json
import logging

import voluptuous as vol

from homeassistant.const import (CONF_NAME, ATTR_ICON)
from homeassistant.helpers import config_validation as cv
from homeassistant.loader import bind_hass
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.entity_component import EntityComponent

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'homey'
ENTITY_ID_FORMAT = DOMAIN + '.{}'

CONF_ICON = "icon"
CONF_CAPABILITIES = "capabilities"
CONF_CAPABILITIES_TITLES = "capabilitiesTitles"
CONF_CAPABILITIES_UNITS = "capabilitiesUnits"
CONF_CAPABILITIES_CONVERTERS = "capabilitiesConverters"

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        cv.slug: vol.Any({
            vol.Optional(CONF_NAME): cv.string,
            vol.Optional(CONF_ICON): cv.string,
            vol.Optional(CONF_CAPABILITIES): dict,
            vol.Optional(CONF_CAPABILITIES_TITLES): dict,
            vol.Optional(CONF_CAPABILITIES_UNITS): dict,
            vol.Optional(CONF_CAPABILITIES_CONVERTERS): dict
        }, None)
    })
}, extra=vol.ALLOW_EXTRA)

#@asyncio.coroutine
async def async_setup(hass, config):
    """Set up variables."""
    component = EntityComponent(_LOGGER, DOMAIN, hass)

    devices = []

    for device_id, device_config in config[DOMAIN].items():
        if not device_config:
            device_config = {}

        name = device_config.get(CONF_NAME)
        icon = device_config.get(CONF_ICON)
        capabilities = device_config.get(CONF_CAPABILITIES)
        capabilitiesTitles = device_config.get(CONF_CAPABILITIES_TITLES)
        capabilitiesUnits = device_config.get(CONF_CAPABILITIES_UNITS)
        capabilitiesConverters = device_config.get(CONF_CAPABILITIES_CONVERTERS)

        devices.append(Device(device_id, name, icon, capabilities, capabilitiesTitles, capabilitiesUnits, capabilitiesConverters))

#    yield from component.async_add_entities(devices)
    await component.async_add_entities(devices)

    return True

class Device(Entity):
    """Representation of a homey device."""

    def __init__(self, device_id, name, icon, capabilities, capabilitiesTitles, capabilitiesUnits, capabilitiesConverters):
        """Initialize a homey device."""
        self.entity_id = ENTITY_ID_FORMAT.format(device_id)
        self._name = name
        self._icon = icon
        self._capabilities = capabilities
        self._capabilitiesTitles = capabilitiesTitles
        self._capabilitiesUnits = capabilitiesUnits
        self._capabilitiesConverters = capabilitiesConverters

    #@asyncio.coroutine
    async def async_added_to_hass(self):
        """Run when entity about to be added."""
        super().async_added_to_hass()

    @property
    def should_poll(self):
        """If entity should be polled."""
        return False

    @property
    def name(self):
        """Return the name of the variable."""
        return self._name

    @property
    def icon(self):
        """Return the icon to be used for this entity."""
        return None

    @property
    def state(self):
        """Return the state of the component."""
        return ""

    @property
    def state_attributes(self):
        """Return the state attributes."""
        return {
            "icon": self._icon,
            "capabilities": self._capabilities,
            "capabilitiesTitles": self._capabilitiesTitles,
            "capabilitiesUnits": self._capabilitiesUnits,
            "capabilitiesConverters": self._capabilitiesConverters
        }
