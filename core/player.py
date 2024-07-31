class Player:
    def __init__(self, id = None, name = None, cash = 0.0, status = "Disconnected"):
        self.__id = id
        self.__name = name
        self.__cash = cash
        self.status = status
        
    #cria um player
    def insertPlayer(self, data):
        self.__id = data.get("id")
        self.__name = data.get("name")
        self.__cash = data.get("cash")
        self.status = "Connected"
    
    #retorna os dados do usuário
    def returnData(self, web = False):
        if web:
            data = {
                "id": self.__id,
                "name": self.__name,
                "cash": self.__cash,
                "status": self.status
            }
            return data
        else:
            return self.__name, self.__cash, self.status
        
    #verifica se o saldo é suficiente para apostar
    def toBet(self, bet, account):
        if bet <= self.__cash:
            self.__cash -= bet
            account.update_cash(self.__id, self.__cash)
            return True
        else:
            return False
                  
    #adiciona o ganhos das apostas ao saldo
    def win(self, money, account):
        self.__cash += money
        account.update_cash(self.__id, self.__cash)
    
    
    #adiciona mais dinheiro na conta do usuário
    def deposit(self, value):
        self.__cash += value