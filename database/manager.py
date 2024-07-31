import sqlite3
from hashlib import sha256

class ConnectDatabase:
    def __init__(self):
        self.db = sqlite3.connect("./database/database.db", check_same_thread=False)
        self.cursor = self.db.cursor()
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Clients(
                            id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
                            name TEXT UNIQUE NOT NULL, 
                            email TEXT UNIQUE NOT NULL, 
                            password TEXT NOT NULL, 
                            cash REAL DEFAULT 150)""")
    
    #login na conta do cliente
    def login(self, data):
        password = sha256(data.get("password").encode()).hexdigest()
        client = self.cursor.execute(f"""SELECT * FROM Clients
                            WHERE email = "{str(data.get('email'))}"
                            """).fetchall()
        if len(client) > 0:
            if client[0][3] == password:
                data = {
                    "result": "Success",
                    "id": client[0][0],
                    "name": client[0][1],
                    "email": client[0][2],
                    "password": password,
                    "cash": client[0][4]
                }
                return data
            else:
                return {"result": "ErrorPassword"}
        
        else:
            return {"result": "Error"}
    
    
    #cria um cliente e adiciona-o no banco de dados
    def create_client(self, data):
        password = sha256(data.get("password").encode()).hexdigest()
        try:
            self.cursor.execute(f"""INSERT INTO Clients(
                                 name, email, password)
                                 VALUES(
                                    "{str(data.get('name'))}",
                                    "{str(data.get('email'))}",
                                    "{str(password)}")""")
            self.db.commit()
            return {"result": "Success"}
            
        except:
            check = self.cursor.execute(f"""SELECT name FROM Clients
                                WHERE name = "{str(data.get('name'))}"
                                """).fetchall()
                                
            if len(check) > 0:
                return {"result": "ErrorUsernameExist"}
            else:
                check = self.cursor.execute(f"""SELECT email FROM Clients
                                WHERE email = "{str(data.get('email'))}"
                                """).fetchall()
                                
                if len(check) > 0:
                    return {"result": "ErrorEmail"}
                else:
                    return {"result": "Error"}
        
    
    #retorna os dados do cliente
    def return_client(self, id, password):
        client = self.cursor.execute(f"""SELECT * FROM Clients
                            WHERE id = {int(id)}
                            AND password = '{str(password)}'""").fetchall()
        
        if len(client) > 0:
            data = {
                "result": "Success",
                "id": client[0][0],
                "name": client[0][1],
                "email": client[0][2],
                "cash": client[0][4]
            }
            
            return data
        else:
            return {"result": "Error"}
            
            
    #atualiza o saldo do usuário
    def update_cash(self, id, cash):
        self.cursor.execute(f"""UPDATE Clients
                            SET cash = {float(cash)}
                            WHERE id = {int(id)}""")
        self.db.commit()