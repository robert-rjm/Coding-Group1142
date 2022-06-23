'''
required libraries
'''
import numpy as np
import random


'''
required class
'''
class Character:
    def __init__(self, name, strength=0, health=0, gamewon=0):
        self.name = name
        self.strength = strength
        self.health = health
        self.gamewon = gamewon
    def __str__(self):
        return f" {self.name}; your strength is {self.strength}, your health is {self.health}"
    def __repr__(self):
        return f"{self}({Character().__str__()})"

class Attribute:
    def __init__ (self, name, strength=0, health=0):
        self.name = name
        self.strength = strength
        self.health = health
    def __str__ (self):
        return f" {self.name}; gives strength {self.strength} and health {self.health}"
    def __repr__(self):
        return f"{self}({Attribute().__str__()})"

class Fighter:
    def __init__ (self, name, attribute=0, strength=0, health=0, gamewon=0):
        self.name = name
        self.attribute = attribute
        self.strength = strength
        self.health = health
        self.gamewon = gamewon
    def __str__(self):
        return f"{self.name} with {self.attribute} (strength {self.strength} and health {self.health})."
    def __repr__(self):
        return f"{self}({Fighter().__str__()})"
    def fight(self, opponent):
        # Basic stuff that must be reset before each fight    
        discounter = 9
        # Loop for the fighting until theres a clear winner
        while True:
            # safety mechanism to ensure the two fighters arent exaclty the same, randomly selected if same strength and health
            if self.health == opponent.health and self.strength == opponent.strength:
                winner = random.choice([self, opponent])
                winner.gamewon += 1
                print(f"No true winner but the winner is {winner} due to a lucky punch")
                break
            # ensuring that if no winner is found after 99990 rounds, either fighter is randomly selected to win 
            discounter += 1
            if discounter >= 10000:
                winner = random.choice([self, opponent])
                winner.gamewon += 1
                print(f"No true winner but the winner is {winner} due to a lucky punch")
                break        
            # damage that each punch causes, based on the strength and the current round
            damage_taken = opponent.strength / discounter
            damage_given = self.strength / discounter
            selfhealth = self.health
            opponenthealth = opponent.health
            # fight until someone has health below 0
            while selfhealth > 0 and opponenthealth > 0:
                selfhealth -= damage_taken
                opponenthealth -= damage_given
            # check whether there is a winner with positive health
            if selfhealth > opponenthealth and selfhealth >= 0:
                self.gamewon += 1
                print(f"The winner is: {self}!\nThe fight took {discounter - 9} round(s)")
                break
            elif opponenthealth > selfhealth and opponenthealth >= 0:
                opponent.gamewon += 1
                print(f"The winner is: {opponent}!\nThe fight took {discounter - 9} round(s)")
                break
            else:
                pass


'''
characters and attributes list
'''
characters = [
    Character("Harry Potter", 100, 100),
    Character("Ron Weasley", 90, 110),
    Character("Draco Malfoy", 120, 80),
    Character("Voldemort", 140, 60)
    ]

attributes = [
    Attribute("Coffee", 50, -10),
    Attribute("Sword", 80, 10),
    Attribute("Protein Shake", 70, 20),
    Attribute("Hat", -20, 40),
    Attribute("Pizza", 40, -30),
    Attribute("Skis", 90, 0),
    Attribute("Vision Goggles", 60, -10)
    ]


'''
Functions
'''
#function to pick the desired fighter
def let_user_pick_C(characters):
    print("Please choose your fighter: ")

    for idx, element in enumerate(characters):
        print("{}) {}".format(idx + 1, element))

    while True:
        try:
            i = int(input(f"\nPlease insert only your fighter number (between 1 an {len(characters)}): "))
        except ValueError:
            continue
        if 0 < i <= len(characters):
            return i - 1

#function to pick attributes
def let_user_pick_A(attributes):
    print("\nPlease choose your weapon: ")

    for idx, element in enumerate(attributes):
        print("{}) {}".format(idx + 1, element))

    while True:
        try:
            i = int(input(f"\nPlease insert only your weapon number (between 1 an {len(attributes)}): "))
        except ValueError:
            continue
        if 0 < i <= len(attributes):
            return i - 1

