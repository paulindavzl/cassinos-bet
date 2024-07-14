from core.game import Game, Sl
import os
import time as tm
from core.commands import Commands

class RenderGame():
    def __init__(self):
        
        #cores usadas no jogo
        self.color = {
            "y": "\033[33m",
            "r": "\033[31m",
            "g": "\033[32m",
            "w": "\033[37m"
        }
        #naipes das cartas
        self.__tokens = {
            "hearts": "♥",
            "swords": "♠",
            "golds": "♦",
            "woods": "♣",
            "wild": "🃏"
        }
        
        self.game = Game()
        self.cmd = Commands(self.color, self.game)
        
        self.__start()
        
        
    #recebe o nome do player
    def __start(self):
        os.system("clear")
        name = input(f"{self.color['y']}Informe seu nome (3 - 10 letras)\n>>{self.color['w']}").strip()
        
        if 10 >= len(name) >= 3:
            self.game.create_player(name.title())
            self.render_game(anim = True)
        elif len(name) == 0:
            print(f"{self.color['r']}Informe um nome por favor!{self.color['y']}")
            tm.sleep(3)
            self.__start()
        elif len(name) < 3:
            print(f"{self.color['r']}Este nome é muito curto!{self.color['y']}")
            tm.sleep(3)
            self.__start()
        else:
            print(f"{self.color['r']}Este nome é muito grande!{self.color['y']}")
            tm.sleep(3)
            self.__start()
            
    
    #renderiza o jogo
    def render_game(self, slots = Sl.default_slots, anim = False, big_win = False):
        os.system("clear")
        self.__show_info()
        
        if big_win != False:
            print(f"{self.color['g']}      GRANDE GANHO! {big_win}")
        
        #estiliza os slots
        def styler():
            slot = []
            for line in slots:
                new_line = []
                for item in line:
                    new_line.append((item[0], self.__tokens[item[1]]))
                slot.append(new_line)
                
            return slot
                
        #organiza os slots
        def organizer():
            slot = []
            for line in styler():
                column = 0
                new_line = []
                for item in line:
                    new_line.append(f"{line[column][0]}{line[column][1]}")
                    column += 1
                slot.append(new_line)
            return slot
            
        results = organizer()
        for line in results:
            if anim == False and big_win == False:
                tm.sleep(.1)
            elif big_win != False:
                tm.sleep(.5)
            print(f"\n              {line[0]}  {line[1]}  {line[2]}              ")
            
    
    #exibe informações importantes
    def __show_info(self):
            data_player = self.game.player.returnData()
            cash = float(f"{data_player[1]: .2f}")
            print(f"""{self.color['y']}=--==--==--=[ BARALHO's BET ]=--==--==--=
{'=--='*10}
--------------- Nome de usuário: {self.color['w']}{data_player[0]}{self.color['y']}
--------------- Saldo: {self.color['g']}{str(cash).replace(".", ",")}{self.color['y']}
----------Valor da aposta: {self.color['g']}{str(self.game.bet).replace(".", ",")} BetCoin(s){self.color['y']}
----------Turbo: {self.color['g']}{self.game_mode()}{self.color['y']}
-----{self.color['w']}/bet {self.color['y']}para alterar o valor da aposta
-----{self.color['w']}/put {self.color['y']}para depositar BetCoins
-----{self.color['w']}/wins {self.color['y']}para ver as formas de ganhar e seus pagamentos
-----{self.color['w']}/auto {self.color['y']}para giros automáticos
-----{self.color['w']}/turbo {self.color['y']}para ativar/desativar o modo turbo
{'=--='*10}""")

    
    #anima o sorteio dos slots
    def __animation(self):
       for i in range(self.game.mode()):
            slots = Sl.organizer_slots(anim = True)
            self.render_game(slots, anim = True)
            tm.sleep(.05)
            os.system("clear")
            
    
    #retorna o modo de jogo turbo on/off
    def game_mode(self):
        if self.game.turbo:
            return "ativado"
        else:
            return "desativado"
    
    
    #comeca o jogo
    def run(self):
            if self.game.player.toBet(self.game.bet) != False:
                self.__animation()
                results = self.game.run()
                self.render_game(results[0], big_win = results[1][2])
                
                if results[1][0] == True:
                    win = float(f"{results[1][1]: .2f}")
                    print(f"{self.color['g']}\nVocê ganhou +{self.game.bet + (self.game.bet * win): .2f}{self.color['y']}")
                    
                    if results[1][2] != False:
                        tm.sleep(1)
                    
            else:
                self.__animation()
                self.render_game(anim = True)
                cash = self.game.player.returnData()[1]
                
                if cash >= 1:
                    print(f"\n{self.color['r']}O valor da sua aposta é superior ao seu saldo!\n{self.color['y']}Abaixe a aposta para o minímo usando {self.color['w']}/bet min{self.color['y']} ou deposite usando {self.color['w']}/put{self.color['y']}")
                else:
                    print(f"\n{self.color['r']}Você não possui saldo suficiente para jogar!\n{self.color['y']}Deposite usando {self.color['w']}/put {self.color['y']}para continuar!")
                    
                return "ErrorCash"
        
        
#inicia o jogo ao rodar este arquivo como principal
if __name__ == "__main__":
    RD = RenderGame()
    
    def run_game():
        if RD.game.auto == False:
            RD.render_game(anim = True)
            command = input(f"{RD.color['y']}\n{'=--='*10}\nEnter para girar\n>>{RD.color['w']}")
            
            if len(command) >= 1:
                if command.strip()[0] == "/":
                    RD.cmd.identifier_commands(command)
                    run_game()
        
        else:
            RD.render_game(anim = True)
            print(f"\nGiros restantes: {RD.color['w']}{RD.game.auto}")
            input(f"{RD.color['y']}Enter para começar a girar\n")
            
        while True:
            if RD.game.auto == False:
                RD.run()
                command = input(f"{RD.color['y']}\n{'=--='*10}\nEnter para girar\n>>{RD.color['w']}")
            else:
                i = 0
                for spin in range(RD.game.auto):
                    if RD.run() != "ErrorCash":
                        i += 1
                        print(f"{RD.color['y']}\nGiros restantes: {RD.color['w']}{RD.game.auto - 1 - spin}{RD.color['y']}")
                        tm.sleep(.7)
                    else:
                        break
                
                print(f"Em {RD.color['g']}{i} giros de {RD.game.bet} {RD.color['y']}você ganhou: {RD.color['y']}{RD.game.wins: .2f} BetCoins")
                RD.game.auto = False
                RD.game.wins = 0
                command = input(f"\n{RD.color['y']}Enter para continuar\n>>")
                run_game()
            
            if len(command) >= 1:
                if command.strip()[0] == "/":
                    RD.cmd.identifier_commands(command)
                    run_game()
                    
    run_game()