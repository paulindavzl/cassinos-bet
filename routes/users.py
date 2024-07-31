from flask import Blueprint, render_template, request, make_response, url_for, redirect
import requests
from core import utils

users_routes = Blueprint("users_routes", __name__)

# gerencia os cookies (cria/obtém/exclui)
@users_routes.route("/cookies", methods=["GET", "POST", "DELETE"])
def manager_cookies():
    method = request.method #obtém o método de requisição
    # caso o método seja POST
    if method == "POST":
        data = request.json
        
        cookies = make_response({"result": "Success"})
        #cookies.set_cookie("login_key", data.get("key"))
#        cookies.set_cookie("status_account", "Connected")
        
    #caso seja DELETE
    elif method == "DELETE":
        cookies = make_response({"result": "Success"})
        cookies.set_cookie("login_key", "")
        cookies.set_cookie("status_account", "")
        
    # caso seja GET
    else:
        cookies = request.cookies
        
    return cookies


# gerencia o login do usuário
@users_routes.route("/login", methods=["GET", "POST"])
def login():
    method = request.method
    url_root = request.url_root
    
    if method == "GET":
        verify = utils.is_connected(url_root)
        connected = verify.get("result")
        
        if connected != False and connected.get("account") == True:
            return redirect("{{ url_for('game_routes.home_game') }}")
                
        # caso não tenha sucesso ao fazer login automaticamente
        url_login_post = f"{url_root}user/login"
        return render_template("user/login.html", 
            URL_POST_LOGIN = url_login_post)
    
    # caso o método seja POST
    else:
        data = request.json
        
        # tenta fazer login com os dados recebidos
        try_login = utils.try_login(data, url_root)
        try_login["url_game"] = f"{url_root}game/"
        return try_login
        

# gerencia o registro do usuário
@users_routes.route("/register", methods=["GET", "POST"])
def register():
    method = request.method
    url = request.url_root
    
    if method == "GET":
        user_account = requests.get(f"{url}/user/cookies").json()
        
        # tenta fazer login automaticamente
        if user_account.get("key") != "":
            verify = utils.decode_key(user_account.get("key"), url)
            
            if verify.get("result") == "Success":
                return url_for("game_routes.start_game")
                
        return render_template("user/register.html")
        
    # caso o método seja POST
    else:
        data = request.json
        return {"result": "Success"}
        