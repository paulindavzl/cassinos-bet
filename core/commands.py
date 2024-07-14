#Este arquivo será usado apenas na renderização com Terminal
import os
import core.wins

class Commands:
    def __init__(self, color, game):
        self.color = color
        self.game = game
        
        
    #identifica os comandos
    def identifier_commands(self, cmd):
        if cmd[:4] == "/bet":
            if len(cmd.strip()) > 4:
                self.__command_bet(cmd[5:])
            else:
                self.__command_bet()
                
        elif cmd[:4] == "/put":
            if len(cmd.strip()) > 4:
                try:
                    self.__command_put(float(cmd[5:]))
                except:
                    self.__command_put()
            else:
                self.__command_put()
        
        elif "/wins" in cmd and len(cmd.strip()) == 5:
            core.wins.Wins(self.color)
            
        elif cmd[:5] == "/auto":
            self.__command_auto()
        
        elif "/turbo" in cmd and len(cmd.strip()) == 6:
            self.game.mode(True)
            if self.game.turbo:
                input(f"{self.color['g']}Modo turbo ativado{self.color['y']}\n")
            else:
                input(f"{self.color['g']}Modo turbo desativado{self.color['y']}\n")
            
        else:
            input(f"{self.color['r']}Comando {self.color['w']}{cmd} {self.color['r']}inválido!{self.color['y']}\n")
            
                
    #comando para alterar o valor da aposta
    def __command_bet(self, cmd = False):
        #retorna possíveis erros
        def bet_result(vlr):
            result = self.game.new_bet(vlr)
            
            if result == "ValueErrorMin":
                input(f"{self.color['r']}Valor muito baixo! {self.color['y']}Mín: 1 BetCoin\n")
            elif result == "ValueErrorMax":
                input(f"{self.color['r']}Valor muito alto! {self.color['y']}Máx: 1000 BetCoins\n")
            else:
                input(f"{self.color['g']}Você alterou o valor da aposta para {vlr} BetCoin(s) com sucesso!{self.color['y']}\n")
            
        if cmd == False:
            value = input(f"{self.color['y']}Informe o novo valor da aposta (1 - 1000)\n{self.color['w']}/cancel {self.color['y']}para cancelar!\n>>{self.color['w']}").replace(",", ".")
            
            try:
                value = float(value)
                bet_result(value)
                    
            except:
                if value == "/cancel":
                    input(f"{self.color['w']}/bet {self.color['y']}cancelado!\n")
                elif value == "min":
                    bet_result(1.0)
                elif value == "max":
                    bet_result(1000.0)
                else:
                    return "ValueError"
        
        else:
            try:
                bet_result(float(cmd))
            except:
                if cmd == "min":
                    bet_result(1.0)
                elif cmd == "max":
                    vlr = float(f"{self.game.player.returnData()[1]: .2f}")
                    bet_result(vlr)
                    
                else:
                    input(f"{self.color['r']}Comando inválido!\n{self.color['w']}{cmd} {self.color['y']}não é um comando válido de {self.color['w']}/bet{self.color['y']}!\n")
            
            
    #comando para depositos
    def __command_put(self, cmd = False):
        #retorna possíveis erros
        def put_result(value):
            result = self.game.deposit(value)
            
            if result == "ValueErrorMin":
                input(f"{self.color['r']}Valor muito baixo! {self.color['y']}Mín: 10 reais\n")
            elif result == "ValueErrorMax":
                input(f"{self.color['r']}Valor muito alto! {self.color['y']}Máx: 1500 reais\n")
            else:
                input(f"{self.color['g']}Você depositou {value} com sucesso {self.color['y']}\n")
        
        if cmd == False:
            value = input(f"{self.color['y']}Insira o valor que será depositado! (10 - 1500)\n{self.color['w']}/cancel {self.color['y']}para cancelar!\n>>{self.color['w']}").replace(",", ".")
            
            try:
                value = float(value)
                put_result(value)
                
            except:
                if value == "/cancel":
                    input(f"{self.color['w']}/put {self.color['y']}cancelado!\n")
                elif len(value) < 1:
                    input(f"{self.color['r']}O comando {self.color['w']}/put {self.color['r']}não aceita valores vazios!\n")
                else:
                    input(f"{self.color['w']}{value} {self.color['r']}não é um comando válido para {self.color['w']}/put\n{self.color['y']}Digíte apenas números nesse comando!\n")
                
        else:
            put_result(cmd)
            
            
    #ativa giros automáticos
    def __command_auto(self):
        spins = input(f"{self.color['y']}Quantos giros automáticos você deseja? (10 - 100)\n{self.color['w']}/cancel {self.color['y']}para cancelar!\n>>{self.color['w']}")
        
        try:
            spins = int(spins)
            if 100 >= spins >= 10:
                self.game.auto = spins
            else:
                input(f"{self.color['r']}Quantidade de giros inválidas!\n{self.color['y']}Mín: 10 / Máx: 100\n")
                
        except:
            input(f"{self.color['r']}O comando {self.color['w']}/auto {self.color['r']}aceita apenas números inteiros!\n{self.color['y']}")