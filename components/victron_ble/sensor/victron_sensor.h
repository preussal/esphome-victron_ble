#pragma once

#include "esphome/components/sensor/sensor.h"
#include "esphome/components/victron_ble/victron_ble.h"

namespace esphome {
namespace victron_ble {

enum class VICTRON_SENSOR_TYPE {
  AC_OUT_POWER,
  ALARM_REASON,
  AUX_VOLTAGE,
  BATTERY_CURRENT,
  BATTERY_VOLTAGE,
  CHARGER_ERROR,
  CONSUMED_AH,
  DEVICE_STATE,
  LOAD_CURRENT,
  MID_VOLTAGE,
  PV_POWER,
  STATE_OF_CHARGE,
  TEMPERATURE,
  TIME_TO_GO,
  YIELD_TODAY,

  INVERTER_AC_APPARENT_POWER,
  INVERTER_AC_VOLTAGE,
  INVERTER_AC_CURRENT,

  DCDC_CONVERTER_INPUT_VOLTAGE,
  DCDC_CONVERTER_OUTPUT_VOLTAGE,
  DCDC_CONVERTER_OFF_REASON,

  SMART_LITHIUM_BMS_FLAGS,
  SMART_LITHIUM_ERROR,
  SMART_LITHIUM_CELL1,
  SMART_LITHIUM_CELL2,
  SMART_LITHIUM_CELL3,
  SMART_LITHIUM_CELL4,
  SMART_LITHIUM_CELL5,
  SMART_LITHIUM_CELL6,
  SMART_LITHIUM_CELL7,
  SMART_LITHIUM_CELL8,
  SMART_LITHIUM_BALANCER_STATUS,

  SMART_BATTERY_PROTECT_OUTPUT_STATE,
  SMART_BATTERY_PROTECT_ERROR_CODE,
  SMART_BATTERY_PROTECT_WARNING_REASON,
  SMART_BATTERY_PROTECT_INPUT_VOLTAGE,
  SMART_BATTERY_PROTECT_OUTPUT_VOLTAGE,
  SMART_BATTERY_PROTECT_OFF_REASON,

  LYNX_SMART_BMS_ERROR,
  LYNX_SMART_BMS_IO_STATUS,
  LYNX_SMART_BMS_WARNINGS_ALARMS,

  MULTI_RS_ACTIVE_AC_IN,
  MULTI_RS_ACTIVE_AC_IN_POWER,

  VE_BUS_ERROR,
  VE_BUS_ACTIVE_AC_IN,
  VE_BUS_ACTIVE_AC_IN_POWER,
  VE_BUS_ALARM,

  DC_ENERGY_METER_BMV_MONITOR_MODE,
};

class VictronSensor : public Component, public sensor::Sensor, public Parented<VictronBle> {
 public:
  void dump_config() override;
  void setup() override;

  void set_type(VICTRON_SENSOR_TYPE val) { this->type_ = val; }

 protected:
  VICTRON_SENSOR_TYPE type_;
};
}  // namespace victron_ble
}  // namespace esphome