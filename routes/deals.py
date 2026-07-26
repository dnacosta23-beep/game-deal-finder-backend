import requests
from flask import Blueprint, request

from services.cheapshark import search_deals, get_stores


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
        stores = get_stores()

        formatted_deals = []

        for deal in deals:
            formatted_deals.append({
                "title": deal["title"],
                "sale_price": float(deal["salePrice"]),
                "normal_price": float(deal["normalPrice"]),
                "savings": round(float(deal["savings"])),
                "store": stores.get(deal["storeID"], "Unknown Store"),
                "thumb": deal["thumb"],
                "deal_url": (
                    "https://www.cheapshark.com/redirect"
                    f"?dealID={deal['dealID']}"
                ),
            })

        return formatted_deals

    except requests.RequestException as error:
        return {
            "error": "Failed to fetch deals from CheapShark.",
            "details": str(error)
        }, 502