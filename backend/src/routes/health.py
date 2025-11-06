from flask import Blueprint, jsonify, current_app
bp = Blueprint("health", __name__)

@bp.route("/ready", methods=["GET"])
def ready():
    # Simple readiness check — in MVP just return ok.
    return jsonify({"status": "ok", "service": "finnish-friend-ai"}), 200

@bp.route("/live", methods=["GET"])
def live():
    return jsonify({"live": True}), 200
