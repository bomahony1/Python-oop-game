import random
# Creature class 
# Has one argument name, and a default argument max_hp which is set to 10
# class has three methods:
#   check_life - checks health of creature, if its 0 it says creature has died, else it returns the health
#   attack - mechanics of attack function, function picks number between (1 and 20), if number is less than targets attack
#            plus speed abilities it miss's the attack, else it will attack target, damage dealt to target is decided by
#            picking random number between (1 and 4), and adding it to creatures own attack abilities.
#   turn - checks if targets life is equal to 0, if it is, return True, else attack the target.


class Creature:
    def __init__(self, name, max_hp = 10):
        self.name = name
        self.health = max_hp
        self.abilities = {"Attack":1, "Defense":5, "Speed": 5}
        self.max_hp = 10
    
    def check_life(self):
        if self.health < 0:
            self.health = 0
            print(self.name + " has died.")
            return self.health
        else:
            return self.health
        
    def attack(self, target):
        random_num = random.randint(1,20)
        target_defense_plus_speed = target.abilities['Speed'] + target.abilities["Defense"]
        print(self.name + " attacks " + target.name)
        if random_num < target_defense_plus_speed:
            print('Attack Missed...')
        else:
            random_num = random.randint(1, 4)
            attack_damage = random_num + self.abilities['Attack']
            target.health -= attack_damage
            print('Attack hits for ' + str(attack_damage) + " damage")
    
    def turn(self, roundnum, target):
        if target.check_life() == 0:
            return True
        else:
            self.attack(target)
            return False

# Fighter Class inherits Creature class
# Has one argument name, and a default argument max_hp which is set to 10
# Initalises parent class attibute with super().__init__()
# class has three methods:
#   shield_up - if fighter attack abilities and defense abilites are default, decrease attack abilities by 5 and increase
#               defense abilities by 5
#   shield_down - if fighter attack abilities and defense abilites are not default, increase attack abilities by 5 and decrease
#               defense abilities by 5
#   turn - Uses modular operators to check round numbers, In Round 1 the fighter attacks the target and then uses shield_up. 
#          In Round 2 and 3 the Fighter just attacks the target. In round 4 the Fighter uses shield_down and then attacks the target. 
#          Then it goes back to the Round 1 actions.  
#          if targets life is 0, return True and break out of loop

        
class Fighter(Creature):
    def __init__(self, name, max_hp = 50):
        super().__init__(name, max_hp)
        self.abilities = {"Attack":5, "Defense":10, "Speed": 3}
        self.max_hp = 50
    
    def shield_up(self):
        attack = self.abilities['Attack']
        defense = self.abilities['Defense']
        if attack == 5 and defense == 10:
            self.abilities['Attack'] -= 5
            self.abilities['Defense'] += 5
        print(self.name + " takes a defensive stance.")
        
    def shield_down(self):
        attack = self.abilities['Attack']
        defense = self.abilities['Defense']
        if attack != 5 and defense != 10:
            self.abilities['Attack'] = 5
            self.abilities['Defense'] = 10
        print(self.name + " stance returns to normal.")
    
    def turn(self, round_num, target):
        if round_num % 4 == 1:
            self.attack(target)
            self.shield_up()
        if round_num % 4 == 2 or round_num % 4==3:
            self.attack(target)
        if round_num % 4== 0:
            self.shield_down()
            self.attack(target)
        if target.check_life() == 0:
            return True 

# class Archer inherits Creature class
# Has one argument name, and a default argument max_hp which is set to 10
# Initalises parent class attibute with super().__init__()
# class has three methods:
#   attack - checks if attack and defense abilties are set to default, if they aren't set them to default,
#            generate random number between 1 and 20, and add targets defense and speed values, if the random
#            number generated is less than sum of targets defense and speed values, the attack missed
#            else attack target, attack damage is sum of a random number between 1 and 8, and archers 
#            attack value
#   sneak_attack - generate two random numbers and pick the larger number, if archers abilities is more than targets
#                  abilities, add the difference to the larger random number. If archers attack value and defense values 
#                  are set to default, add 3 to attack and minus 3 from defense. Finally add the targets defense and speed 
#                  values, if it is more than the total attack roll, the attack missed. Else the target is attacked, the total
#                  attack values is the sum of a number between 1 and 8 and archers attack values.
#   turn -  Uses modular operators to check round numbers, In Round 1 the archer attacks the target. 
#           In Round 2 and 3 and 4 the Archer uses sneak_attack on the target. Then it goes
#           back to the Round 1 actions. Every round check targets health, if it is True, 
#           break out of loop.

