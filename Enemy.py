import random

class Enemy:
    def __init__(self, name, bio, health, strength, defense):
        self.name = name
        self.bio = bio
        self.health = health
        self.strength = strength
        self.defense = defense

    def attack(self):
        return random.randint(1, 20) + self.strength  # d20 roll

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.health -= actual_damage
        return actual_damage

    def display_info(self):
        return (
            f"{self.name}: {self.bio}\n"
            f"Health: {self.health}, Strength: {self.strength}, Defense: {self.defense}"
        )

# Basic enemy list allowing for multiple iterations
enemies = [
    Enemy("Bloodfang Orc", "A brutal warrior fueled by rage and conquest.", 80, 10, 4),
    Enemy("Hollowborn", "A cursed revenant trapped between life and death.", 90, 8, 5),
    Enemy("Whispering Plague", "A sentient mist that corrupts all it touches.", 70, 6, 3),
    Enemy("Dreadmonger", "A nightmare entity that warps the minds of its victims.", 100, 9, 6),
    Enemy("Black Maw", "A living abyss that devours everything in its path.", 120, 13, 7),
    Enemy("Marionette of Sorrow", "A cursed puppet controlled by an unknown force.", 60, 7, 3),
    Enemy("Pale Choir", "Ghostly echoes that sing their victims into oblivion.", 85, 5, 4),
    Enemy("Boneharvest Lich", "A skeletal sorcerer who collects the souls of the damned.", 110, 11, 6),
    Enemy("Ghastwalker", "A spectral hunter that prowls the realms of the living.", 75, 9, 4),
    Enemy("Voidborn Horror", "A monstrous being from beyond reality itself.", 130, 14, 8),
    Enemy("Void Reaper", "An unstoppable hunter, forged from nanotechnology and vengeance.", 150, 18, 9),
    Enemy("Cyber Lich", "A necromancer fused with machines, controlling armies of undead drones.", 140, 16, 8),
    Enemy("Mecha Warlord", "A towering war machine, built for slaughter and programmed for conquest.", 200, 20, 10),
    Enemy("Bloodstorm Striker", "An elite assassin who feeds off adrenaline and carnage.", 120, 17, 7),
    Enemy("Omega Behemoth", "A monstrous fusion of flesh and steel, designed for total annihilation.", 250, 25, 12),
    Enemy("Neurophage", "A virus-powered entity that devours minds and leaves only hollow husks.", 100, 12, 6),
    Enemy("Hellscream Berserker", "A genetically enhanced soldier, driven by fury and bloodlust.", 130, 19, 8),
    Enemy("Xenofang Devourer", "An alien horror with insatiable hunger, tearing through civilizations.", 180, 21, 10),
    Enemy("Doombound Revenant", "A resurrected warrior fueled by endless hatred and a thirst for revenge.", 160, 20, 9),
    Enemy("Spectral Executioner", "A ghost-like assassin that phases through dimensions to claim its victims.", 110, 15, 7),
    Enemy("Warlord", "A ruthless leader commanding mercenary forces for profit and power.", 150, 18, 9),
    Enemy("Cartel Enforcer", "A cold-blooded killer working for a criminal syndicate.", 140, 16, 8),
    Enemy("Elite Hitman", "A highly trained assassin with a near-perfect track record.", 120, 17, 7),
    Enemy("Cyberterrorist", "A hacker with the power to collapse financial systems and infrastructure.", 100, 12, 6),
    Enemy("Urban Raider", "A violent gang leader ruling the streets with fear.", 130, 19, 8),
    Enemy("Black Ops Operative", "An agent trained for covert assassinations and political warfare.", 160, 20, 9),
    Enemy("Weapons Dealer", "A ruthless arms trader fueling global conflicts.", 110, 15, 7),
    Enemy("Militia Commander", "A war-hardened tactician leading insurgent forces.", 180, 21, 10),
    Enemy("Corrupt Official", "A powerful figure who manipulates policies for personal gain.", 90, 10, 5),
    Enemy("Rogue Scientist", "A genius whose unethical experiments could change or destroy the world.", 130, 17, 7),
]

# Enemy encounter system
def encounter_enemy():
    enemy = random.choice(enemies)  # Select a random enemy
    print("\nThe Enemy is Upon You!")
    print(enemy.display_info())  # Show enemy details
    return enemy

# Example usage:
current_enemy = encounter_enemy()