import requests
import config
import json

url = "https://api.playbattlegrounds.com/shards/pc-na/players?filter[playerNames]=Gold_n"

header = {
  "Authorization": "Bearer " + config.APIKEY,
  "Accept": "application/vnd.api+json"
}

r = requests.get(url, headers=header)

if r.status_code != 200:
    print("Status: " + str(r.status_code) + "Problem with the request.")
else:
    data = r.json()
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, sort_keys = True, indent = 4, ensure_ascii = False)

