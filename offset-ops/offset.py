
import requests
import json

base_uri = "http://<host-address>:8082"
res = requests.get(
    url=f"{base_uri}/consumers/<group>/instances/<consumer>/offsets",
    data=json.dumps(
        dict(partitions=[
            dict(topic="test_topic", partition=p) for p in [0, 1, 2]
        ])),
    headers={"Content-Type": "application/vnd.kafka.v2+json"}).json()

print(json.dumps(res, indent=2))