class Archer(Creature):
    def __init__(self, name, max_hp=30):
        super().__init__(name, max_hp)
        self.abilities = {"Attack":7, "Defense":8, "Speed":8}
        self.max_hp = 30
    
    def attack(self, target):
        attack = self.abilities['Attack']
        defense = self.abilities['Defense']
        if attack != 7 and defense != 8:
            self.abilities['Attack'] = 7
            self.abilities['Defense'] = 8
        random_num = random.randint(1,20)
        target_defense_plus_speed = target.abilities['Speed'] + target.abilities["Defense"]
        print(self.name + " attacks " + target.name)
        if random_num < target_defense_plus_speed:
            print('Attack Missed...')
        else:
            random_num = random.randint(1, 8)
            attack_damage = random_num + self.abilities['Attack']
            target.health -= attack_damage
            print('Attack hits for ' + str(attack_damage) + " damage!")
   
    def sneak_attack(self, target):
        attack_roll = []
        for i in range(2):
            attack_roll.append(random.randint(1,20))
        attack_roll.sort()
        largest_attack_roll = attack_roll[-1]
        total_attack_roll = largest_attack_roll
        if self.abilities["Speed"] > target.abilities["Speed"]:
            difference = self.abilities["Speed"] - target.abilities["Speed"]
            total_attack_roll = largest_attack_roll + difference
        if self.abilities['Attack'] == 7 and self.abilities['Defense'] == 8:
            self.abilities['Attack'] += 3
            self.abilities['Defense'] -= 3
            print(self.name + " attack raised.")
            print(self.name + " defense reduced.")
        target_defense_and_speed = target.abilities['Speed'] + target.abilities["Defense"]
        print(self.name + " sneak attacks " + target.name)
        if total_attack_roll < target_defense_and_speed:
            print('Attack Missed...')
        else:
            random_num = random.randint(1, 8)
            attack_damage = random_num + self.abilities['Attack']
            target.health -= attack_damage
            print('Attack hits for ' + str(attack_damage) + " damage")
        
    def turn(self, round_num, target):
        if round_num % 3 == 1:
            self.attack(target)
        if round_num % 3 == 2 or round_num % 3==0:
            self.sneak_attack(target)
        if target.check_life() == 0:
            return True 


# class Goblin inherits Creature class
# Has one argument name, and a default argument max_hp which is set to 10
# Initalises parent class Creature attibutes with super().__init__()


class Goblin(Creature):
    def __init__(self, name, max_hp=15):
        super().__init__(name, max_hp)
        self.abilities = {"Attack":4, "Defense":6, "Speed":6}
        self.max_hp = 15


# class Orc inherits Creature class
# Has one argument name, and a default argument max_hp which is set to 10
# Initalises parent class Creature attibutes with super().__init__()
# class has three mehtods:
#   heavy_attack - Sets Orc's attack to heavy attack, checks if orcs abilities are defualt values at 10 for attack and 6 
#                  for defense, if they are increase attack by 5 points and decrease defense by 3, then call normal attack 
#                  method from creature class.
#   attack - Changes Orc's attack from heavy attack to normal attack. Checks if orcs abilities are not defualt values, 1
#            0 for attack and 6 for defense, if they arent, set attack to 10 and set defense to 6.
#   turn - Sets the sequence of Orc's attack. In Round 1,2,3 the orc attacks the target. In Round 4 the orc uses heavy_attack on the target. 
#          Then it goes back to Round 1 actions in a round robin style. very round check targets health, if it is True, 
#           break out of loop.

class Orc(Creature):
    def __init__(self, name, max_hp=50):
        super().__init__(name, max_hp)
        self.abilities = {"Attack":10, "Defense":6, "Speed":2}
        self.max_hp = 50
    
    def heavy_attack(self, target):
        if self.abilities['Attack'] == 10 and self.abilities['Defense'] == 6:
            self.abilities['Attack'] += 5
            self.abilities['Defense'] -= 3
        print(self.name + " is in rage.")
        Creature.attack(self, target)
    
    def attack(self, target):
        if self.abilities['Attack'] != 10 and self.abilities['Defense'] != 6:
            self.abilities['Attack'] = 10
            self.abilities['Defense'] = 6
        Creature.attack(self, target)
    
    def turn(self, round_num, target):
        if round_num % 4 == 1 or round_num % 4 == 2 or round_num % 4==3:
            if round_num > 1 and round_num % 4 == 1:
                print(self.name + " cooled down") 
            self.attack(target)
        if round_num % 4== 0:
            self.heavy_attack(target)
        if target.check_life() == 0:
            return True

