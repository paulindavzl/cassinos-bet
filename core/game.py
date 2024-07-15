from core.slots import Slots
from core.player import Player

Sl = Slots()

class Game:
    def __init__(self):
        self.bet = 1.0
        self.turbo = False
        self.auto = False
        self.wins = 0
    
    
    #começa o jogo
    def run(self, account):
        slots = Sl.organizer_slots()
        result = self.__check_game(slots, account)
        return slots, result
        
        
    #cria o player
    def create_player(self, data):
        self.player = Player(data.get("id"), data.get("name"), data.get("cash"))
    
    
    #verifica se o resultado do jogo
    def __check_game(self, slots, account):
        result = Sl.check(slots)
        if result[0] == True:
            win = float(f"{result[1]: .2f}")
            self.player.win(self.bet + (self.bet * win), account)
            if self.auto != False:
                self.wins += self.bet + (self.bet * win)
        return result
          
        
    #altera o modo de jogo turbo/normal
    def mode(self, change = False):
        #apenas retorna valores de turbo on/off
        if change == False:
            if self.turbo == False:
                return 9
            else:
                return 3
                
        #altera o valor de turbo on/off
        else:
            if self.turbo == False:
                self.turbo = True
            else:
                self.turbo = False
        
        
    #altera o valor da aposta
    def new_bet(self, value):
        if 1000 >= value >= 1:
            self.bet = value
            return True
        elif value > 1000:
            return "ValueErrorMax"
        else:
            return "ValueErrorMin"
            
    
    #deposita dinheiro
    def deposit(self, value):
        if 1500 >= value >= 10:
            self.player.deposit(value)
        elif value > 1500:
            return "ValueErrorMax"
        else:
            return "ValueErrorMin"