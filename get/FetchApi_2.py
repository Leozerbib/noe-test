import get.Api_url_2

import requests

def fetch() : 
    url = fetch_genres()
    response = requests.get(url, headers=get.Api_url_2.headers)
    print(response.status_code)
    data = response.json()
    return data

def fetch_countries() :
    url = get.Api_url_2.api_url + get.Api_url_2.URL_fetch_Countries
    return url

def fetch_languages() :
    url = get.Api_url_2.api_url + get.Api_url_2.URL_fetch_Languages
    return url

def fetch_genres() :
    url = get.Api_url_2.api_url + get.Api_url_2.URL_fetch_Genres
    return url