import time


def act_end():
    """
    Returns remaining hours of this act.
    """

    # Episode 5 Act I ends August 23rd 2022
    act_end = time.mktime(time.strptime("23/08/2022", "%d/%m/%Y"))

    diff = act_end - time.time()

    # convert to hours
    hours = diff / 60 / 60

    return hours


if __name__ == "__main__":
    print(act_end())
