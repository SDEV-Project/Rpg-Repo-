import random

class Character:
    def __init__(self, name, bio, health, strength, defense):
        self.name = name
        self.bio = bio
        self.health = health
        self.strength = strength
        self.defense = defense

    def attack(self):
        return random.randint(1, 20) + self.strength  # Simulate a d20 roll

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.health -= actual_damage
        return actual_damage
    

# character list to selct from

characters = [
    Character("Battlion Leader", "A broken man fearless soldier of fortune aimed at success at all costs.", 100, 8, 5),
    Character("Oden", "Mythical swordmaster, weilding an enchanted blade of great power,meant to conquer all.", 80, 10, 3),
    Character("Tom Clancy", "A master spy and man of many skills. His fighting prowess seemily unmatched, ready for challenge", 90, 7, 4),
    Character("Xander Cage", "Stunts and fearlessness are his game, His learning is from the streets and he aint no pushover.", 75, 9, 3),
    Character("Persius Maximus", "From a forgotten time, His skills are centuries old, the last of his kind and skilled assassin.", 85, 7, 6),
    Character("Zeltic De La zues", "A wizard of unbridaled power, Can control time and space with a flickof his staff.", 100, 5, 6),
    Character("Zoric the Brute", "Strenght a plenty and courage to match, this mangy man beast can snap bones like twigs.", 100, 10, 3),
    Character("Braxium Motu", "Warrior sent from the Gods, Good willed and shortfused.", 60, 9, 10),
    Character("Yuzum Opius", "Monk of old turned hunter, His teachings have brought him an unthought of arsenal of heroics.", 100, 7, 7),
    Character("Tonto Grexium", "Losing his family at a young age has readied him for battle, filled with rage and no remorse.", 55, 10, 4),
]


print("Choose your character:")
for i, char in enumerate(characters, 1):
    print(f"{i}. {char.name}: {char.bio}")

choice = int(input("Enter the number of your Hero: ")) - 1
player = characters[choice]
print(f"You have chosen {player.name}! Begin your Journey and God Speed!")
