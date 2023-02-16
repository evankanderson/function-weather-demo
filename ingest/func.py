from typing import Any

from cloudevents.http import CloudEvent
from cloudevents.conversion import to_binary, to_json
import requests

def main(req: Any):
    # Use the same attributes for all events
    attributes = dict(type="com.example.cityquery", source="upload")

    resp = []
    for line in req.stream:
        line = str(line).strip()
        print("Handling '%s'", line)
        resp.append(CloudEvent(attributes, {"city": line}))
    
    return "\n-----\n".join([str(to_json(e)) for e in resp])