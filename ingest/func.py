import csv
from typing import Any

from cloudevents.http import CloudEvent
from cloudevents.conversion import to_binary, to_json
import requests

def main(req: Any):
    # Use the same attributes for all events
    attributes = dict(type="com.example.cityquery", source="upload")

    reader = csv.reader(req.stream)

    resp = []
    for row in reader:
        print("Handling '%s'", row[0])
        resp.append(CloudEvent(attributes, {"city": row[0]}))
    
    return "\n-----\n".join([str(to_json(e)) for e in resp])