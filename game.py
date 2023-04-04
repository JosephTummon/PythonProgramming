from random import randint

class Creature():
    def __init__(self, name, abilities=(1, 5, 5), maxhp=10):
        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.abilities = {}
        self.setabilities(abilities)

    def setabilities(self, tuple):
        self.abilities["attack"] = tuple[0]
        self.abilities["defense"] = tuple[1]
        self.abilities["speed"] = tuple[2]

    def check_life(self):
        if self.hp > 0:
            return self.hp
        else:
            self.hp = 0
            print(self.name, "has fainted...")
            return 0
    
    def attack(self, target):
        attackroll = randint(1, 20)
        attackrandom = int(randint(1, 4))
        attackstrength = self.abilities["attack"] + attackrandom
        defensevalue = target.abilities["speed"] + target.abilities["defense"]
        print(self.name, "attacks", target.name)
        if attackroll > defensevalue:
            print(self.name, "did", attackstrength, "damage!")
            target.hp -= attackstrength
            return target.hp
        else:
            print("Attack missed...")

    def turn(self, roundnum, target):
        self.attack(target)
        return target.check_life()             

### Task 1 Script ###
"""
gnome = Creature("Gnome", (3, 5, 5), 100)
dwarf = Creature("Dwarf", (3, 5, 5))
for i in range(50):
    if (dwarf.hp != 0 and gnome.hp != 0):
        print("Round", i + 1)
        print(dwarf.name, "attacks", gnome.name)
        dwarf.turn(i, gnome)
        print(gnome.name, "attacks", dwarf.name)
        gnome.turn(i, dwarf)
"""

class Fighter(Creature):
    def __init__(self, name, abilities=(5, 10, 3), maxhp=50):
        Creature.__init__(self, name, abilities, maxhp)
        self.shield = False
    
    def shield_up(self):
        if self.shield == False:
            self.abilities["attack"] -= 5
            self.abilities["defense"] += 5
            self.shield = True
        else:
            print("Shield was already up!")

    def shield_down(self):
        if self.shield == True:
            self.abilities["attack"] += 5
            self.abilities["defense"] -= 5
            self.shield = False
        else:
            print("Shield was already down")
    
    def turn(self, round_num, target):
        round_num += 1
        if round_num % 4 == 1:
            self.attack(target)
            self.shield_up()
        elif round_num % 4 == 2 or round_num % 4 == 3:
            self.attack(target)
        elif round_num % 4 == 0:
            self.shield_down()
            self.attack(target)
        if target.check_life() != 0:
            print("Target still has", target.hp, "left.")


### Task 2 script ###
"""
dwarf = Creature("Dwarf", (3, 5, 5), 50)    
knight = Fighter("Knight")
for i in range(20):
    if (knight.hp != 0 and dwarf.hp != 0):
        print("Round", i + 1)
        print(dwarf.name, "attacks", knight.name)
        dwarf.turn(i, knight)
        if (knight.hp == 0):
            break
        print(knight.name, "attacks", dwarf.name)
        knight.turn(i, dwarf)
""" 

class Archer(Creature):
    def __init__(self, name, abilities=(7, 8, 8), maxhp=30):
        Creature.__init__(self, name, abilities, maxhp)
        self.modified = False
        
    def sneak_attack(self, target):
        num1 = randint(1, 20)
        num2 = randint(1, 20)
        attacknum = max(num1, num2)
        if self.abilities["speed"] > target.abilities["speed"]:
            attacknum += self.abilities["speed"] - target.abilities["speed"]
        if self.modified == False:
            self.abilities["attack"] += 3
            self.abilities["defense"] -= 3
            self.modified = True
        print(self.name, "sneak attacks", target.name)
        if attacknum > target.abilities["defense"] + target.abilities["speed"]:
            attackdamage = self.abilities["attack"] + randint(1,4)
            target.hp -= attackdamage
            print("Attack hits for", attackdamage, "damage!")
        else:
            print("Attack missed...")

    def turn(self, round_num, target):
        round_num += 1
        if round_num % 4 == 1:
            self.attack(target)
        elif round_num % 4 == 2 or round_num % 4 == 3:
            self.sneak_attack(target)
        elif round_num % 4 == 0:
            self.attack(target)

### Task 3 Script ###
"""    
knight = Fighter("Knight")
elf = Archer("Elf")
for i in range(20):
    if (knight.hp != 0 and elf.hp != 0):
        print("Round:", i + 1)
        elf.turn(i, knight)
        if (knight.hp <= 0):
            knight.check_life()
            break
        knight.turn(i, elf)
"""

class Goblin(Creature):
    def __init__(self, name, abilities=(4, 6, 6), maxhp=15):
        Creature.__init__(self, name, abilities, maxhp)

