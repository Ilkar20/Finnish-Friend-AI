import requests
from config.settings import OLLAMA_API_URL, MODEL_NAME

def query_ollama(prompt):
    """
    Sends the prompt to the local Ollama model API and returns its response text.
    """
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip()
    except requests.exceptions.RequestException as e:
        print(f"[Error] Ollama connection failed: {e}")
        return "Sorry, I’m having trouble connecting to the AI service."
