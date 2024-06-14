import get.FetchApi_2
import get.FetchApi_1
import format
import til
from datetime import date




def format_and_fetch(source,entity):
    data = get.FetchApi_2.fetch_game_language()
    current_day = date.today().strftime("%Y%m%d")
    til.store(True,source,entity,data)
    return
    format.convert_raw_to_formatted("response.json",source,entity)

format_and_fetch(2,6)

#get.FetchApi_1.get_twitch_access_token()