class Orc(Creature):
    def __init__(self, name, abilities=(10, 6, 2), maxhp=50):
        Creature.__init__(self, name, abilities, maxhp)
        self.modified = False

    def heavy_attack(self, target):
        if self.modified == False:
            print(self.name, "is in rage!")
            self.abilities["attack"] += 5
            self.abilities["defense"] -= 3
            self.modified = True
        attackroll = randint(1, 20)
        attackrandom = int(randint(1, 4))
        attackstrength = self.abilities["attack"] + attackrandom
        defensevalue = target.abilities["speed"] + target.abilities["defense"]
        print(self.name, "attacks", target.name)
        if attackroll > defensevalue:
            print(self.name, "did", attackstrength, "damage!")
            target.hp -= attackstrength
            return target.hp
        else:
            print("Attack missed...")
    
    def attack(self, target):
        if self.modified == True:
            print(self.name, "cooled down...")
            self.abilities["attack"] -= 5
            self.abilities["defense"] += 3
            self.modified = False
        attackroll = randint(1, 20)
        attackrandom = int(randint(1, 4))
        attackstrength = self.abilities["attack"] + attackrandom
        defensevalue = target.abilities["speed"] + target.abilities["defense"]
        print(self.name, "attacks", target.name)
        if attackroll > defensevalue:
            print(self.name, "did", attackstrength, "damage!")
            target.hp -= attackstrength
            return target.hp
        else:
            print("Attack missed...")
    
    def turn(self, round_num, target):
        round_num += 1 
        if round_num % 4 != 0:
            self.attack(target)
        elif round_num % 4 == 0:
            self.heavy_attack(target)

### Exercise 2 ###
### Task 1 Script ###
"""
Goblin1 = Goblin("Goblin")
Orc1 = Orc("Orc")
for i in range(20):
    if (Goblin1.hp != 0 and Orc1.hp != 0):
        print("Round:", i + 1)
        Goblin1.turn(i, Orc1)
        if (Orc1.hp <= 0):
            Orc1.check_life()
            break
        Orc1.turn(i, Goblin1)
        if (Goblin1.hp <= 0):
            Goblin1.check_life()
            break
"""

class OrcGeneral(Orc, Fighter):
    def __init__(self, name, abilities=(10, 6, 2), maxhp=100):
        Orc.__init__(self, name, abilities, maxhp)
        self.shield = False

    def turn(self, round_num, target):
        round_num += 1
        if round_num % 4 == 1:
            self.attack(target)
            self.shield_up()
        elif round_num % 4 == 2:
            self.attack(target)
        elif round_num % 4 == 3:
            self.shield_down()
            self.attack(target)
        elif round_num % 4 == 0:
            self.heavy_attack(target)

### Test for OrcGeneral ###
"""   
Goblin1 = OrcGeneral("OrcGeneral")
Orc1 = Orc("Orc")
for i in range(20):
    if (Goblin1.hp != 0 and Orc1.hp != 0):
        print("Round:", i + 1)
        Goblin1.turn(i, Orc1)
        if (Orc1.hp <= 0):
            Orc1.check_life()
            break
        Orc1.turn(i, Goblin1)
        if (Goblin1.hp <= 0):
            Goblin1.check_life()
            break
"""
class GoblinKing(Goblin, Archer):
    def __init__(self, name, abilities=(4, 6, 6), maxhp=50):
        Goblin.__init__(self, name, abilities, maxhp)
        self.modified = False
    
    def turn(self, round_num, target):
        round_num += 1
        if round_num % 4 == 1:
            self.attack(target)
        elif round_num % 4 == 2 or round_num % 4 == 3:
            self.sneak_attack(target)
        elif round_num % 4 == 0:
            self.attack(target)

### Task 3 ###
"""
Goblin1 = OrcGeneral("OrcGeneral")
Orc1 = GoblinKing("GoblinKing")
for i in range(20):
    if (Goblin1.hp != 0 and Orc1.hp != 0):
        print("Round:", i + 1)
        Goblin1.turn(i, Orc1)
        if (Orc1.hp <= 0):
            Orc1.check_life()
            break
        Orc1.turn(i, Goblin1)
        if (Goblin1.hp <= 0):
            Goblin1.check_life()
            break
"""

### Exercise 3, The Wizard! ###

