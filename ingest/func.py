import csv
import io
import logging
from typing import Any

from cloudevents.http import CloudEvent
from cloudevents.conversion import to_binary, to_json
import requests

def main(req: Any):
    # Use the same attributes for all events
    attributes = dict(type="com.example.cityquery", source="upload")

    reader = csv.reader(io.TextIOWrapper(req.stream, encoding='utf-8'), strict=True)

    resp = []
    for row in reader:
        logging.info("Handling '%s'", row[0])

        resp.append(CloudEvent(attributes, {"city": row[0], "state": row[1]}))
    
    return "\n-----\n".join([to_json(e).decode('utf-8') for e in resp])