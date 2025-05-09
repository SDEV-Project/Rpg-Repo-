import random

class Boss:
    def __init__(self, name, bio, health, strength, defense):
        self.name = name
        self.bio = bio
        self.health = health
        self.strength = strength
        self.defense = defense

    def attack(self):
        return random.randint(1, 20) + self.strength

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.health -= actual_damage
        return actual_damage

    def display_info(self):
        return f"{self.name}: {self.bio}\nHealth: {self.health}, Strength: {self.strength}, Defense: {self.defense}"

# Define a list of bosses
bosses = [
    boss("Grimfang the Cruel", "A monstrous wolf-like beast with razor-sharp claws and a hunger for destruction.", 95, 10, 2),
    boss("Seraphina the Shadowmancer", "A cunning sorceress who commands dark magic and delights in manipulating her foes.", 88, 6, 9),
    boss("Ironclad Gustav", "A heavily armored brute wielding a massive warhammer, crushing all who stand in his way.", 92, 9, 4),
    boss("Vex'thul the Mindbender", "A telepathic entity that preys on the fears and weaknesses of its victims.", 85, 5, 10),
    boss("Queen Morwen the Twisted", "A regal but malevolent ruler who governs with an iron fist and dark sorcery.", 90, 7, 7),
    boss("Kaelen the Undying", "A powerful necromancer who has cheated death countless times and commands legions of undead.", 98, 4, 8),
    boss("Ragnar Bloodfist", "A savage berserker known for his brutal strength and relentless aggression.", 87, 10, 3),
    boss("Silas the Deceiver", "A master of disguise and illusion, capable of tricking even the most perceptive.", 82, 8, 6),
    boss("Pyreheart Ignis", "A fiery elemental being that scorches everything in its path with intense flames.", 94, 9, 5),
    boss("Mistress Evangeline", "A charismatic but ruthless cult leader who controls her followers with dark promises.", 89, 7, 6)

]
