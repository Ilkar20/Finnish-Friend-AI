from flask import Flask
from flask_cors import CORS

def create_app(config_object=None):
    app = Flask(__name__, instance_relative_config=False)
    # load defaults
    app.config.from_object("app.config.DefaultConfig")
    if config_object:
        app.config.update(config_object)

    CORS(app)  # dev friendly: allow frontend file:// or localhost

    # register blueprints
    from src.routes.chat import bp as health_bp
    from src.routes.health import bp as chat_bp

    app.register_blueprint(health_bp, url_prefix="/health")
    app.register_blueprint(chat_bp, url_prefix="/api")

    return app
