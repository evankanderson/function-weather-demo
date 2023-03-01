import logging
import os
from typing import Any

import noaa_sdk
from redis import Sentinel, Redis

def initRedis():
    if os.environ.get('SENTINEL_HOST'):
        s = Sentinel([(os.environ['SENTINEL_HOST'], 26379)])
        return s.master_for('mymaster')
    if os.environ.get('REDIS_HOST'):
        return Redis(host=os.environ['REDIS_HOST'])
    logging.warn("Unable to locate ")
    return None

noaa = noaa_sdk.NOAA()

redis = initRedis()

def fetch(data: Any, attributes: dict):
    if data is None:
        logging.warn("Skipping empty body")
        return None
    zip = data.get('zip')

    res = noaa.get_forecasts(zip, 'US', type='forecastHourly')

    redis.set(zip, res[0])

    logging.info("Stored %s for %s", res[0].get('shortForecast'), zip)

    # Your function implementation goes here
    return None

