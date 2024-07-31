from flask import Flask
from routes.users import users_routes
from routes.game import game_routes

app = Flask(__name__)

app.register_blueprint(users_routes, url_prefix="/user")
app.register_blueprint(game_routes, url_prefix="/game")

if __name__ == "__main__":
    app.run()