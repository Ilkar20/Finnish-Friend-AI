from flask import current_app

# import builder and client (client is created at runtime to allow mocking)
from src.ai.prompt_builder import build_prompt
from src.ai.ollama_client import OllamaClient
import json
import re

class TutorService:
    def __init__(self, ollama_client=None):
        self.ollama_client = ollama_client  # allow injection for tests
        self.model_name = current_app.config.get("MODEL_NAME", "llama3") if current_app else "llama3"

    def _get_client(self):
        if self.ollama_client:
            return self.ollama_client
        # Lazy import of current_app to avoid circular import at module load
        return OllamaClient()

    def parse_model_text(self, text):
        """
        Try to extract correction and explanation heuristically from model text.
        For MVP keep it simple: look for 'Correction:' and 'Explanation:' markers.
        """
        correction = None
        explanation = None

        # naive search
        corr_match = re.search(r"Correction[:\s]+(['\"]?)(.+?)\\1(?:\\.|$)", text)
        if corr_match:
            correction = corr_match.group(2).strip()
        else:
            # look for "Correction: X" without quotes
            m = re.search(r"Correction[:\s]+(.+?)(?:\n|$)", text)
            if m:
                correction = m.group(1).strip()

        expl_match = re.search(r"Explanation[:\s]+(.+?)(?:\n|$)", text)
        if expl_match:
            explanation = expl_match.group(1).strip()

        # fallback: put full text as reply
        return {
            "reply": text.strip(),
            "correction": correction,
            "explanation": explanation,
            "alternatives": [],
            "difficulty": "beginner"
        }

    def handle_message(self, message, history=None):
        prompt = build_prompt(message, history=history)
        client = self._get_client()

        # If client is a simple mock object, its generate method will be used.
        model_resp = client.generate(self.model_name, prompt, stream=False)

        text = model_resp.get("text", "") if isinstance(model_resp, dict) else str(model_resp)
        parsed = self.parse_model_text(text)
        # attach raw for debugging
        parsed["raw_ollama"] = model_resp
        return parsed
