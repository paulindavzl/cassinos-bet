import database.manager as manager

class ConnectAccount:
    def __init__(self):
        self.db = manager.ConnectDatabase()
        self.key = "./database/account.txt"
        
    #entra na conta do cliente automaticamente (somente pelo terminal)
    def check_login(self):
        try:
            with open(self.key, "r+") as connect:
                key = connect.read()
                if connect.read() != "False":
                    
                    id = ""
                    position = 0
                    for item in key:
                        if item != "-":
                            id = f"{id}{item}"
                            position += 1
                        else:
                            break
                            
                    password = str(key[position + 1:])
                    client = self.db.return_client(int(id), password)
                    
                    if client.get("result") == "Success":
                        return client
                    else:
                        connect.write("False")
                        return {"result": "ErrorLogin"}
                else:
                    connect.write("False")
                    return {"result": "ErrorLogin"}
                
        except:
            with open(self.key, "w") as connect:
                connect.write("False")
                return {"result": "ErrorLogin"}
    
    
    #salva o login no dispositivo (somente pelo terminal)
    def save_login(self, id, password):
        with open(self.key, "w") as connect:
            data = f"{id}-{password}"
            connect.write(str(data))
            
    
    #entra na conta do cliente manualmente
    def login(self, data, web = False):
        connect = self.db.login(data)
        if connect.get("result") == "Success" and web == False:
            self.save_login(connect.get("id"), connect.get("password"))
            
        return connect
    
    
    #sai da conta do cliente
    def exit(self):
        with open(self.key, "w") as connect:
            connect.write("False")
    
    
    #cria uma conta para o cliente
    def register(self, data, web = False):
        if 22 >= len(data.get("name")) >= 4:
            if data.get("email") != None and "@" in data.get("email") and ".com" in data.get("email"):
                if 12 >= len(data.get("password")) >= 6:
                    
                    data["name"] = data["name"].title()
                    account = self.db.create_client(data)
                    if account.get("result") == "Success":
                        connect_account = self.login(data, web)
                        return connect_account
                    else:
                        return account
                        
                else:
                    return {"result": "ErrorPassword"}
            else:
                return {"result": "ErrorEmailType"}
        else:
            return {"result": "ErrorUsernameSize"}
             
             
    #atualiza o saldo do usuário no banco de dados
    def update_cash(self, id, cash):
        self.db.update_cash(id, cash)