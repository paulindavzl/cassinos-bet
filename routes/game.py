from flask import Blueprint, request, url_for, render_template, redirect
import requests
from core import utils

game_routes = Blueprint("game_routes", __name__)

@game_routes.route("/")
def home_game():
    url_root = request.url_root
    
    if is_connected(url_root).get("result"):
        return render_template("game/home-game.html")
        
    else:
        return redirect("{{ url_for(users_routes.login) }}")