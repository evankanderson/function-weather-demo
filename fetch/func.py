import os
from typing import Any

import noaa_sdk
from redis import Sentinel, Redis

noaa = noaa_sdk.NOAA()

redis = None
if os.environ.get('REDIS_SENTINEL'):
    redis = Sentinel([(os.environ['REDIS_SENTINEL'], 26379)])
else:
    redis = Redis(host=os.environ['REDIS_HOST'], )

def fetch(data: Any, attributes: dict):
    zip = data.get('zip')

    res = noaa.get_forecasts(zip, 'US', type='forecastHourly')

    redis.set(zip, res[0])

    logging.info("Stored %s for %s", res[0].get('shortForecast'), zip)

    # Your function implementation goes here
    return None
