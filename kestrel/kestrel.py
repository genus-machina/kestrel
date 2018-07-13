#!/usr/bin/env python
from functools import partial
from gpiozero import MotionSensor
from signal import pause

import logging
logging.basicConfig(
    format="%(levelname)s: %(message)s",
    level=logging.INFO
)


def log_sensor_activity(**kwargs):
    logging.info("%s sensor has %s", kwargs["sensor"], kwargs["action"])


northeast_sensor = MotionSensor(14)
southeast_sensor = MotionSensor(15)

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

logging.info("kestrel has started")
pause()
