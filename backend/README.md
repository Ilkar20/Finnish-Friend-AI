# 🇫🇮 Finnish Friend AI – Backend

## 🧠 Overview
The backend powers the AI interactions for the Finnish Friend AI application. It builds prompts, communicates with the LLM via Ollama, and exposes API endpoints for the frontend.

**Tech Stack:**
- **Framework:** Flask
- **AI Service:** Ollama with Llama 3

**Core Responsibilities:**
- 🧱 Build AI prompts (`prompt_builder`)
- 🤖 Handle AI requests (`TutorService`)
- 🌐 Expose endpoints (`/api/chat`, `/health`)

---

## 📦 Requirements

- Python 3.10+
- pip
- Ollama (for running the LLM locally)

---

## ⚙️ Setup Instructions

### 1. Create and activate a virtual environment

```bash
python -m venv .venv

# For Linux/macOS:
source .venv/bin/activate

# For Windows:
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Pull the AI model via Ollama

```bash
ollama pull llama3
```

---

## 🚀 Running the Backend

Start the Flask server:

```bash
python src/main.py
```

The server will run at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### 🔌 API Endpoints

| Endpoint     | Method | Description                |
|--------------|--------|----------------------------|
| `/api/chat`  | POST   | Send message, get AI reply |
| `/health`    | GET    | Health check               |

---

## 🧪 Running Tests

From the `backend/` directory:

```bash
pytest -q
```


