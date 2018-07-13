from astral import Astral

astral = Astral()
location = astral["Raleigh"]


def is_after(start):
    return lambda datetime: datetime > start

def is_before(end):
    return lambda datetime: datetime < end

def is_night(datetime):
    date = datetime.date()
    (dawn, dusk) = location.daylight(date=date, local=False)
    return datetime < dawn or datetime > dusk
