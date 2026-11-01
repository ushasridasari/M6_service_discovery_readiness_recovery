import time
import requests

URL = "http://inventory-service/inventory"

while True:
    try:
        r = requests.get(URL, timeout=2)
        print(f"{time.strftime('%H:%M:%S')} status={r.status_code} pod={r.json()['pod']}", flush=True)
    except Exception as e:
        print(f"{time.strftime('%H:%M:%S')} ERROR: {e}", flush=True)
    time.sleep(1)
