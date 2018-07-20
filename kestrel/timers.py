from astral import Astral
from datetime import datetime, time, timedelta, timezone
import threading

def after(delay, handler):
    threading.Timer(delay.total_seconds(), handler).start()

def at(when, handler):
    now = datetime.now(timezone.utc)
    delay = when - now
    after(delay, handler)

def at_dawn(handler):
    location = Astral()[LOCATION]
    dawn = next(location.dawn(local=False).timetz())
    return at(dawn, handler)

def at_dusk(handler):
    location = Astral()[LOCATION]
    dusk = next(location.dusk(local=False).timetz())
    return at(dusk, handler)

def at_morning(handler):
    morning = next(MORNING)
    return at(morning, handler)

def at_night(handler):
    night = next(NIGHT)
    return at(night, handler)

def local_timezone():
    delta = datetime.now() - datetime.utcnow()
    minutes = round(delta.total_seconds() / 60)
    return timezone(timedelta(minutes=minutes))

def next(time):
    now = datetime.now(timezone.utc)
    if now.timetz() < time:
        return datetime.combine(now.date(), time)
    else:
        return datetime.combine(now.date() + timedelta(days=1), time)

LOCATION = "Raleigh"
MORNING = time(5, 0, 0, tzinfo=local_timezone())
NIGHT = time(22, 0, 0, tzinfo=local_timezone())
