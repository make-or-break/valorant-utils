import time

import valorant.data as data


def current_season():
    """
    Returns the current season.
    Data is pulles drom the data.py file.
    """

    for season in data.COMPETETIVE_SEASONS:

        start = time.mktime(
            time.strptime(
                data.COMPETETIVE_SEASONS[season]["start"], "%Y-%m-%dT%H:%M:%SZ"
            )
        )

        end = time.mktime(
            time.strptime(data.COMPETETIVE_SEASONS[season]["end"], "%Y-%m-%dT%H:%M:%SZ")
        )

        if time.time() > start and time.time() < end:
            return (
                season,
                data.COMPETETIVE_SEASONS[(season)]["name"],
                time.mktime(
                    time.strptime(
                        data.COMPETETIVE_SEASONS[(season)]["end"], "%Y-%m-%dT%H:%M:%SZ"
                    )
                ),
            )

    # if no season is found, return None
    return None


def act_end():
    """
    Returns remaining seconds of this act.
    """

    season, name, act_end = current_season()

    return act_end - time.time()


if __name__ == "__main__":

    print(current_season())
    print(act_end() / 60 / 60)
