import requests
from flask import current_app

class OllamaClient:
    def __init__(self, url=None, timeout=None):
        self.url = url or current_app.config.get("OLLAMA_URL")
        self.timeout = timeout or current_app.config.get("OLLAMA_TIMEOUT", 20)

    def generate(self, model_name, prompt, stream=False, temperature=0.2, max_tokens=512):
        """
        Call Ollama's /api/generate endpoint and return normalized text.
        For MVP: non-streaming.
        """
        payload = {
            "model": model_name,
            "prompt": prompt,
            "stream": stream,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        resp = requests.post(self.url, json=payload, timeout=self.timeout)
        resp.raise_for_status()
        body = resp.json()
        # Ollama may return in different fields; try common ones:
        generated = body.get("text") or body.get("response") or body.get("output") or ""
        return {"raw": body, "text": generated}
