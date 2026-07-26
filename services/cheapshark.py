import requests


CHEAPSHARK_DEALS_URL = "https://www.cheapshark.com/api/1.0/deals"


def search_deals(game_title):
    parameters = {
        "title": game_title,
    }

    headers = {
        "User-Agent": "GameDealFinder/1.0"
    }

    response = requests.get(
        CHEAPSHARK_DEALS_URL,
        params=parameters,
        headers=headers,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()
