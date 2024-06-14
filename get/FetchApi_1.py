import get.Api_url_1
import json
import requests



# Configuration des API
TWITCH_CLIENT_ID = get.Api_url_1.Client_ID
TWITCH_SECRET = get.Api_url_1.auth_key

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


# Récupérer les données des jeux depuis l'API Twitch
def get_twitch_games(first=100, max_games=1000):
    access_token = get_twitch_access_token(TWITCH_CLIENT_ID, TWITCH_SECRET)
    print(access_token)
    headers = {
        'Authorization':f'Bearer {access_token}',
        'Client-Id': 'de0st9nif0zdqgdcue9vgyuvkp0ys8'
        
    }
    games = []
    cursor = None
    pages = max_games // first

    for _ in range(pages):
        print("hello")
        url = get.Api_url_1.URL_fetch_Top_game
        params = {
            'first': first
        }
        if cursor:
            params['after'] = cursor
        print(url)
        response = requests.get(url, headers=headers, params=params)
        print(response)
        response.raise_for_status()
        data = response.json()
        games.extend(data['data'])
        cursor = data.get('pagination', {}).get('cursor')
        if not cursor:
            break

    return games



# Fonction pour obtenir les streams pour un jeu donné
def get_streams_for_game(game_id,  first=50):
    access_token = get_twitch_access_token(TWITCH_CLIENT_ID, TWITCH_SECRET)
    url = get.Api_url_1.URL_fetch_Top_stream
    headers = {
        'Authorization':f'Bearer {access_token}',
        'Client-Id': 'de0st9nif0zdqgdcue9vgyuvkp0ys8'
        
    }
    params = {
        'game_id': game_id,
        'first': first
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()['data']

def fetch_stream_per_game():

    # Lire le fichier JSON pour obtenir la liste des jeux
    with open('datalake/raw/Twitch/game/top1000games/response.json', 'r') as file:
        top_games = json.load(file)
    # Liste pour stocker les résultats
    all_streams = []

    # Récupérer les 50 streams pour chaque jeu
    for game in top_games:
        game_id = game['id']
        try:
            streams = get_streams_for_game(game_id)
            for stream in streams:
                all_streams.append({
                    'game_id': game_id,
                    'game_name': game['name'],
                    'stream_id': stream['id'],
                    'user_id': stream['user_id'],
                    'user_name': stream['user_name'],
                    'viewer_count': stream['viewer_count'],
                    'started_at': stream['started_at'],
                    'language': stream['language'],
                    'thumbnail_url': stream['thumbnail_url']
                })
            print(f"Successfully retrieved streams for game {game['name']}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to retrieve streams for game {game['name']}: {e}")

    # Enregistrer les résultats dans un fichier JSON
    with open('top_1000_games_streams.json', 'w') as file:
        json.dump(all_streams, file, indent=4)

    print("Les données des streams ont été enregistrées dans 'top_1000_games_streams.json'")


    print("Les données des jeux ont été enregistrées dans 'top_1000_games.json'")



def fetch() : 
    url = get_twitch_games()
    response = requests.get(url)
    print(response.status_code)
    data = response.json()
    return data

def fetch_plateforme() :
    url = get.Api_url_1.URL_fetch_plateform 
    return url

