#!/usr/bin/env python
from datetime import time
from functools import partial
from gpiozero import LED, MotionSensor
from signal import pause
from timers import always, at_dawn, at_dusk, at_morning, at_night


import logging
logging.basicConfig(
    format="%(levelname)s: %(message)s",
    level=logging.INFO
)

def log_sensor_activity(action="done something", sensor="a device"):
    logging.info("%s sensor has %s", sensor, action)

logging.info("Initializing devices...")

northeast_lamp = LED(2, active_high=False)
southeast_lamp = LED(3, active_high=False)
northeast_sensor = MotionSensor(14)
southeast_sensor = MotionSensor(15)

logging.info("Setting up device handlers...")

northeast_sensor.when_motion = partial(
    log_sensor_activity,
    sensor="northeast", action="activated"
)
northeast_sensor.when_no_motion = partial(
    log_sensor_activity,
    sensor="northeast", action="deactivated"
)
southeast_sensor.when_motion = partial(
    log_sensor_activity,
    sensor="southeast", action="activated"
)
southeast_sensor.when_no_motion = partial(
    log_sensor_activity,
    sensor="southeast", action="deactivated"
)

logging.info("Setting up scheduled handlers...")

def handle_dawn():
    logging.info("DAWN")
    northeast_lamp.off()
    southeast_lamp.off()

def handle_dusk():
    logging.info("DUSK")
    northeast_lamp.on()
    southeast_lamp.on()

def handle_morning():
    logging.info("MORNING")
    northeast_lamp.on()
    southeast_lamp.on()

def handle_night():
    logging.info("NIGHT")
    northeast_lamp.off()
    southeast_lamp.off()

always(at_dawn, handle_dawn)
always(at_dusk, handle_dusk)
always(at_morning, handle_morning)
always(at_night, handle_night)

logging.info("kestrel has started.")
pause()
