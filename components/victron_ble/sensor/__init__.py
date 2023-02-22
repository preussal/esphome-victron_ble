from esphome.components import sensor
import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.const import (
    CONF_ACCURACY_DECIMALS,
    CONF_DEVICE_CLASS,
    CONF_ID,
    CONF_TYPE,
    CONF_ICON,
    CONF_UNIT_OF_MEASUREMENT,
    UNIT_AMPERE,
    UNIT_CELSIUS,
    UNIT_EMPTY,
    UNIT_MINUTE,
    UNIT_VOLT,
    UNIT_WATT,
    UNIT_KILOWATT_HOURS,
    ICON_BATTERY,
    ICON_POWER,
    ICON_THERMOMETER,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_DURATION,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_VOLTAGE,
    STATE_CLASS_MEASUREMENT,
)
from .. import victron_ble_ns, CONF_VICTRON_BLE_ID, VictronBle

DEPENDENCIES = ["victron_ble"]
CODEOWNERS = ["@Fabian-Schmidt"]

UNIT_AMPERE_HOURS = "Ah"

VictronSensor = victron_ble_ns.class_(
    "VictronSensor", sensor.Sensor, cg.Component)

VICTRON_SENSOR_TYPE = victron_ble_ns.namespace("VICTRON_SENSOR_TYPE")

CONF_SUPPORTED_TYPE = {
    "BATTERY_MONITOR_TIME_TO_GO":  {
        CONF_TYPE: VICTRON_SENSOR_TYPE.BATTERY_MONITOR_TIME_TO_GO,
        CONF_UNIT_OF_MEASUREMENT: UNIT_MINUTE,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 0,
        CONF_DEVICE_CLASS: DEVICE_CLASS_DURATION,
    },
    "BATTERY_MONITOR_BATTERY_VOLTAGE":  {
        CONF_TYPE: VICTRON_SENSOR_TYPE.BATTERY_MONITOR_BATTERY_VOLTAGE,
        CONF_UNIT_OF_MEASUREMENT: UNIT_VOLT,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 2,
        CONF_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    },
    "BATTERY_MONITOR_ALARM_REASON":  {
        CONF_TYPE: VICTRON_SENSOR_TYPE.BATTERY_MONITOR_ALARM_REASON,
    },
    "BATTERY_MONITOR_AUX_VOLTAGE":  {
        CONF_TYPE: VICTRON_SENSOR_TYPE.BATTERY_MONITOR_AUX_VOLTAGE,
        CONF_UNIT_OF_MEASUREMENT: UNIT_VOLT,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 2,
        CONF_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    },
    "BATTERY_MONITOR_MID_VOLTAGE":  {
        CONF_TYPE: VICTRON_SENSOR_TYPE.BATTERY_MONITOR_MID_VOLTAGE,
        CONF_UNIT_OF_MEASUREMENT: UNIT_VOLT,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 2,
        CONF_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    },
    "BATTERY_MONITOR_TEMPERATURE":  {
        CONF_TYPE: VICTRON_SENSOR_TYPE.BATTERY_MONITOR_TEMPERATURE,
        CONF_UNIT_OF_MEASUREMENT: UNIT_CELSIUS,
        CONF_ICON: ICON_THERMOMETER,
        CONF_ACCURACY_DECIMALS: 2,
        CONF_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
    },
    "BATTERY_MONITOR_BATTERY_CURRENT":  {
        CONF_TYPE: VICTRON_SENSOR_TYPE.BATTERY_MONITOR_BATTERY_CURRENT,
        CONF_UNIT_OF_MEASUREMENT: UNIT_AMPERE,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 3,
        CONF_DEVICE_CLASS: DEVICE_CLASS_CURRENT,
    },
    "BATTERY_MONITOR_CONSUMED_AH":  {
        CONF_TYPE: VICTRON_SENSOR_TYPE.BATTERY_MONITOR_CONSUMED_AH,
        CONF_UNIT_OF_MEASUREMENT: UNIT_AMPERE_HOURS,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 1,
        # device_class=???,
    },
    "BATTERY_MONITOR_STATE_OF_CHARGE":  {
        CONF_TYPE: VICTRON_SENSOR_TYPE.BATTERY_MONITOR_STATE_OF_CHARGE,
        CONF_UNIT_OF_MEASUREMENT: UNIT_AMPERE,
        CONF_ICON: ICON_BATTERY,
        CONF_ACCURACY_DECIMALS: 3,
        CONF_DEVICE_CLASS: DEVICE_CLASS_CURRENT,
    },
    
    "SOLAR_CHARGER_DEVICE_STATE":  {
        CONF_TYPE: VICTRON_SENSOR_TYPE.SOLAR_CHARGER_DEVICE_STATE,
    },
    "SOLAR_CHARGER_CHARGER_ERROR":  {
        CONF_TYPE: VICTRON_SENSOR_TYPE.SOLAR_CHARGER_CHARGER_ERROR,
    },
    "SOLAR_CHARGER_BATTERY_VOLTAGE":  {
        CONF_TYPE: VICTRON_SENSOR_TYPE.SOLAR_CHARGER_BATTERY_VOLTAGE,
        CONF_UNIT_OF_MEASUREMENT: UNIT_VOLT,
        CONF_ICON: ICON_POWER,
        CONF_ACCURACY_DECIMALS: 2,
        CONF_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    },
    "SOLAR_CHARGER_BATTERY_CURRENT":  {
        CONF_TYPE: VICTRON_SENSOR_TYPE.SOLAR_CHARGER_BATTERY_CURRENT,
        CONF_UNIT_OF_MEASUREMENT: UNIT_AMPERE,
        CONF_ICON: ICON_POWER,
        CONF_ACCURACY_DECIMALS: 1,
        CONF_DEVICE_CLASS: DEVICE_CLASS_CURRENT,
    },
    "SOLAR_CHARGER_YIELD_TODAY":  {
        CONF_TYPE: VICTRON_SENSOR_TYPE.SOLAR_CHARGER_YIELD_TODAY,
        CONF_UNIT_OF_MEASUREMENT: UNIT_KILOWATT_HOURS,
        CONF_ICON: ICON_POWER,
        CONF_ACCURACY_DECIMALS: 2,
        CONF_DEVICE_CLASS: DEVICE_CLASS_ENERGY,
    },
    "SOLAR_CHARGER_PV_POWER":  {
        CONF_TYPE: VICTRON_SENSOR_TYPE.SOLAR_CHARGER_PV_POWER,
        CONF_UNIT_OF_MEASUREMENT: UNIT_WATT,
        CONF_ICON: ICON_POWER,
        CONF_ACCURACY_DECIMALS: 0,
        CONF_DEVICE_CLASS: DEVICE_CLASS_POWER,
    },
    "SOLAR_CHARGER_LOAD_CURRENT":  {
        CONF_TYPE: VICTRON_SENSOR_TYPE.SOLAR_CHARGER_LOAD_CURRENT,
        CONF_UNIT_OF_MEASUREMENT: UNIT_AMPERE,
        CONF_ICON: ICON_POWER,
        CONF_ACCURACY_DECIMALS: 1,
        CONF_DEVICE_CLASS: DEVICE_CLASS_CURRENT,
    },
}


