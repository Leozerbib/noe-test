import get.Api_url_2
import json
import requests

TWITCH_CLIENT_ID = get.Api_url_2.Client_ID
TWITCH_SECRET = get.Api_url_2.auth_key

# Obtenir le token d'accès de Twitch
def get_twitch_access_token():
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': TWITCH_CLIENT_ID,
        'client_secret': TWITCH_SECRET,
        'grant_type': 'client_credentials'
    }
    print(params)
    response = requests.post(url, params=params)
    response.raise_for_status()
    print(response.json())
    return response.json()['access_token']
    


def fetch_game(id, i) :
    url = get.Api_url_2.URL_fetch_GAME
    print(id)
    ma_liste_sans_null = [x for x in id if x is not '']

    liste_en_string = '(' + ','.join(map(str, ma_liste_sans_null)) + ')'

    print(liste_en_string)
    print(f"fetch_game batch : {i}/100")
    headers = {
        'Authorization':f'Bearer {get_twitch_access_token()}',
        'Client-Id': 'de0st9nif0zdqgdcue9vgyuvkp0ys8'
    }
    response = requests.post(url, headers=headers, data=f'fields age_ratings,aggregated_rating,category,checksum,created_at,first_release_date,game_engines,game_localizations,game_modes,genres,language_supports,multiplayer_modes,name,platforms,rating,rating_count,release_dates,similar_games,status,tags,themes,total_rating,total_rating_count; where id = (' + ','.join(map(str, all_game)) + ');')
    print(response.status_code)
    print(response.json())
    data = response.json()
    return data

def fetch_game_per_top() :
    with open('datalake/raw/Twitch/game/top1000games/response.json', 'r') as file:
        top_games = json.load(file)
    # Liste pour stocker les résultats
    all_game = []
    # Taille de la sous-liste
    taille_sous_liste = 10

    for j in range(0, len(top_games), taille_sous_liste):
        sous_liste = []
        for i in range(j, j + taille_sous_liste):
            game_id = top_games[i]['igdb_id']
            sous_liste.append(game_id)
        for i in fetch_game(sous_liste,j):
            all_game.append(i)
    return all_game
        

    

def fetch_age_rating() :
    url = get.Api_url_2.URL_fetch_AGE_RATING
    headers = {
        'Authorization':f'Bearer {get_twitch_access_token()}',
        'Client-Id': 'de0st9nif0zdqgdcue9vgyuvkp0ys8'
    }
    response = requests.post(url, headers=headers)
    print(response.status_code)
    print(response.json())
    data = response.json()
    return data

def fetch_game_engine() :
    url = get.Api_url_2.URL_fetch_GAME_ENGINE
    headers = {
        'Authorization':f'Bearer {get_twitch_access_token()}',
        'Client-Id': 'de0st9nif0zdqgdcue9vgyuvkp0ys8'
    }
    response = requests.post(url, headers=headers,data = 'fields checksum,companies,name,platforms,slug;limit 500;')
    print(response.status_code)
    print(response.json())
    data = response.json()
    return data

def fetch_game_mode() :
    url = get.Api_url_2.URL_fetch_GAME_MODES
    headers = {
        'Authorization':f'Bearer {get_twitch_access_token()}',
        'Client-Id': 'de0st9nif0zdqgdcue9vgyuvkp0ys8'
    }
    response = requests.post(url, headers=headers,data = 'fields checksum,name,slug;limit 500;')
    print(response.status_code)
    print(response.json())
    data = response.json()
    return data

def fetch_game_genre() :
    url = get.Api_url_2.URL_fetch_GAME_GENRES
    headers = {
        'Authorization':f'Bearer {get_twitch_access_token()}',
        'Client-Id': 'de0st9nif0zdqgdcue9vgyuvkp0ys8'
    }
    response = requests.post(url, headers=headers,data = 'fields checksum,name,slug;limit 500;')
    print(response.status_code)
    print(response.json())
    data = response.json()
    return data

def fetch_game_language() :
    url = get.Api_url_2.URL_fetch_GAME_LANGUAGE
    with open('datalake/raw/Jeu/jeu/info/response.json', 'r') as file:
        top_games = json.load(file)
    all_game = set()
    for i in top_games:
        try:
            for j in i['language_supports']:
                print(j)
                all_game.add(j)
        except:
            print("no platforms")
    headers = {
        'Authorization':f'Bearer {get_twitch_access_token()}',
        'Client-Id': 'de0st9nif0zdqgdcue9vgyuvkp0ys8'
    }
    response = requests.post(url, headers=headers,data = 'fields checksum,game,language,language_support_type; where  ;limit 500;')
    print(response.status_code)
    print(response.json())
    data = response.json()
    return data

def fetch_game_langue() :
    url = get.Api_url_2.URL_fetch_GAME_LANGUE
    headers = {
        'Authorization':f'Bearer {get_twitch_access_token()}',
        'Client-Id': 'de0st9nif0zdqgdcue9vgyuvkp0ys8'
    }
    response = requests.post(url, headers=headers,data = 'fields checksum,locale,name,native_name;limit 500;')
    print(response.status_code)
    print(response.json())
    data = response.json()
    return data

def fetch_game_plateform() :
    url = get.Api_url_2.URL_fetch_GAME_PLATEFORM
    headers = {
        'Authorization':f'Bearer {get_twitch_access_token()}',
        'Client-Id': 'de0st9nif0zdqgdcue9vgyuvkp0ys8'
    }
    with open('datalake/raw/Jeu/jeu/info/response.json', 'r') as file:
        top_games = json.load(file)
    # Liste pour stocker les résultats
    all_game = set()
    for i in top_games:
        try:
            for j in i['platforms']:
                print(j)
                all_game.add(j)
        except:
            print("no platforms")
        

    print(all_game)
    response = requests.post(url, headers=headers,data = 'fields abbreviation,alternative_name,category,checksum,generation,name,platform_family,platform_logo,slug;limit 500; where id = (' + ','.join(map(str, all_game)) + ');')
    print(response.status_code)
    print(response.json()) 

    for i in response.json():
        print("hello")
        print(i)
        try:   
            if i['category'] == 1:
                i['category'] = 'Console'
            elif i['category'] == 2:
                i['category'] = 'Arcade'
            elif i['category'] == 3:
                i['category'] = 'Platform'
            elif i['category'] == 4:
                i['category'] = 'Operating System'
            elif i['category'] == 5:
                i['category'] = 'Portable Console'
            elif i['category'] == 6:
                i['category'] = 'Computer'
            else:
                i['category'] = 'Other'
        except:
            print("no category")
    print(response.json())
    data = response.json()
    return data

def fetch_game_theme() :
    url = get.Api_url_2.URL_fetch_GAME_THEME
    headers = {
        'Authorization':f'Bearer {get_twitch_access_token()}',
        'Client-Id': 'de0st9nif0zdqgdcue9vgyuvkp0ys8'
    }
    response = requests.post(url, headers=headers,data = 'fields checksum,name,slug;limit 500;')
    print(response.status_code)
    print(response.json())
    data = response.json()
    return data

def fetch_game_loca() :
    url = get.Api_url_2.URL_fetch_GAME_LOCA
    headers = {
        'Authorization':f'Bearer {get_twitch_access_token()}',
        'Client-Id': 'de0st9nif0zdqgdcue9vgyuvkp0ys8'
    }
    response = requests.post(url, headers=headers,data = 'fields checksum,game,name,region;limit 500;')
    print(response.status_code)
    print(response.json())
    data = response.json()
    return data