from .const import *
from .Game import Game
from .Team import Team

import requests


def get_request(url):
    """
    Always make a GET request to get data.
    """
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        return {}


def query_player(id: str, season: str) -> list:
    url = PLAYER_URL.format(id)
    url += SEASON_TAG.format(season)

    jason = get_request(url)
    splits = [Game(id, game).stats for game in jason['stats'][0]['splits']]
    return splits


def query_player_list(id: str, season: str) -> list:
    url = TEAM_URL
    if id:
        url += "/{}".format(id)

    url += EXPAND_ROSTER
    url += SEASON_TAG.format(season)
    jason = get_request(url)

    team = [Team(t, season).players for t in jason['teams']]
    all_players = sum(team, []) # flatten out list
    return all_players
