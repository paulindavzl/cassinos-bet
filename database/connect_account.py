import database.manager as db

#entra na conta do cliente automaticamente (somente pelo terminal)
def check_login():
    try:
        with open("./database/account.txt", "r+") as connect:
            key = connect.read()
            if connect.read() != "False":
                id = int(key[:4])
                password = str(key[4:])
                client = db.return_client(id, password)
                
                if client.get("result") == "Success":
                    return client
                else:
                    connect.write("False")
                    return {"result": "ErrorLogin"}
            else:
                connect.write("False")
                return {"result": "ErrorLogin"}
            
    except:
        with open("account.txt", "w") as connect:
            connect.write("False")
            return {"result": "ErrorLogin"}


#salva o login no dispositivo (somente pelo terminal)
def save_login(id, password):
    with open("./database/account.txt", "w") as connect:
        data = f"{id}{password}"
        connect.write(str(data))
        

#entra na conta do cliente manualmente
def login(data):
    connect = db.login(data)
    if connect.get("result") == "Success":
        save_login(connect.get("id"), connect.get("password"))
        
    return connect


#cria uma conta para o cliente
def register(data):
    if 22 >= len(data.get("name")) >= 4:
        if "@" in data.get("email") and ".com" in data.get("email"):
            if 12 >= len(data.get("password")) >= 6:
                
                account = db.create_client(data)
                if account.get("result") == "Success":
                    connect_account = login(data)
                    return connect_account
                else:
                    return account
                    
            else:
                return {"result": "ErrorPassword"}
        else:
            return {"result": "ErrorTypeEmail"}
    else:
        return {"result": "ErrorSizeName"}
         
         
#atualiza o saldo do usuário no banco de dados
def update_cash(id, cash):
    db.update_cash(id, cash)