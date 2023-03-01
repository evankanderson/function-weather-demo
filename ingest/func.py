import csv
import io
import logging
import os
from typing import Any

from cloudevents.http import CloudEvent
from cloudevents.conversion import to_binary, to_json
import requests

def main(req: Any):
    # Use the same attributes for all events
    attributes = dict(type="com.example.cityquery", source="upload")

    reader = csv.reader(io.TextIOWrapper(req.stream, encoding='utf-8'), strict=True)
    resp = []

    handleEvent = lambda e: resp.append(to_json(e).decode('utf-8'))

    if os.environ.get('K_SINK'):
        handleEvent = SendEvent

    for row in reader:
        logging.info("Handling '%s'", row[0])
        event = CloudEvent(attributes, {"city": row[0], "state": row[1]})
        handleEvent(event)
    
    return "\n-----\n".join(resp)

def SendEvent(event: CloudEvent):
    headers, body = to_binary(event)
    requests.post(os.environ['K_SINK'], data=body, headers=headers)