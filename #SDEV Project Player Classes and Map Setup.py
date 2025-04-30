# SDEV Project Player Classes and Map Setup

# Player class initializer - These values are placeholders
class Player:
    def __init__(self):
        self.name = ''
        self.hp = 50
        self.mp = 0
        self.strength = 10
        self.endurance = 10
        self.faith = 10
        self.location = 'starting location'

# Creating an instance of the Player class
myPlayer = Player()

# Map setup
# Using nested dictionaries to create a grid for the map in order to navigate in the text RPG using
# the words 'up, down, left, right, north, south, east, west,' etc.

# Basic layout
# 
#      _______
# a1-a3|_|_|_|
# b1-b3|_|X|_|
# c1-c3|_|_|_|
# d1-d3|_|_|_|
# X = starting position

# Keywords set equal to the words corresponding to their commands in the game
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED_COMBAT_FIN = False  # Set the solved state or 'combat finished' state to False
UP = ('up', 'north')
DOWN = ('down', 'south')
RIGHT = ('right', 'east')
LEFT = ('left', 'west')

# Catalog of completed zones for the game engine
FINISHED_ROOMS = {
    'a1': False, 'b1': False, 'c1': False, 'd1': False,
    'a2': False, 'b2': False, 'c2': False, 'd2': False,
    'a3': False, 'b3': False, 'c3': False, 'd3': False
}

# Zonemap setup
zonemap = {
    'a1': {
        DESCRIPTION: "",
        EXAMINATION: 'examine',
        SOLVED_COMBAT_FIN: False,  # Set the solved state or 'combat finished' state to False
        UP: ('up', 'north'),
        DOWN: ('down', 'south'),
        RIGHT: ('right', 'east'),
        LEFT: ('left', 'west')
    }
}

