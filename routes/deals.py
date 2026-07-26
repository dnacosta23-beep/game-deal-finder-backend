import requests
from flask import Blueprint, request

from services.cheapshark import search_deals


deals_bp = Blueprint("deals", __name__)


@deals_bp.route("/api/deals", methods=["GET"])
def get_deals():
    game_title = request.args.get("title", "")

    if not game_title:
        return {
            "error": "Please provide a game title."
        }, 400

    try:
        deals = search_deals(game_title)
        return deals

    except requests.RequestException as error:
        print(error)

        return {
            "error": "Failed to fetch deals from CheapShark.",
            "details": str(error)
        }, 502