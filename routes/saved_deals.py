from flask import Blueprint, request
from services.supabase_client import supabase


saved_deals_bp = Blueprint( "saved_deals", __name__, )


@saved_deals_bp.route("/api/saved-deals", methods=["POST"])
def create_saved_deal():
    deal_data = request.get_json()

    # Stop if the request did not include any deal data.
    if not deal_data:
        return {"error": "Deal data is required"}, 400

    # Stop if the deal does not have a store link.
    if not deal_data.get("deal_url"):
        return {"error": "Deal URL is required"}, 400

    try:
        existing_deal = (
            supabase
            .table("saved_deals")
            .select("id")
            .eq("deal_url", deal_data["deal_url"])
            .execute()
        )

        # If a matching row was found, do not save a duplicate.
        if existing_deal.data:
            return {"error": "This deal is already saved"}, 409

        response = (
            supabase
            .table("saved_deals")
            .insert(deal_data)
            .execute()
        )

        return response.data[0], 201

    except Exception:
        return {"error": "Unable to save deal"}, 500



@saved_deals_bp.route("/api/saved-deals", methods=["GET"])
def get_saved_deals():
    try:
       
        response = (
            supabase
            .table("saved_deals")
            .select("*")
            .order("created_at", desc=True)
            .execute()
        )

        return response.data

    except Exception:
        return {"error": "Unable to retrieve saved deals"}, 500


# DELETE: Remove one saved deal using its database id.
@saved_deals_bp.route( "/api/saved-deals/<int:deal_id>", methods=["DELETE"], )
def delete_saved_deal(deal_id):
    try:
        response = (
            supabase
            .table("saved_deals")
            .delete()
            .eq("id", deal_id)
            .execute()
        )
        
        if not response.data:
            return {"error": "Saved deal not found"}, 404

        return {"message": "Saved deal deleted successfully"}, 200

    except Exception:
        return {"error": "Unable to delete saved deal"}, 500