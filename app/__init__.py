from flask import Flask

from app.config import Config


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.blueprints.auth.routes import auth_bp
    from app.blueprints.children.routes import children_bp
    from app.blueprints.dashboard.routes import dashboard_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(children_bp)
    app.register_blueprint(dashboard_bp)

    @app.get("/health")
    def health():
        return {"status": "online", "message": "Stuntfree API is running"}

    return app
