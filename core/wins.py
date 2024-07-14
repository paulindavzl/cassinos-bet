#Este arquivo será usado apenas na renderização com Terminal

import os

class Wins:
    def __init__(self, color):
        os.system("clear")
        self.color = color
        self.intro()
        
    def intro(self):
        os.system("clear")
        print(f"""=--==--=[ FORMAS DE GANHOS E VALORES ]=--==--=
        
Você poderá ver nesta página:
    
    •1 - Formas de ganhar
    •2 - Valores de cada carta e naipes
    \n/cancel para voltar ao jogo
    
{'=--='*10}""")
        opc = input(f"O que você deseja ver? (responda com o índice)\n>>")
        
        if opc.strip() == "1":
            self.wins_form()
            self.intro()
        elif opc.strip() == "2":
            self.values()
            input("Enter para voltar à página anterior\n")
            self.intro()
        elif opc.strip() == "/cancel":
            pass
        else:
            input("Opção inválida!\n")
            self.intro()
        
    def wins_form(self):
        os.system("clear")
        print(f"""{'=--='*10}
        
Neste jogo, existem 5 tipos de ganhos:
    
    •1 - Horizontal
    •2 - Vertical
    •3 - Diagonais:
        - De cima para baixo / esquerda para direita
        - De baixo para cima / esquerda para direita
    •4 - Combo de Wilds
    •5 - Full Body:
        - Full Red (todos os naipes vermelhos)
        - Full Black (todos os naipes pretos)
        \n/cancel para voltar à página anterior
        
{'=--='*10}""")
        opc = input("Qual tipo você quer ver? (responda com o índice)\n>>")
        
        def obs():
            print(f"""
O ganho final é resultado da seguinte equação:
            
    • A + (A × B)
    
Onde:
    
    •A é o valor da aposta
    •B é o valor que resulta da combinação das cartas e naipes
    
    ~Observe que nenhum ganho será menor que o valor apostado!

{'=--='*10}""")

            input("Enter para voltar à página anterior\n")
            self.wins_form()
        
        match opc.strip():
            case "1":
                self.win_horizontal()
                obs()
            case "2":
                self.win_vertical()
                obs()
            case "3":
                self.win_diagonal()
                obs()
            case "4":
                self.win_combo()
                obs()
            case "5":
                self.win_full_body()
                obs()
            case "/cancel":
                pass
            case _:
                input("Opção inválida!\n")
                self.wins_form()
                
        
        
    def win_horizontal(self):
        os.system("clear")
        print(f"""=--==--==--=[  GANHOS NA HORIZONTAL  ]=--==--==--=

Cada rodada você poderá ganhar com até 3 horizontais! Esses ganhos podem ser:
    
    •Cartas sequenciais com naipes iguais:
        
        A♥️  2♥️  3♥️
        
    •Cartas iguais com naipes diferentes:
        
        A♥️  A♠️  A♦️
            
{'=--='*10}""")
        
        self.combinations()
        
        
    def win_vertical(self):
        os.system("clear")
        print(f"""=--==--==--=[  GANHOS NA VERTICAL  ]=--==--==--=

Cada rodada você poderá ganhar com até 3 verticais! Esses ganhos se dão por naipes iguais alinhados na vertical:
    
    A♥️
    
    K♥️
    
    7♥️
    
    ~Observe que para ganhar na vertical, as cartas não precisam ser iguais ou sequenciais!
    
{'=--='*10}""")

        self.combinations()
        
        
    def win_diagonal(self):
        os.system("clear")
        print(f"""=--==--==--=[ GANHOS NAS DIAGONAIS ]=--==--==--=

Cada rodada você poderá ganhar nas duas diagonais simultaneamente de duas formas:
    
    •Com cartas sequenciais e naipes iguais
    •Com cartas iguais e naipes diferentes
        
        A♥️  9♠️  2♣️
        
        Q♦️  2♥️  6♦️
        
        2♠️  K♣️  3♥️
        
        ~Observe que o ganho da:
            -Diagonal de cima para baixo / esquerda para direita é com cartas sequenciais e naipes iguais!
            -Diagonal de baixo para cima / esquerda para direita é com cartas diferentes e naipes diferentes!
        
{'=--='*10}""")

        self.combinations()
        
        
    def win_combo(self):
        os.system("clear")
        print(f"""=--==--=[ GANHOS COM COMBO DE WILDS ]=--==--=

Cada rodada você tem 1,5% de chance de ganhar um COMBO DE WILDS:
    
    J🃏  J🃏  J🃏
    
    J🃏  J🃏  J🃏
    
    J🃏  J🃏  J🃏
    
    ~O valor pago por cada COMBO DE WILDS depende do valor de cada carta que pode vir:
        
        •A, J, Q e K
        
    ~O ganho total é o valor da carta multiplicado por 50
    
    ~O COMBO DE WILDS não faz combinações com outras formas de ganhos, podendo pagar de 60 - 150 vezes o valor da aposta!

{'=--='*10}""")


    def win_full_body(self):
        os.system("clear")
        print(f"""=--==--==--=[ GANHOS COM FULL BODY ]=--==--==--=

Cada rodada pode vir um Full Body, que são quando todas as cartas tem os naipes da mesma cor! Existem dois tipos diferentes:
    
    •Full Black:
        
        J♠️  Q♠️  K♠️
        
        J♠  ️Q♠️  K♠️
        
        J♠️  ️Q♠️  K♠️
        
    •Full Red:
        
        J♥️  Q♥️️  K♥️
        
        J♥️  Q♥️  K♥️
        
        J♥️  Q♥️  K♥️
        
        ~Ganhos em Full Body podem combinar com outros tipos de ganhos e é a unica forma de obter o ganho máximo de 555 vezes o valor apostado + o valor apostado!
        
        ~Pagamento mínimo de um Full Body é de 100 + valor apostado!
        

{'=--='*10}""")


    def combinations(self):
        print(f"""
Existem situações onde os ganhos podem combinar com outros tipos:
    
    •Diagonais + Vertical + Horizontais:
        
        A♥️  2♥️  3♥️
        
        A♠️  A♥  A️♣️
        
        2♥️  3♥️  A♥️
        
        ~Observe que nesse caso você teria ganho na segunda linha vertical, em todas as linhas horizontais nas duas diagonais!
        ~Também é possível observar que para ganhar em cartas sequenciais, elas não precisam estar na ordem correta:
            
            • 2♥  3♥  A️♥️  →  A♥️  2♥️  3♥️
            
            -Isso pode ser visto:
                No ganho da última linha horizontal
                No ganho da Diagonal de baixo para cima / da esquerda para direita
                
        ~Se você conseguir 5 ganhos em uma rodada, o ganho será multiplicado por 10, como seria nesse caso que tem 6 possíveis ganhos!
            
{'=--='*10}""")
        
        
    def values(self):
        os.system("clear")
        print(f"""=--==--=[ VALORES DAS CARTAS E NAIPES ]=--==--=

A maioria das cartas neste jogo tem o mesmo valor, com exceção das cartas:
    
    •A = 0,25
    •J = 0,12
    •Q = 0,2
    •K = 0,3
    
O restante das cartas (2 - 9) valem 0,05

    ~O valor de cada carta é somado e o resultado final é multiplicado pelo valor da aposta! Para saber o valor ganho basta resolver a equação:
        
        • A + (A × B)
        
        Onde:
            
            A = valor da aposta
            B = resultado da combinação de cartas e naipes
            
    ~O valor do ganho final nunca será menor que o valor apostado
    
    ~Cada carta tem uma chance de vir a cada rodada:
        
        •A, J, Q, K = ±3,57% ou 1/28 de chance de vir
        •2 - 9 = ±10,71% ou 3/28 de chance de vir
    
Os naipes também tem seus valores específicos e chances de vir:
    
    •♥️ = 0,2 (±16,6% ou 1/6 de chance de vir)
    •♠ = 0,15 (±16,6% ou 1/6 de chance de vir)
    •️♦️ = 0,08 (±33,3% ou 2/6 de chance de vir)
    •️♣️ = 0,075 (±33,3% ou 2/6 de chance de vir)
    
Para saber o valor ganho é necessário saber 4 coisas:
   
   •O valor apostado
   •O valor de cada carta envolvido na vitória
   •O valor de cada naipe envolvido na vitória
   •Se multiplica ou não
   
   ~Veja o exemplo:
       
       Valor da aposta = 1.0 BetCoin
       
       A♥️  2♥️  3♥️
       
       Se usarmos as informações já fornecidas, sabemo que o:
           
           •Valor de carta: 0,25 (A) + 0,05 (2) + 0,05 (3) = 0,6
           •Valor de naipe: 3 × 0,2 (3 × ♥️) = 0,6
           
           Ou seja, o valor deste ganho é a soma do valor de cartas + o valor de naipes, multiplicado pelo valor da aposta:
               
               •Valor de ganho: 1 × (0,6 + 0,6) = 1,2
               
           No final de tudo, basta somar com o valor da aposta (+1):
               
               • 1 + 1,2 = 2,2
              
        E este exemplo não multiplica, já que para multiplicar é necessário acumular 5+ ganhos em uma rodada!
       
{'=--='*10}""")
