from flask import Flask
from flask_cors import CORS
from routes.chat_routes import chat_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(chat_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="127.0.0.1", port=5000, debug=True)