# function implementing selection
def continue_with_character():
    global res1
    global character_choice
    global attribute_choice
    while True:
        try:
            res1 = let_user_pick_C(characters)
            character_choice = characters[res1]
            print(character_choice)
            res2 = let_user_pick_A(attributes)
            attribute_choice = attributes[res2]
            print(attribute_choice)
            while True:              
                try:
                    x = input(f"\nDo you want to continue with {character_choice.name} and {attribute_choice.name}: yes or no? ")
                    if x.lower() == "no":
                        print("\nPlease reselect a character and chose a new weapon/attribute")
                        break
                    elif x.lower() == "yes":
                        fighter_strength = character_choice.strength + attribute_choice.strength
                        fighter_health = character_choice.health + attribute_choice.health
                        print("Let's start the fight!!!")
                        print(f'Your character has strength {fighter_strength} and health {fighter_health}.')
                        break
                except ValueError:
                    print("Please answer by yes or no.")
        except ValueError:
            continue
        if x.lower() == "yes":
            fighters.append(Fighter(character_choice.name, attribute_choice.name, character_choice.strength + attribute_choice.strength, character_choice.health + attribute_choice.health))
            break

# random attributes
def create_fighters():
    for i in range(0,len(characters)):
        if i == res1:
            continue
        else:
            x = random.randint(0,len(attributes)-1)
            z = Fighter(characters[i].name, attributes[x].name, characters[i].strength + attributes[x].strength, characters[i].health + attributes[x].health)
            fighters.append(z)

def selection_to_fighter():
    global fighters
    fighters = []
    continue_with_character()            
    create_fighters()

# determine the winner 
def winner():
    global first_place
    global second_place
    global third_place
    global last_place
    if TMW[0].gamewon > TMW[1].gamewon:
        first_place = TMW[0]
        second_place = TMW[1]
    elif TMW[1].gamewon > TMW[0].gamewon:
        first_place = TMW[1]
        second_place = TMW[0]
    else:
        raise "Unexpected Error occured"
    if TML[0].gamewon > TML[1].gamewon:
        third_place = TML[0]
        last_place = TML[1]
    elif TML[1].gamewon > TML[0].gamewon:
        third_place = TML[1]
        last_place = TML[0]
    else:
        raise "Unexpected Error occured"
    standing()

# illustrate the ranking
def standing():
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    if character_choice.name == first_place.name:
        print(f"Congratulation on first place! Your fighter won the tournament by winning both fights!")
    elif character_choice.name == second_place.name:
        print(f"Congratulation! Your fighter placed second. You lost the second fight against {first_place.name}")
    elif character_choice.name == third_place.name:
        print(f"Congrats on third place! Better luck next time. The winner of the tournament is {first_place.name}.")
    elif character_choice.name == last_place.name:
        print(f"Better luck next time, your fighter won none of the fights! The winner of the tournament is {first_place.name}")
    else:
        print("An error has occurred")
    print(
        f"""
        The complete tournament ranking is:\n
        First Place goes to: {first_place}
        Second Place goes to: {second_place}
        Third Place goes to: {third_place}
        Last Place goes to: {last_place}
        """
        )
    for i in fighters:
        # reset gamewon to zero
        i.gamewon = 0
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------------------------")

# actual fighting
def fighting():
    global group1
    global group2
    global tournament
    global TMW
    global TML
    global secondleg
    group1 = fighters.copy()
    group2 = []
    x = random.randint(0,3)
    y = random.randint(0,2)
    group2.append(group1[x])
    del group1[x]
    group2.append(group1[y])
    del group1[y]
    tournament = [tuple(group1), tuple(group2)]
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    print("\nTournament fights stage 1:")
    for x, y in tournament:
        print(x.name, "vs", y.name)
    print("\n")
    for x, y in tournament:
        print(f"Fight between {x.name} and {y.name}:")
        x.fight(y)
        print(f"\t {x} \n\t {y} \n")
    TMW, TML = [], []
    for i in fighters:
        if i.gamewon > 0:
            TMW.append(i)
        elif i.gamewon == 0:
            TML.append(i)
    secondleg = ((TMW[0], TMW[1]), (TML[0], TML[1]))
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    print("\nTournament fights stage 2:")
    for x, y in secondleg:
        print(x.name, "vs", y.name)
    print("\n")
    for x, y in secondleg:
        print(f"Fight between {x.name} and {y.name}:")
        x.fight(y)
        print(f"\t {x} \n\t {y} \n")
    winner()
    restart_fight()



# possibility to restart
def restart_fight():
    while True:
        try:
            x = input("\n\nWould you like to start a new tournament? ")
            if x.lower() in ["yes", "no"]:
              break
        except ValueError:
            print("Please answer yes or no")
    if x.lower() == "yes":
        tournament_duel()
    elif x.lower() == "no":
        print("Thank you! Have a nice day!")
    else:
      restart_fight()
        

# full fighting code in one function
def tournament_duel():
    #run this function to start the selection process
    selection_to_fighter()
    # actual fighting
    fighting()


'''
To execute the code, run the following line of code
'''
tournament_duel()

