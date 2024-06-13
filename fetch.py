import requests
import til
import get.FetchApi_2


import urllib.request
import json
with urllib.request.urlopen("https://api.watchmode.com/v1/sources/?apiKey=YOUR_API_KEY") as url:
    data = json.loads(url.read().decode())
    print(data)