# class OrcGeneral inherits from Orc and Fighter class 
# Has one argument name, and a default argument max_hp which is set to 10
# Initalises parent class Orc attibutes with super().__init__()
# class has one method:
#   turn - Sets the sequence of OrcGeneral's attack. Round 1, the OrcGeneral attacks the target and then uses shield_up. In Round 2, the OrcGeneral just attacks
#          the target. In Round 3, the OrcGeneral uses shield_down and then then attacks the target. In Round 4, the
#          OrcGeneral uses heavy_attack on the target. Every round check targets health, if it is True, 
#           break out of loop.


class OrcGeneral(Orc, Fighter):
    def __init__(self, name, max_hp = 100):
        super().__init__(name, max_hp)
        self.abilities = {"Attack":10, "Defense":6, "Speed":2}  
        self.max_hp = 100
    
    def turn(self, round_num, target):
        if round_num % 4 == 1:
            self.attack(target)
            self.shield_up()
        if round_num % 4 == 2:
            self.attack(target)
        if round_num % 4 == 3:
            self.shield_down()
            self.attack(target)
        if round_num % 4== 0:
            self.heavy_attack(target)
        if target.check_life() == 0:
            return True 


# class OrcGeneral inherits from Orc and Fighter class 
# Has one argument name, and a default argument max_hp which is set to 10
# Initalises parent class Orc attibutes with super().__init__()
# class has one method:
#   turn - Sets the sequence of OrcGeneral's attack.

class GoblinKing(Archer, Goblin):
    def __init__(self, name, max_hp=50):
        super().__init__(name, max_hp)
        self.abilities = {"Attack":10, "Defense":6, "Speed":2} 
        self.max_hp = 50

    def turn(self, round_num, target):
        if round_num % 3 == 1:
            self.attack(target)
        if round_num % 3 == 2 or round_num % 3==0:
            self.sneak_attack(target)
        if target.check_life() == 0:
            return True     

# class Wizard inherits from Creature class
# Has one argument name, and a default argument max_hp which is set to 20
# Initalises parent class Orc attibutes with super().__init__()
#   attack - increases wizards mana by 20 points, if the current mana plus 20 is more than 100, mana is set to max mana.
#            then call Creature attack method
#   recharge - increases wizards mana by 30 points, if the current mana plus 30 is more than 100, mana is set to max mana.
#   firebolt - create a random number between 1 and 10 and add half the Arcana value to the random number (rounded
#              If the attack hits the target, if the current mana plus 20 is more than 100, mana is set to max mana, 
#              the wizard gains 10 Mana points.
#   heal - heals aliies, picks a random number between 1 and 8, and add's it to half the arcana value. add this value
#          to target. If this value is more than targets max health, then targets health is set to max health.
#          else just add the value to targets health.
#   mass heal - takes agrument allies which is for the heros. if wizards mana is less then 30, mass heal won't work.
#             else take 30 mana points away. total heal is a random number between 1 and 10, and arcana number. 
#             Add this value to allies health, if this number added is more than heros max health, set health to max health.
#             else just add the value to all allies health and add to wizards health aswell.
#   fire_storm - takes one argument enemies, if the wizards mana is less than 50, wizard dosent have enough, else
#              for all the enemies deal fire sotrm damage which is calcukate by the wizards arcana vlaue and add it
#              to a random number between 5 and 20. Add the mana and a random number between 1 and 20. If this value is 
#              more than or equal to wizards abilites, take away targets health by attack damage divided by 2, else take 
#              away the original attack damage.



