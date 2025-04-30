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
    
]