def set_default_based_on_type():
    def set_defaults_(config):
        # set defaults based on sensor type:
        if CONF_UNIT_OF_MEASUREMENT not in config and \
           CONF_UNIT_OF_MEASUREMENT in CONF_SUPPORTED_TYPE[config[CONF_TYPE]]:
            config[CONF_UNIT_OF_MEASUREMENT] = CONF_SUPPORTED_TYPE[config[CONF_TYPE]
                                                                   ][CONF_UNIT_OF_MEASUREMENT]
        if CONF_ICON not in config and \
           CONF_ICON in CONF_SUPPORTED_TYPE[config[CONF_TYPE]]:
            config[CONF_ICON] = CONF_SUPPORTED_TYPE[config[CONF_TYPE]][CONF_ICON]
        if CONF_ACCURACY_DECIMALS not in config and \
           CONF_ACCURACY_DECIMALS in CONF_SUPPORTED_TYPE[config[CONF_TYPE]]:
            config[CONF_ACCURACY_DECIMALS] = CONF_SUPPORTED_TYPE[config[CONF_TYPE]
                                                                 ][CONF_ACCURACY_DECIMALS]
        if CONF_DEVICE_CLASS not in config and \
           CONF_DEVICE_CLASS in CONF_SUPPORTED_TYPE[config[CONF_TYPE]]:
            config[CONF_DEVICE_CLASS] = CONF_SUPPORTED_TYPE[config[CONF_TYPE]
                                                            ][CONF_DEVICE_CLASS]
        return config

    return set_defaults_


CONFIG_SCHEMA = sensor.sensor_schema(
    state_class=STATE_CLASS_MEASUREMENT
).extend(
    {
        cv.GenerateID(): cv.declare_id(VictronSensor),
        cv.GenerateID(CONF_VICTRON_BLE_ID): cv.use_id(VictronBle),
        cv.Required(CONF_TYPE): cv.enum(CONF_SUPPORTED_TYPE, upper=True),
    }
).extend(cv.COMPONENT_SCHEMA)
FINAL_VALIDATE_SCHEMA = set_default_based_on_type()


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)
    await cg.register_parented(var, config[CONF_VICTRON_BLE_ID])

    cg.add(var.set_type(CONF_SUPPORTED_TYPE[config[CONF_TYPE]][CONF_TYPE]))
