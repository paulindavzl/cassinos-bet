import random as rm

class Slots:
    def __init__(self):
        self.wins = 0
        self.default_slots = [
            [("J", "hearts"), ("Q", "hearts"), ("K", "hearts")],
            [("J", "hearts"), ("Q", "hearts"), ("K", "hearts")],
            [("J", "hearts"), ("Q", "hearts"), ("K", "hearts")]
        ]
        
        self.__slots_cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "2", "3", "4", "5", "6", "7", "8", "9", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]
        self.__slots_naipes = ["hearts", "swords", "golds", "woods", "golds", "woods"]
        self.__slots_alternatives = {"A": "1", "J": "10", "Q": "11", "K": "12"}
        
        #utilizado na versão WEB para mostrar os ganhos
        self._slots_wins = [
            "sl", "sl", "sl", 
            "sl", "sl", "sl", 
            "sl", "sl", "sl"
        ]
    
    #sorteia as cartas
    def __raffle_slots(self):
        card = rm.choice(self.__slots_cards)
        naipe = rm.choice(self.__slots_naipes)
        return card, naipe
    
    #verifica o valor de cada naipe
    def __naipes_values(self, naipes):
        values = {
            "hearts": 0.2,
            "swords": 0.15,
            "golds": 0.08,
            "woods": 0.075
        }
        
        multi = 0
        for naipe in naipes:
            multi += values.get(naipe)
        return multi
        
        
    #verifica o valor de cada carta
    def __cards_values(self, cards):
        values = {
            "A": 0.25,
            "J": 0.12,
            "Q": 0.2,
            "K": 0.3
        }
        
        multi = 0
        for card in cards:
            if str(card) in "AJQK":
                multi += values.get(card)
            else:
                multi += 0.05
                
        return multi
    
    
    #organiza os slots
    def organizer_slots(self, anim = False):
        
        if self.wilds_combo() == True and anim == False:
            return self.__assured_win()
        else:
            slots = [
                [self.__raffle_slots(), self.__raffle_slots(), self.__raffle_slots()],
                [self.__raffle_slots(), self.__raffle_slots(), self.__raffle_slots()],
                [self.__raffle_slots(), self.__raffle_slots(), self.__raffle_slots()]
            ]
            return slots
        
        
    #verfiica se o slots premiam
    def check(self, slots):
        self.__multi = 0
        self._slots_wins = [
            "sl", "sl", "sl", 
            "sl", "sl", "sl", 
            "sl", "sl", "sl"
        ]
        self.__result = False
        self.__sequence = 0
        self.__big_win = False
        
        #verifica a sequêcia de naipes
        def __naipes_check(naipes):
            #naipes todos iguais
            if naipes[0] == naipes[1] and naipes[1] == naipes[2]:
                return "equal"
            #naipes todos diferentes
            elif naipes[0] != naipes[1] and naipes[0] != naipes[2] and naipes[1] != naipes[2]:
                return "different"
            #nem todos iguais ou diferentes
            else:
                return False
        
        #transcreve as cartas com letras
        def alternative_cards(slots):
            position = 0
            slot = []
            
            #modifica o valor das cartas (letras > números)
            for item in slots:
                new_item = self.__slots_alternatives.get(slots[position][0]), slots[position][1]
                
                #if não for letra, mantém o valor inicial
                if new_item[0] == None:
                    new_item = slots[position][0], slots[position][1]
                slot.append(new_item)
                position += 1
            return slot
        
        #verifica a sequência dos slots
        def sequential(slots, slot_win, position = False):
            slot_check = alternative_cards(slots)
            cards = [slot_check[0][0], slot_check[1][0], slot_check[2][0]]
            cards = sorted(cards, key = int)
            
            #verifica se existe sequência nos slots
            if int(cards[0]) + 1 == int(cards[1]) and int(cards[1]) + 1 == int(cards[2]):
                
                naipes = slot_check[0][1], slot_check[1][1], slot_check[2][1]
                cards = slot_check[0][0], slot_check[1][0], slot_check[2][0]
                
                #verifica se os naipes são iguais
                if __naipes_check(naipes) == "equal":
                    values_naipes = self.__naipes_values(naipes)
                    values_cards = self.__cards_values(cards)
                    
                    self.__multi += values_naipes + values_cards
                    self.__result = True
                    self.__sequence += 1
                    
                    #utilizado apenas na versão WEB
                    if position != False:
                        if position == 0:
                            self._slots_wins[0] = "win"
                            self._slots_wins[1] = "win"
                            self._slots_wins[2] = "win"
                        elif position == 1:
                            self._slots_wins[3] = "win"
                            self._slots_wins[4] = "win"
                            self._slots_wins[5] = "win"
                        elif position == 2:
                            self._slots_wins[6] = "win"
                            self._slots_wins[7] = "win"
                            self._slots_wins[8] = "win"
                            
                    else:
                        if slot_win == "TB":
                            self._slots_wins[0] = "win"
                            self._slots_wins[4] = "win"
                            self._slots_wins[8] = "win"
                        elif slot_win == "BT":
                            self._slots_wins[2] = "win"
                            self._slots_wins[4] = "win"
                            self._slots_wins[6] = "win"
      
        #verificia a diagonal de cima pra baixo
        def dTopBottom(slots):
            position = 0
            slot = []
            for item in slots:
                slot.append(item[position])
                position += 1
            
            if slot[0][0] == slot[1][0] and slot[1][0] == slot[2][0]:
                
                slot_check = alternative_cards(slot)
                naipes = slot_check[0][1], slot_check[1][1], slot_check[2][1]
                cards = slot_check[0][0], slot_check[1][0], slot_check[2][0]
                
                if __naipes_check(naipes) == "different":
                    values_naipes = self.__naipes_values(naipes)
                    values_cards = self.__cards_values(cards)
                    
                    self.__multi += values_naipes + values_cards
                    self.__result = True
                    self.__sequence += 1
                    self._slots_wins[0] = "win"
                    self._slots_wins[4] = "win"
                    self._slots_wins[8] = "win"
                
            else:
                sequential(slot, "TB")
                
        #verificia a diagonal de baixo para cima
        def dBottomTop(slots):
            position = 2
            slot = []
            for item in slots:
                slot.append(item[position])
                position -= 1
            
            if slot[0][0] == slot[1][0] and slot[1][0] == slot[2][0]:
                
                slot_check = alternative_cards(slot)
                naipes = slot_check[0][1], slot_check[1][1], slot_check[2][1]
                cards = slot_check[0][0], slot_check[1][0], slot_check[2][0]
                
                if __naipes_check(naipes) == "different":
                    values_naipes = self.__naipes_values(naipes)
                    values_cards = self.__cards_values(cards)
                    
                    self.__multi += values_naipes + values_cards
                    self.__result = True
                    self.__sequence += 1
                    self._slots_wins[2] = "win"
                    self._slots_wins[4] = "win"
                    self._slots_wins[6] = "win"
                
            else:
                sequential(slot, "BT")
                
        #verifica se existe ganhos na horizontal
        def horizontal(slots):
            position = 0 #indica qual linha horizonal foi analisada
            
            for item in slots:
                if item[0][0] == item[1][0] and item[1][0] == item[2][0]:
                    
                    slot_check = alternative_cards(item)
                    naipes = slot_check[0][1], slot_check[1][1], slot_check[2][1]
                    cards = slot_check[0][0], slot_check[1][0], slot_check[2][0]
                    
                    if __naipes_check(naipes) == "different":
                        values_naipes = self.__naipes_values(naipes)
                        values_cards = self.__cards_values(cards)
                        
                        self.__multi += values_naipes + values_cards
                        self.__result = True
                        self.__sequence += 1
                        if position == 0:
                            self._slots_wins[0] = "win"
                            self._slots_wins[1] = "win"
                            self._slots_wins[2] = "win"
                        elif position == 1:
                            self._slots_wins[3] = "win"
                            self._slots_wins[4] = "win"
                            self._slots_wins[5] = "win"
                        elif position == 2:
                            self._slots_wins[6] = "win"
                            self._slots_wins[7] = "win"
                            self._slots_wins[8] = "win"
                    
                else:
                    sequential(item, "HR", position)
                
                position += 1
                
        #verifica se todos os slots tem naipes pretos
        def fullBlack(slots):
            black_naipes = 0
            for slot in slots:
                for item in slot:
                    if item[1] == "swords" or item[1] == "woods":
                        black_naipes += 1
            if black_naipes == 9:
                if self.__multi < 1:
                    self.__multi = 1
                self.__multi *= 10.0
                self.__result = True
                self.__big_win = "Full Black"
                self.__sequence = 5
                self._slots_wins[0:] = [
                    "win", "win", "win",
                    "win", "win", "win",
                    "win", "win", "win"
                ]
        
        #verifica se todos os slots tem naipes vermelhos
        def fullRed(slots):
            red_naipes = 0
            for slot in slots:
                for item in slot:
                    if item[1] == "hearts" or item[1] == "golds":
                        red_naipes += 1
            if red_naipes == 9:
                if self.__multi < 1:
                    self.__multi = 1
                self.__multi *= 10.0
                self.__result = True
                self.__big_win = "Full Red"
                self.__sequence = 5
                self._slots_wins[0:] = [
                    "win", "win", "win",
                    "win", "win", "win",
                    "win", "win", "win"
                ]
                
        #verifica se os naipes verticais são iguais
        def vertical_naipes(slots):
            for pos_line in range(3):
                naipes = []
                for slot in slots:
                    naipes.append(slot[pos_line][1])
                    
                if naipes[0] == naipes[1] and naipes[1] == naipes[2]:
                    self.__multi += self.__naipes_values(naipes)
                    self.__result = True
                    self._slots_wins[pos_line] = "win"
                    self._slots_wins[pos_line + 3] = "win"
                    self._slots_wins[pos_line + 6] = "win"
                    
        
        if slots[0][0][1] != "wild":
            dTopBottom(slots)
            dBottomTop(slots)
            horizontal(slots)
            vertical_naipes(slots)
            fullBlack(slots)
            fullRed(slots)
            
        else:
            card = slots[0][0][0]
            self.__multi = 50 * self.__cards_values([card])
            self.__sequence = 5
            self.__result = True
            self.__big_win = "Combo de Wilds"
            self._slots_wins[0:] = [
                    "win", "win", "win",
                    "win", "win", "win",
                    "win", "win", "win"
                ]
        
        if self.__sequence >= 5:
            self.__multi *= 10
        
        return self.__result, float(f"{self.__multi: .2f}"), self.__big_win, self._slots_wins
        
        
    #calcula a chance de soltar combo de wilds
    def wilds_combo(self):
        #1,5% de chance de ganhar combo de wilds
        awarded = [1, 99, 196]
        raffle = rm.randint(1, 200)
        
        if raffle in awarded:
            return True
        else:
            return False
        
        
    #combo de wilds
    def __assured_win(self):
          possible_wins = [
              [
                  [("A", "wild"), ("A", "wild"), ("A", "wild")],
                  [("A", "wild"), ("A", "wild"), ("A", "wild")],
                  [("A", "wild"), ("A", "wild"), ("A", "wild")]
              ],
              [
                  [("J", "wild"), ("J", "wild"), ("J", "wild")],
                  [("J", "wild"), ("J", "wild"), ("J", "wild")],
                  [("J", "wild"), ("J", "wild"), ("J", "wild")]
              ],
              [
                  [("Q", "wild"), ("Q", "wild"), ("Q", "wild")],
                  [("Q", "wild"), ("Q", "wild"), ("Q", "wild")],
                  [("Q", "wild"), ("Q", "wild"), ("Q", "wild")]
              ],
              [
                  [("K", "wild"), ("K", "wild"), ("K", "wild")],
                  [("K", "wild"), ("K", "wild"), ("K", "wild")],
                  [("K", "wild"), ("K", "wild"), ("K", "wild")]
              ]
          ]
          
          wild_win = rm.choice(possible_wins)
          return wild_win
          