class Wizard(Creature):
    def __init__(self, name, abilities=(5, 10, 5, 10), maxhp=20):
        Creature.__init__(self, name, abilities, maxhp)
        self.abilities["arcana"] = abilities[3]
        self.mana = 100
    
    def attack(self, target):
        self.mana += 20
        if self.mana > 100:
            self.mana = 100
        attackroll = randint(1, 20)
        attackrandom = int(randint(1, 4))
        attackstrength = self.abilities["attack"] + attackrandom
        defensevalue = target.abilities["speed"] + target.abilities["defense"]
        print(self.name, "attacks", target.name)
        if attackroll > defensevalue:
            print(self.name, "did", attackstrength, "damage!")
            target.hp -= attackstrength
            return target.hp
        else:
            print("Attack missed...")
    
    def recharge(self):
        self.mana += 30
        print(self.name, "channels magical energy...")
        print("Mana: +30!")
        if self.mana > 100:
            self.mana = 100
    
    def firebolt(self, target):
        attackroll = randint(1, 20) + (self.abilities["arcana"] // 2)
        attackstrength = randint(1, self.abilities["arcana"])
        defensevalue = target.abilities["speed"] + target.abilities["defense"]
        print(self.name, "shot a firebolt at", target.name)
        if attackroll > defensevalue:
            print("Fireball hits for", attackstrength, "damage!")
            target.hp -= attackstrength
            self.mana += 10
            if self.mana > 100:
                self.mana = 100
                print("Max Mana!")
            return target.hp
        else:
            print("Attack missed...")

    def heal(self, target):
        if self.mana >= 20:
            print("Mana: -20!")
            healing = randint(0,8) + self.abilities["arcana"]
            target.hp += healing
            print(self.name, "healed", target.name, "by", healing, "points.")
            if target.hp > target.maxhp:
                target.hp = target.maxhp
            self.mana -= 20
            if self.mana < 0:
                self.mana = 0
        else:
            print("Not enough mana!")
    
    def massheal(self, allies):
        if self.mana >= 30:
            print("Mana: -30!")
            for i in allies:
                healing = randint(0, 10) + self.abilities["arcana"]
                i.hp += healing
                print(self.name, "healed", i.name, "by", healing, "points.")
                if i.hp > i.maxhp:
                    i.hp = i.maxhp
            self.mana -= 30
            if self.mana < 0:
                self.mana = 0
        else:
            print("Not enough mana!")

    def firestorm(self, enemies):
        if self.mana >= 50:
            print("Mana: -50!")
            for i in enemies:
                enemy = randint(1, 20) + i.abilities["speed"]
                damage = randint(5, 20) + self.abilities["arcana"]
                if enemy >= self.abilities["arcana"]:
                    print(i.name, "took", damage // 2, "damage!")
                    i.hp -= damage // 2
                else:
                    i.hp -= damage
                    print(i.name, "took", damage, "damage!")
            self.mana -= 50
            if self.mana < 0:
                self.mana = 0
        else: 
            print("Not enough mana!")

### Task 2 ###
"""
Goblin1 = OrcGeneral("OrcGeneral")
Orc1 = GoblinKing("GoblinKing")
knight = Fighter("Knight")
elf = Archer("Elf")
wizard = Wizard("Wizard")
allies = [knight, elf]
enemies = [Goblin1, Orc1]
### Testing wizard attack ###
for i in range(4):
    wizard.attack(Goblin1)
### Testing Firebolt ###
wizard.firebolt(Orc1)
### Testing wizard recharge ###
wizard.recharge()
### Testing Healing ###
wizard.heal(knight)
### Testing Mass Heal ###
wizard.massheal(allies)
### Testing Firestorm ###
wizard.firestorm(enemies)
"""

### Exercise 4 ###
### Task 1 ###
class Battle():
    def __init__(self):
        orcleader = Orc("Orcleader ")
        goblinleader = GoblinKing("GoblinKing")
        goblin1 = Goblin("Goblin")
        orc1 = Orc("Orc")
        self.enemies = [orcleader, goblinleader, goblin1, orc1]
        knight = Fighter("Knight")
        elf = Archer("Elf")
        self.allies = [knight, elf]
        self.player = Wizard("Player")
    
    ### Task 2 ###
    def auto_select(self, target_list):
        i = randint(0, (len(target_list) - 1))
        target = False
        for i in range(i, i + len(target_list)):
            if target_list[i % len(target_list)].hp != 0:
                target = True
                return target_list[i % len(target_list)]
        if target == False:
            return None
    
    def select_target(self, target_list):
        for i in range(len(target_list)):
            print(i+1, ":", target_list[i].name, ", HP: ", target_list[i].hp, "/", target_list[i].maxhp)
        choice = int(input("Enter Choice: ")) 
        while choice not in range(1, len(target_list) + 1):
            choice = int(input("Enter Choice:")) 
        return choice

    ### Task 3 ###
    def start(self):
        # Getting list in order of speed
        order = []
        line = "======================================================="
        for i in self.enemies:
            order.append(i)
        for i in self.allies:
            order.append(i)
        order = sorted(order, key=lambda x: x.abilities["speed"], reverse=True)

        # Execute each round
        print("THE BATTLE BEGINS")
        battle = True
        round = 1
        # Start battle 
        while round <= 20:
            print(line)
            print("Round:", round)
            print(line)
            enemiesalive = 0
            alliesalive = 0
            # Go through list in order
            for j in self.enemies:
                if j.hp != 0:
                    enemiesalive += 1 
            for j in self.allies:
                if j.hp != 0:
                    alliesalive += 1 
            for i in order:
                if i.hp > 0:
                    print(i.name)
                    if i in self.allies:
                        i.turn(round, self.auto_select(self.enemies))
                    elif i in self.enemies:
                        i.turn(round, self.auto_select(self.allies))
            for i in order:
                print(i.name, "has", i.hp, "HP.")
            round += 1
            if enemiesalive == 0:
                battle = False
            if alliesalive == 0:
                battle = False
            


### Testing Task 2 ###
'''
game = Battle()
game.select_target(game.enemies)
'''
### Testing Task 3 ###
game = Battle()
game.start()