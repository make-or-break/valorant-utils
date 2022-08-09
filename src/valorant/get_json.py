import json

import requests

from valorant.main import get_name
from valorant.main import get_puuid
from valorant.main import get_tag

# API documentation:
# https://docs.henrikdev.xyz/valorant.html

# we request a lot of different JSON api endpoints,
# so we make a function to get the response
# this reduces boilerplate code


def get_response(api_endpoint):
    """
    Get the response of a url.
    """

    response = requests.get("https://api.henrikdev.xyz/valorant/" + api_endpoint)

    if response.status_code == 200 and response.json()["status"] == 200:
        return response.json()
    else:
        return None


###############################################################################
# code related to getting player stats


def get_player_json(Username, Tagline):
    """
    Get the json data of a player.
    """

    api_endpoint = "v2/mmr/eu/" + Username + "/" + Tagline

    if (response := get_response(api_endpoint)) is None:
        return False

    if not get_name(response):
        return False

    if not get_tag(response):
        return False

    if not get_puuid(response):
        return False

    return response


def get_player_json_by_puuid(puuid):
    """
    Get the json data of a player by puuid.
    """

    api_endpoint = "v2/by-puuid/mmr/eu/" + puuid

    if (response := get_response(api_endpoint)) is None:
        return False

    if not get_name(response):
        return False

    if not get_tag(response):
        return False

    if not get_puuid(response):
        return False

    return response


###############################################################################
# code related to getting match history


def get_matches_json(Username, Tagline):
    """
    Get the last 5 matches that where played by this user
    """

    api_endpoint = "v3/matches/eu/" + Username + "/" + Tagline + "?filter=competitive"

    return get_response(api_endpoint)


def get_matches_json_by_puuid(puuid):
    """
    Get the last 5 matches that where played by this user
    """

    api_endpoint = "v3/by-puuid/matches/eu/" + puuid + "?filter=competitive"

    return get_response(api_endpoint)


###############################################################################
# code related to getting MMR history


def get_mmr_json(puuid):
    """
    Get the MMR history of a player.
    """

    api_endpoint = "v1/by-puuid/mmr-history/eu/" + puuid

    return get_response(api_endpoint)


###############################################################################
# code related to getting match stats


def get_match_json(matchid):
    """
    Get the match stats of a match.
    """

    api_endpoint = "v2/match/" + matchid

    return get_response(api_endpoint)


###############################################################################


if __name__ == "__main__":

    # libary is meant to be used as a module
    # so this is only used for testing
    matches = get_matches_json("MayNiklas", "Niki")

    print(matches)
