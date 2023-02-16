from typing import Any

from cloudevents.http import CloudEvent
from cloudevents.conversion import to_binary, to_json
import requests

def main(req: Any):
    # Use the same attributes for all events
    attributes = dict(type="com.example.cityquery")

    resp = []
    for line in req.data:
        line = line.strip()
        resp.append(CloudEvent(attributes, {"city": line}))
    
    return "\n-----\n".join([to_json(e) for e in resp])