class Wizard(Creature):
    def __init__(self, name, max_hp=20):
        super().__init__(name, max_hp)
        self.abilities = {"Attack": 3, "Defense": 5, "Speed": 5, "Arcana": 10}
        self.mana = 100
        self.max_mana = 100
        self.max_hp = 20
    
    def attack(self, target):
        if (self.mana + 20) > 100:
            print("Mana is full")
            self.mana = 100
        else:
            self.mana += 20
            print("Mana: +20!")
        Creature.attack(self, target)
    
    def recharge(self):
        print("Gandalf channels magical energy...")
        if (self.mana + 30) > 100:
            self.mana = 100
            print("Mana is full")
        else:
            self.mana += 30
            print('Mana: +30!')
    
    def fire_bolt(self, target):
        print(self.name + " fires a fire bolt at " + target.name)
        attack_roll = random.randint(1,20)
        arcana_num = int((self.abilities["Arcana"])/2)
        total_attack_roll = attack_roll + arcana_num
        target_defense_plus_speed = target.abilities['Speed'] + target.abilities["Defense"]
        if total_attack_roll < target_defense_plus_speed:
            print('Fire Bolt Attack Missed...')
        else:
            attack_value = random.randint(1, self.abilities["Arcana"])
            target.health -= attack_value
            print('Fire bolt hits for ' + str(attack_value) + " damage")
            if (self.mana + 10) > 100:
                self.mana = 100
                print("Mana is full")
            else:
                self.mana += 10
                print("Mana: +10!")

    def heal(self, target):
        if self.mana < 20:
            print("Wizard does not have enough Mana points to heal target")
        else:
            self.mana -= 20
            print("Mana: -20")
            random_num = random.randint(0,8)
            arcana_num = int((self.abilities["Arcana"])/2)
            total_heal = random_num + arcana_num
            if target.health + total_heal > target.max_hp:
                target.health = target.max_hp
                print(self.name + " has increased " + target.name + " health to max HP!")
            else:
                target.health += total_heal
                print(self.name + " heals " + target.name + " for " + str(total_heal) + " HP!")

    
    def mass_heal(self, allies):
        if self.mana < 30:
            print("Wizard does not have enough Mana points to heal")
        else:
            self.mana -= 30
            print("Mana: -30")
            random_num = random.randint(0,10)
            arcana_num = self.abilities["Arcana"]
            total_heal = random_num + arcana_num
            if self.health + total_heal > self.max_hp:
                self.health = self.max_hp
                print(self.name + " has increased his own health to max HP!")
            else:
                self.health += total_heal
                print(self.name + " heals himself for " + str(total_heal) + " HP!")
            for i in allies:
                if i.health + total_heal > i.max_hp:
                    i.health = i.max_hp
                    print(self.name + " has increased " + i.name + " health to max HP!")
                else:
                    i.health += total_heal
                    print(self.name + " heals " + i.name + " for " + str(total_heal) + " HP!")

    
    def fire_storm(self, enemies):
        if self.mana < 50:
            print("Wizard does not have enough Mana points to use fire storm")
        else:
            self.mana -= 50
            print("Mana: -50")
            for i in enemies:
                arcana_num = self.abilities["Arcana"]
                random_num = random.randint(5, 20)
                attack_damage = random_num + arcana_num
                random_num2 = random.randint(1,20)
                mana_plus_random_num2 = self.abilities["Speed"] + random_num2
                if mana_plus_random_num2 >= self.abilities["Arcana"]:
                    i.health -= int(attack_damage/2)
                    print("Fire Storm deals "+ str(int(attack_damage/2)) + " fire damage to " + i.name + "!")
                else:
                    i.health -= attack_damage
                    print("Fire Storm deals "+ str(attack_damage) + " fire damage to " + i.name + "!")
    
    def turn(self, round_num, target):
        if target.check_life() == 0:
            return True

# class Battle 
# two arguments, enemies and heros
# added an instance varaiables wizard to Wizard
#   method - auto_select takes argument, of a target list and chooses a random target. if the target has more than 0 health,
#          return the random target. else return none.
#   select_target - chooses a target in a target list and prints out all the targets
#   start - joins heros enemies and players, then sorts them based on their speed value, iterate through the sorted list and 
#          if creature is a heros, they randomly choose and enemy and attack them, if creature is enemey, they randomly choose
#          hero. if creature is player, it calls the player turn method. If any of the creatures of 0 life, they are removed from the list
#          if the any of the lists are empty then the game ends
#   player turn - prints all options avalable for player, if player chooses heal, attack or firebolt, it calls select_target method and then
#          calls the respective method from the wizard class based on which target is slected.
#          else it just calls the respective method from the wizard class such as mass heal. If wizard dosent have enough mana points for 
#          a method, it prompts user for another input.


