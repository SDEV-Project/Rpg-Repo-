import random
from Character import Character, characters  # Import Cahrcter lsit and Attributes
from Enemy import Enemy, enemies, encounter_enemy  # Import enemy list and Attributes

# Player Selection
print("Choose your Hero:")
for i, char in enumerate(characters, 1):
    print(f"{i}. {char.name}: {char.bio}")

choice = int(input("Enter the number of your Hero: ")) - 1
player = characters[choice]
print(f"\nYou have chosen {player.name}! Begin your journey!\n")

# Map Setup
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED_COMBAT_FIN = False
UP = ('up', 'north')
DOWN = ('down', 'south')
RIGHT = ('right', 'east')
LEFT = ('left', 'west')

FINISHED_ROOMS = {
    'a1': False, 'b1': False, 'c1': False, 'd1': False,
    'a2': False, 'b2': False, 'c2': False, 'd2': False,
    'a3': False, 'b3': False, 'c3': False, 'd3': False
}

zonemap = {
    'a1': {
        DESCRIPTION: "A dark and eerie room filled with ancient markings.",
        EXAMINATION: "This place feels haunted, the air is thick with mystery.",
        SOLVED_COMBAT_FIN: False,
        UP: ('up', 'north'),
        DOWN: ('down', 'south'),
        RIGHT: ('right', 'east'),
        LEFT: ('left', 'west')
    }
}

# Game Loop
def start_game(player):
    print(f"\nWelcome, {player.name}! Your journey begins in {player.location}.")

    while player.health > 0:
        print("\nActions: [move] [fight] [rest] [quit]")
        action = input("What do you want to do? ").lower()

        if action == "move":
            move_player(player)
        elif action == "fight":
            enemy = random.choice(enemies)  
            combat(player, enemy)
        elif action == "rest":
            player.health += 20
            print("\nYou rest and recover 20 health!")
        elif action == "quit":
            print("\nThanks for playing!")
            break
        else:
            print("\nInvalid choice, try again.")

    print("\nGame Over! You have failed your quest And died in Battle.")

# Movement Function
def move_player(player):
    print("\nWhere Shall You go? [north] [south] [east] [west]")
    direction = input("Enter direction: ").lower()

    if direction in UP:
        player.location = "moved north"
    elif direction in DOWN:
        player.location = "moved south"
    elif direction in LEFT:
        player.location = "moved west"
    elif direction in RIGHT:
        player.location = "moved east"
    else:
        print("Invalid direction.")

    print(f"\nYou are now at {player.location}.")

# Battle System
def combat(player, enemy):
    print(f"\nA wild {enemy.name} appears! {enemy.bio}")

    while player.health > 0 and enemy.health > 0:
        print(f"\n{player.name}: {player.health} HP | {enemy.name}: {enemy.health} HP")
        
        action = input("Attack or Defend? ").lower()

        if action == "attack":
            damage = player.attack()  # FIXED: Ensure `Player.attack()` exists
            enemy.take_damage(damage)
            print(f"\nYou strike {enemy.name} for {damage} damage!")
        
        if enemy.health > 0:
            enemy_damage = enemy.attack()
            player.take_damage(enemy_damage)  # FIXED: Ensure `Player.take_damage()` exists
            print(f"\n{enemy.name} retaliates for {enemy_damage} damage!")

        if player.health <= 0:
            print(f"\n{player.name} has fallen!")
            return False
        elif enemy.health <= 0:
            print(f"\nYou defeated {enemy.name}!")
            return True

# Start the game with the chosen character
start_game(player)