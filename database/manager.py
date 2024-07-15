import sqlite3
from hashlib import sha256

db = sqlite3.connect("./database/database.db")
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Clients(
                    id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL, 
                    email TEXT UNIQUE NOT NULL, 
                    password TEXT NOT NULL, 
                    cash REAL DEFAULT 150)""")

#login na conta do cliente
def login(data):
    password = sha256(data.get("password").encode()).hexdigest()
    client = cursor.execute(f"""SELECT * FROM Clients
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
def create_client(data):
    password = sha256(data.get("password").encode()).hexdigest()
    try:
        cursor.execute(f"""INSERT INTO Clients(
                             name, email, password)
                             VALUES(
                                "{str(data.get('name'))}",
                                "{str(data.get('email'))}",
                                "{str(password)}")""")
        db.commit()
        return {"result": "Success"}
        
    except:
        check = cursor.execute(f"""SELECT name FROM Clients
                            WHERE name = "{str(data.get('name'))}"
                            """).fetchall()
                            
        if len(check) > 0:
            return {"result": "ErrorUsername"}
        else:
            check = cursor.execute(f"""SELECT email FROM Clients
                            WHERE email = "{str(data.get('email'))}"
                            """).fetchall()
                            
            if len(check) > 0:
                return {"result": "ErrorEmail"}
            else:
                return {"result": "Error"}
    

#retorna os dados do cliente
def return_client(id, password):
    client = cursor.execute(f"""SELECT * FROM Clients
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
def update_cash(id, cash):
    cursor.execute(f"""UPDATE Clients
                        SET cash = {float(cash)}
                        WHERE id = {int(id)}""")
    db.commit()