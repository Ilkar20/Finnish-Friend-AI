from flask import Blueprint, request, jsonify
from services.ollama_service import query_ollama
from config.settings import SYSTEM_PROMPT

chat_bp = Blueprint("chat_bp", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    """
    Chat endpoint: Receives user input, sends it to the AI model, and returns a response.
    """
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    # Combine system prompt with user input
    full_prompt = f"{SYSTEM_PROMPT}\nUser: {user_message}\nAI:"

    ai_response = query_ollama(full_prompt)
    return jsonify({"reply": ai_response})
