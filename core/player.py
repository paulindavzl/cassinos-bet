class Player:
    def __init__(self, id, name, cash):
        self.__id = id
        self.__name = name
        self.__cash = cash
    
    #retorna os dados do usuário
    def returnData(self):
        return self.__name, self.__cash
        
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