class Battle:
    def __init__(self):
        global enemies
        global allies
        global wizard
        enemies = []
        allies = []
        goblinking = GoblinKing("Goblin King")
        orcgeneral = OrcGeneral("Orc General")
        orc = Orc("Orc")
        goblin = Goblin("Goblin")
        aragon = Fighter("Aragon")
        bromir = Fighter("Boromir")
        leoglas = Archer("Legolas")
        wizard = Wizard("Gandalf")
        enemies.extend([goblinking, orcgeneral, orc, goblin])
        allies.extend([aragon, wizard, bromir, leoglas])
    
    def auto_select(self, target_list):
        choice = random.choice(target_list)
        if choice.health > 0:
            return choice
        else:
            return None
    
    def select_target(self, target_list):
        print("Select target to choose: ")
        for i in range(len(target_list)):
            if target_list[i] == wizard:
                continue
            print(str(i + 1) + ": " + target_list[i].name + ", HP: " + str(target_list[i].health) + "/" + str(target_list[i].max_hp))
        while True:
            try:
                user_input = int(input("Enter Choice: "))
            except ValueError:
                print("Error... choose number between 1 - " + str(len(target_list)))
                continue
            if user_input<1 or 4<user_input:
                print("Error... choose number between 1 - " + str(len(target_list)))
                continue
            else:
                for i in range(len(target_list)):
                    if int(user_input) - 1 == i:
                        print("You Choose: \n" + target_list[i].name + ", HP: " + str(target_list[i].health) + "/" + str(target_list[i].max_hp))
                        return target_list[i]

                
    def start(self):
        join = allies + enemies
        sorted_speed = sorted(join, key=lambda x: x.abilities["Speed"], reverse=True)
        print("THE BATTLE BEGINS")
        count = 0
        while True:
            count += 1
            print("=======================================================")
            print("Round " + str(count))
            print("=======================================================")
            for i in sorted_speed:
                if len(allies)-1 == 0:
                    print("Allies Are Defeated")
                    print("=======================================================")
                    return True
                if len(enemies) == 0:
                    print("Enemies Are Defeated")
                    print("=======================================================")
                    return True
                if wizard.check_life() == 0:
                    print("You Have Died")
                    print("Game Over...")
                    return True
                if i == wizard:
                    self.player_turn()
                    print("\n=======================================================")
                else:
                    if i in allies:
                        random_target = self.auto_select(enemies)
                        if random_target == None: 
                            continue
                        if i.turn(count, random_target) == True:
                            enemies.remove(random_target)
                            print("\n" + i.name + " Defeated " + random_target.name)
                        print("\n=======================================================")
                    if i in enemies:
                        random_target = self.auto_select(allies)
                        if random_target == None: 
                            continue
                        if i.turn(count, random_target) == True: 
                            allies.remove(random_target)
                            print("\n" + i.name + " Defeated " + random_target.name)
                        print("\n=======================================================")
            print("End of Round " + str(count))
            print("=======================================================")
    
    
    def player_turn(self):
        print("=======================================================")
        print("Player: " + wizard.name + " HP:" + str(wizard.health) + "/" + str(wizard.max_hp) + " Mana:" + str(wizard.mana) + "/" + str(wizard.max_mana))
        print("Allies: ")
        for i in allies:
            if i == wizard:
                continue
            else:
                print("  " + i.name + ", HP: " + str(i.health) + "/" + str(i.max_hp))
        print("Enemies: ")
        for i in enemies:
            print("  " + i.name + ", HP: " + str(i.health) + "/" + str(i.max_hp))
        print("=======================================================")
        print("Actions. F: Attack R: Recharge Mana")
        print("Spells. 1: Heal 2: Firebolt 3: Mass Heal 4: Fire Storm")
        print("To Quit game type: Quit")
        print("=======================================================")
        action_input = input("Enter action: ").lower()
        while True:

            #Actions for allies...

            # heal
            if action_input == str(1):
                if wizard.mana < 20:
                    print("Not enough Mana points, pick another option")
                    action_input = input("Enter action: ")
                else:
                    wizard.heal(self.select_target(allies))
                    return True

            #mass heal 
            elif str(action_input) == str(3):
                if wizard.mana < 30:
                    print("Not enough Mana points, pick another option")
                    action_input = input("Enter action: ")
                else:
                    wizard.mass_heal(allies)
                    return True
            
            #Actions for player...

            #recharge
            elif action_input == "r":
                wizard.recharge()
                return True
            
            #Actions for enemies...

            # attack
            if action_input == "f":
                target_selected = self.select_target(enemies)
                wizard.attack(target_selected)
                if target_selected.check_life() == 0:
                    enemies.remove(target_selected)
                return True
            
            # firebolt
            if action_input == str(2):
                target_selected = self.select_target(enemies)
                wizard.fire_bolt(target_selected)
                if target_selected.check_life() == 0:
                    enemies.remove(target_selected)
                return True
            
            #fire storm
            elif str(action_input) == str(4):
                if wizard.mana < 50:
                    print("Not enough Mana points, pick another option")
                    action_input = input("Enter action: ")
                else:
                    wizard.fire_storm(enemies)
                    for i in enemies:
                        if i.check_life() == 0:
                            enemies.remove(i)
                    return True
                
            # Action to Quit...
            if action_input == "quit":
                print("You Quit the Game...")
                exit()
                
            else:
                print("Please Enter valid input...")
                action_input = input("Enter action: ")



       

            
b = Battle()
b.start()           






