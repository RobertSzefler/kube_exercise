#!/usr/bin/env python3.11

import json
import subprocess

out = subprocess.check_output("kubectl get pods -o json", shell=True).decode('utf-8')
data = json.loads(out)

for item in data["items"]:
	if item["kind"] != "Pod": continue
	status = item["status"]
	print(f"* app: {item['metadata']['labels']['app']}, phase {status['phase']}, started {status['startTime']}")
	for cstat in status["containerStatuses"]:
		print(f"  image: {cstat['image']}")
		print(f"  image id: {cstat['imageID']}")
