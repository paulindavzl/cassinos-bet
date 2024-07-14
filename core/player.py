class Player:
    def __init__(self, name):
        self.__name = name
        self.__cash = 150.00
    
    #retorna os dados do usuário
    def returnData(self):
        return self.__name, self.__cash
        
    #verifica se o saldo é suficiente para apostar
    def toBet(self, bet):
        if bet <= self.__cash:
            self.__cash -= bet
            return True
        else:
            return False
                  
    #adiciona o ganhos das apostas ao saldo
    def win(self, money):
        self.__cash += money
    
    
    #adiciona mais dinheiro na conta do usuário
    def deposit(self, value):
        self.__cash += value