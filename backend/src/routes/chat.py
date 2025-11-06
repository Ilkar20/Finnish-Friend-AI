from flask import Blueprint, request, jsonify, current_app
bp = Blueprint("chat", __name__)

from src.services.tutor_service import TutorService

tutor = TutorService()

@bp.route("/chat", methods=["POST"])
def chat():
    payload = request.get_json() or {}
    message = payload.get("message", "").strip()
    history = payload.get("history", [])  # optional list of prior turns
    if not message:
        return jsonify({"error": "message required"}), 400

    try:
        result = tutor.handle_message(message, history)
        return jsonify(result), 200
    except Exception as e:
        current_app.logger.exception("chat error")
        return jsonify({"error": "server error", "detail": str(e)}), 500
