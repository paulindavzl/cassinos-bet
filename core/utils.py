from database.connect_account import ConnectAccount
import requests
from hashlib import sha256

# criptografa a senha do usuário com SHA-256
def encrypt(password):
    hash_pass = sha256(password.encode()).hexdigest()
    return hash_pass

# decodifica a chave de login
def decode_key(key, url):
    return {"result": "Error"}
    
# verifica se os dados recebidos estão devidamente preenchidos
def analyze_data(data, received_by):
    email = data.get("email")
    password = data.get("password")
    
    if received_by == "login":
        if "@" not in email and ".com" not in email:
            return {"result": "ErrorEmailType"}
        elif 30 < len(email) < 11:
            return {"result": "ErrorEmailLen"}
        elif 16 < len(password) < 6:
            return {"resutl": "ErrorPassLen"}
        else:
            return {"result": "Success"}
            
            
# tenta fazer login com os dados do usuário
def try_login(data: dict, url: str):
    # verifica se os dados estão preenchidos
    resp_data = analyze_data(data, "login")
        
    if resp_data.get("result") == "Success":
        #tenta retornar os dados do usuário
        resp_account = ConnectAccount().login(data, True)
        
        if resp_account.get("result") == "Success":
            key = f"{resp_account.get('id')}-{resp_account.get('password')}"
            data_cookie = {
                "key": key
            }
            
            requests.post(f"{url}/user/cookies", json = data_cookie)
            return {"result": "Success"}
            
        else:
            return resp_account
    else:
        return resp_data
        
        
# verifica se o usuário já está conectado
def is_connected(url: str):
    req_url = f"{url}user/cookies"
    verify = requests.get(req_url).json()
    
    key = verify.get("key")
    if verify.get("status") == "Connected" and len(key) > 64:
        response = {
            "result": {"request_status": True},
            "key": verify.get("key")
        }
        
        if decode_key(key, url) == "Success":
            response["result"]["account"] == True
        else:
            response["result"]["account"] == False
            
        return response
    else:
        return {"result": False}
        