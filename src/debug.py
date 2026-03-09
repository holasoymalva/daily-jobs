import requests
import json

url = "https://www.getonbrd.com/api/v0/search/jobs?query=junior"
res = requests.get(url, headers={"Accept": "application/json"})
data = res.json()
if data.get("data"):
    item = data["data"][0]
    print(json.dumps(item, indent=2)[:800])
