import datetime
import json

import requests

from valorant.get_json import *


# convert time
def milliseconds_to_time(milliseconds):
    """
    Convert milliseconds to time.
    """

    seconds = milliseconds // 1000
    minutes = seconds // 60
    seconds = seconds % 60
    return "%d:%02d" % (minutes, seconds)


###############################################################################
# code related to getting player stats


def get_elo(data: json):
    """
    Get the elo of a player.
    """

    if not data:
        return False

    return data["data"]["current_data"]["elo"]


def get_rank(data: json):
    """
    Get the rank of a player.
    """

    if not data:
        return False

    return data["data"]["current_data"]["currenttierpatched"]


def get_rank_tier(data: json):
    """
    Get the rank tier of a player.
    """

    if not data:
        return False

    d = data["data"]["current_data"]["currenttier"]
    if not d:
        d = 0
    return d


def get_puuid(data: json):
    """
    Get the puuid of a player.
    """

    if not data:
        return False

    return data["data"]["puuid"]


def get_name(data: json):
    """
    Get the name of a player.
    """

    if not data:
        return False

    if (name := data["data"]["name"]) is None:
        return False

    return name


def get_tag(data: json):
    """
    Get the tagline of a player.
    """

    if not data:
        return False

    if (tag := data["data"]["tag"]) is None:
        return False

    return tag


###############################################################################
# code related to getting match history


def get_matchid(data):
    """
    Get the matchid of the last match.
    """

    return data["data"][0]["metadata"]["matchid"]


def get_match_ids(data):
    """
    Get the matchids of the last 5 matches.
    """

    ids = []
    for i in data["data"]:
        ids.append(i["metadata"]["matchid"])
    return ids


###############################################################################
# code related to getting MMR history


def get_mmr_change(data, date):
    """
    Get the MMR change of the last match.
    """

    for match in data["data"]:
        if match["date_raw"] == date:
            return match["mmr_change_to_last_game"]


def get_mmr_elo(data, date):
    """
    Get elo of player after the last match.
    """

    for match in data["data"]:
        if match["date_raw"] == date:
            return match["elo"]


###############################################################################
# code related to getting match stats


def get_match_metadata(data):
    """
    Get the metadata of a match
    """

    return data["data"]["metadata"]


def get_game_start(data):
    """
    Get the time of the start of the last match.
    """

    return data["data"]["metadata"]["game_start"]


def get_game_length(data):
    """
    Get the length of the last match (in milliseconds).
    """

    return data["data"]["metadata"]["game_length"]


def get_rounds_played(data):
    """
    Get the length of the last match (in rounds).
    """

    return data["data"]["metadata"]["rounds_played"]


def get_map(data):
    """
    Get the map of the last match.
    """

    return data["data"]["metadata"]["map"]


###############################################################################


if __name__ == "__main__":
    # libary is meant to be used as a module
    # so this is only used for testing
    matches = get_matches_json("MayNiklas", "Niki")

    for match in get_match_ids(matches):
        data = get_match_json(match)

        print(
            f"""
        Match started: {datetime.datetime.utcfromtimestamp(get_game_start(data))}
        Match length: {milliseconds_to_time(get_game_length(data))}
        Rounds played: {get_rounds_played(data)}
        Map: {get_map(data)}
        """
        )
