import manager as db


#entra na conta do cliente automaticamente (somente pelo terminal)
def check_login():
    try:
        with open("account.txt", "r+") as connect:
            if connect.read() != "False":
                id = int(connect.read()[:4])
                password = str(connect.read()[4:])
                client = db.return_client(id, password)
                
                if client.get("result") == "Success":
                    return client
                else:
                    connect.write("False")
                    return {"result": "ErrorLogin"}
            else:
                connect.write("False")
                return {"result": "ErrorLogin"}
            
    except Exception as e:
        print(e)
        with open("account.txt", "w") as connect:
            connect.write("False")
            return {"result": "ErrorLogin"}


#salva o login no dispositivo (somente pelo terminal)
def save_login(id, password):
    with open("account.txt", "w") as connect:
        data = f"{id}{password}"
        connect.write(str(data))
        

#cria uma conta para o cliente
def register(data):
    if 22 >= data.get("name") >= 4:
        if "@" in data.get("email") and ".com" in data.get("email"):
            if 12 >= len(data.get("password")) >= 6:
                account = db.create_client(data)
                return account
            else:
                return {"result": "ErrorPassword"}
        else:
            return {"result": "ErrorTypeEmail"}
    else:
        return {"result": "ErrorSizeName"}
        
        
#entra na conta do cliente manualmente
def login(data):
    connect = db.login(data)
    if connect.get("result") == "Success":
        save_login(connect.get("id"), connect.get("password"))
        
    return connect
    
    
data = {
    "email": "paulin@gmail.com",
    "password": "paulo123"
}

print(login(data))
print(check_login())