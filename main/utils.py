import datetime


def uuid_to_date(uuid):
    timestamp = uuid.split("-")[0]
    if timestamp:
        date = datetime.fromtimestamp(int(timestamp) / 1000)
        return date
