import json
import pandas as pd

with open('datalake/raw/Twitch/game/top1000games/response.json', 'r') as file:
        top_games = json.load(file)
with open('datalake/raw/Jeu/jeu/info/response.json', 'r') as file:
        game_info = json.load(file)
with open('datalake/raw/Twitch/game/topStreamTopGame/response.json', 'r') as file:
        top_stream = json.load(file)



# Conversion en DataFrame
top_games_df = pd.DataFrame.from_dict(top_games)
game_info_df = pd.DataFrame.from_dict(game_info)
top_stream_df = pd.DataFrame.from_dict(top_stream)


class Game:
    def __init__(self, id,igdb_id, game_name,ag_rating,first_release_date,game_engines,
                game_modes,genres, platforms, rating,
                rating_count,themes,viewer_count, ):
        self.id = id
        self.igdb_id = igdb_id
        self.name = game_name
        self.ag_rating=ag_rating
        self.first_release_date=first_release_date
        self.game_engines=game_engines
        self.game_modes=game_modes
        self.genres=genres
        self.platforms=platforms
        self.rating=rating
        self.rating_count=rating_count
        self.themes=themes
        self.viewer_count = viewer_count
    def to_dict(self):
        return {
            "id": self.id,
            "igdb_id": self.igdb_id,
            "name": self.name,
            "ag_rating": self.ag_rating,
            "first_release_date": self.first_release_date,
            "game_engines": self._convert_to_native(self.game_engines),
            "game_modes": self._convert_to_native(self.game_modes),
            "genres": self._convert_to_native(self.genres),
            "platforms": self._convert_to_native(self.platforms),
            "rating": self.rating,
            "rating_count": self.rating_count,
            "themes": self._convert_to_native(self.themes),
            "viewer_count": self.viewer_count
        }
    def _convert_to_native(self, value):
        if isinstance(value, pd.Series):
            return value.tolist()
        return value
    def __repr__(self):
        return self.__str__()

       


game=[]
stream=[]

for i in top_games_df.to_dict('records') :
    print("top_games_df") 
    print(i)

    if (i['igdb_id'] == ''):
         continue
    igpd_id  = int(i['igdb_id'])
    game_id  = int(i['id'])
    game_in = game_info_df.loc[game_info_df.where(game_info_df['id'] == igpd_id)]

    if game_in.empty:
        continue
    print("game_info_df")
    print(game_in)
    stream_in = top_stream_df.where(top_stream_df['game_id'] == game_id)
    print("top_stream_df")
    print(stream_in)
    g = Game(
           i['id']
           ,i['igdb_id']
           ,i['name']
           ,game_info_df['aggregated_rating']
           ,game_info_df['first_release_date']
           ,game_info_df['game_engines']
           ,game_info_df['game_modes']
           ,game_info_df['genres']
           ,game_info_df['platforms']
           ,game_info_df['rating']
           ,game_info_df['rating_count']
           ,game_info_df['themes']
           ,sum(top_stream_df['viewer_count']))
    print("game")
    game_json = json.dumps(g.to_dict(), indent=4)
    print(game_json)
    break
    