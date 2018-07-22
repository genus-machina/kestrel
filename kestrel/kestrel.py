#!/usr/bin/env python
from functools import partial
from gpiozero import LED, MotionSensor
from handlers import do, turn_lamp_off, turn_lamp_on
from signal import pause
from timers import always, at_dawn, at_dusk, at_morning, at_night

import logging
logging.basicConfig(
    format="%(levelname)s: %(message)s",
    level=logging.INFO
)

logging.info("Initializing devices...")

northeast_lamp = LED(2, active_high=False)
southeast_lamp = LED(3, active_high=False)
northeast_sensor = MotionSensor(14)
southeast_sensor = MotionSensor(15)

logging.info("Setting up device handlers...")

northeast_sensor.when_motion = partial(
    logging.info,
    "northeast sensor has activated"
)
northeast_sensor.when_no_motion = partial(
    logging.info,
    "northeast sensor has deactivated"
)
southeast_sensor.when_motion = partial(
    logging.info,
    "southeast sensor has activated"
)
southeast_sensor.when_no_motion = partial(
    logging.info,
    "southeast sensor has deactivated"
)

logging.info("Setting up scheduled handlers...")

always(
    at_dawn, do(
        partial(logging.info, "DAWN"),
        turn_lamp_off(northeast_lamp),
        turn_lamp_off(southeast_lamp)
    )
)

always(
    at_dusk, do(
        partial(logging.info, "DUSK"),
        turn_lamp_on(northeast_lamp),
        turn_lamp_on(southeast_lamp)
    )
)

always(
    at_morning, do(
        partial(logging.info, "MORNING"),
        turn_lamp_on(northeast_lamp),
        turn_lamp_on(southeast_lamp)
    )
)

always(
    at_night, do(
        partial(logging.info, "NIGHT"),
        turn_lamp_off(northeast_lamp),
        turn_lamp_off(southeast_lamp)
    )
)

logging.info("kestrel has started.")
pause()
