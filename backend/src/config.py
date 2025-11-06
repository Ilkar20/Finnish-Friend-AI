import os

class DefaultConfig:
    OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
    MODEL_NAME = os.getenv("MODEL_NAME", "llama3")
    # small defaults for MVP
    OLLAMA_TIMEOUT = int(os.getenv("OLLAMA_TIMEOUT", "20"))
    MAX_CONTEXT_TURNS = int(os.getenv("MAX_CONTEXT_TURNS", "6"))
