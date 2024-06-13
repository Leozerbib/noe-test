import get.Api_url_1

import requests

def fetch() : 
    url = fetch_plateforme()
    response = requests.get(url)
    print(response.status_code)
    data = response.json()
    return data

def fetch_plateforme() :
    url = get.Api_url_1.URL_fetch_plateform 
    return url

