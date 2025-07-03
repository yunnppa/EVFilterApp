from flask import Flask

def create_app(): #applied SRP
    app = Flask(__name__)

    from app.views import main
    app.register_blueprint(main)

    return app
