import requests

CHEAPSHARK_DEALS_URL = "https://www.cheapshark.com/api/1.0/deals"
CHEAPSHARK_STORES_URL = "https://www.cheapshark.com/api/1.0/stores"

HEADERS = {
    "User-Agent": "GameDealFinder/1.0"
}

def search_deals(game_title):
    parameters = {
        "title": game_title,
    }


    response = requests.get(
        CHEAPSHARK_DEALS_URL,
        params=parameters,
        headers=HEADERS,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()


def get_stores():

    response = requests.get(
        CHEAPSHARK_STORES_URL,
        headers=HEADERS,
        timeout=10,
    )

    response.raise_for_status()

    return {
        store["storeID"]: store["storeName"]
        for store in response.json()
    }
