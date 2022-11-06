#Homey-Integration: Compound device definition for Home-Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=flat-square)](https://github.com/hacs)
[![GH-release](https://img.shields.io/github/v/release/RonnyWinkler/homeassistant.homey.svg?style=flat-square)](https://github.com/RonnyWinkler/homeassistant.homey/releases)
[![GH-downloads](https://img.shields.io/github/downloads/RonnyWinkler/homeassistant.homey/total?style=flat-square)](https://github.com/RonnyWinkler/homeassistant.homey/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/RonnyWinkler/homeassistant.homey.svg?style=flat-square)](https://github.com/RonnyWinkler/homeassistant.homey/commits/master)
[![GH-code-size](https://img.shields.io/github/languages/code-size/RonnyWinkler/homeassistant.homey.svg?color=red&style=flat-square)](https://github.com/RonnyWinkler/homeassistant.homey)
<a href="https://paypal.me/winklerronny"><img src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif" height="20"></a>

HowTo use the compounds component in HA to create entity groups.

## Install the component in HomeAssistant

1) Install this component in HACS... or copy the folder "homey" to your HomeAssistant custom_components folder (/config/custom_components/homey).
2) Restart HomeAssistant to activate the component


## Prepare the YAML file

Copy an example into your configuration.yaml. Or copy the include into the file "homey.yaml" and add this line to your configuration.yaml:
```yaml
homey: !include homey.yaml
```
Restart HomeAssistant after YAML changes.

## Customize the YAML file to define entity groups

Example for usage in configuration.yaml. Start with the homey element followed by the compound element:
```yaml
homey:
  livingroom_compound:
    name: Livingroom environment
    capabilities:
      measure_temperature: sensor.livingroom_temperature
      measure_temperature.temp1: sensor.livingroom_temperature_1
      measure_temperature.temp3: sensor.livingroom_temperature_2
```

Example for usage in homey.yaml. Start with the compound element:
```yaml
livingroom_compound:
  name: Livingroom environment
  capabilities:
    measure_temperature: sensor.livingroom_temperature
    measure_temperature.temp1: sensor.livingroom_temperature_1
    measure_temperature.temp3: sensor.livingroom_temperature_2
```

## Set up a compound with entities

The "livingroom_compound" will be the compound that gets importes to Homey.
You can set a name that is used as device name. You can rename it in Homey.
Add the capabilities. If you want to add more than one capability of the same type, you can use subcapabilities (capability.sub).

In addition you can set a title for each capability (optional) using "capabilitiesTitles":
```yaml
    capabilitiesTitles:
      measure_temperature: "Temperature title"
      measure_temperature.temp1: "Temperature subcapability 1 title"
      measure_temperature.temp2: "Temperature subcapability 2 title"
```

Example for a plug with measurement sensors:
```yaml
plug:
  name: Plug (Example for plug with power measurement)
  capabilities:
    onoff: switch.plug_on
    meter_power: sensor.plug_power
    measure_power: sensor.plug_power_current
  capabilitiesTitles:
    onoff: Switch
    meter_power: Power meter
    measure_power: Power current
```

## Set up a compound with entity attributes

In addition to entities, you can use attributes, too. 
Just add the attribute to the entity id separated with a dot.
```yaml
my_device_tracker:
  name: Device Name
  capabilities:
    measure_generic: device_tracker.entity_id
    measure_generic.ip: device_tracker.entity_id.ip
    measure_generic.mac: device_tracker.entity_id.mac
    measure_generic.wired: device_tracker.entity_id.is_wired
  capabilitiesTitles:
    measure_generic: State
    measure_generic.ip: IP
    measure_generic.mac: MAC
```

This example creates a device tracker device. The first capability ist the entity itself. As value, the entity state is used.
In addition, some entity attributes are added as subcapability. Please ensure, that every defined capability is unique in the YAML. Use subcapabilities to define several string capabilities using the measure_generic capability.


## Possible capabilities:

- onoff - Homey switch
- button - Homey button
- locked - lock state
- dim (as slider for input_number.set_value
- alarm_battery - all alarm capabilities are boolean values
- alarm_co
- alarm_co2
- alarm_contact
- alarm_fire
- alarm_generic
- alarm_heat
- alarm_motion
- alarm_pm25
- alarm_smoke
- alarm_tamper
- alarm_water
- measure_generic - string value
- measure_numeric - all other measure* and meas* capabilities are using numeric values
- measure_battery
- measure_co
- measure_co2
- measure_current
- measure_gust_angle
- measure_gust_strength
- measure_humidity
- measure_luminance
- measure_noise
- measure_pm25
- measure_power
- measure_pressure
- measure_rain
- measure_temperature
- measure_ultraviolet
- measure_voltage
- measure_water
- measure_wind_angle
- measure_wind_strength
- meter_gas
- meter_water
- meter_power
- meter_rain

## Use Icons

You can set an icon for your compound device  (optional):
```yaml
livingroom_compound:
  name: Livingroom environment
  icon: measure_temperature
```

Possible icons:
- alarm_contact
- alarm_generic
- alarm_heat
- alarm_motion
- alarm_pressure
- alarm_smoke
- alarm_tamper
- alarm_water
- measure_battery
- measure_co2
- measure_current
- measure_generic
- measure_humidity
- measure_luminance
- measure_noise
- measure_numeric
- measure_power
- measure_pressure
- measure_temperature
- measure_voltage
- meter_power

## Use Units

You can set an unit for every capability (optional) using "capabilitiesUnits":
```yaml
temperature:
  name: Outside temperature
  icon: measure_temperature
  capabilities:
    measure_temperature.temp1: your entity
    measure_temperature.temp2: your entity
  capabilitiesTitles:
    measure_temperature.temp1: "Temperature 1 title"
    measure_temperature.temp2: "Temperature 2 title"
  capabilitiesUnits:
    measure_temperature.temp1: "°C"
    measure_temperature.temp2: "°C"
```

This overwrites the unit which can be present in the HA entity.
You can use this unit settings to define units for attributes, too.

## References

Homey app:
https://homey.app/a/io.home-assistant.community/

Homey community with app description and examples:
https://community.homey.app/t/app-pro-home-assistant-community-app/71477