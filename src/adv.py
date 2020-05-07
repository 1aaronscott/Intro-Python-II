''' adventure game '''
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# create some items
item = {
    'gun': Item("gun", "for the uncivilized"),
    'knife': Item("knife", "for cutting steaks"),
    'plate': Item("plate", "for holding steak"),
    'fork': Item("fork", "for spearking steaks"),
    'couch': Item("couch", "latest sectional from Ikea"),
    'steak': Item("steak", "covered in ketchup"),
}

# and put items in rooms
room['outside'].items = [item['couch']]
room['foyer'].items = [item['gun'], item['steak']]
room['overlook'].items = [item['knife']]
room['narrow'].items = [item['plate']]
room['treasure'].items = [item['fork']]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("zaphod", room["outside"])
#user_name = input("What's your name? ")
##player = Player(user_name, room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
choices = ['q', 'n', 's', 'w', 'e']

move = None
while move != 'q':
    #    print(f"\n{player.who} is in the {player.where_am_i()}\n")
    print(f"\nYou are in the {player.where_am_i()}\n")
    move = input(
        f"\nWhere do you want to go, {player.who_am_i()}? ").lower().split()
    if len(move) == 2:
        print("read in 2 words")
        if move[0] == 'get' or move[0] == 'take':
            pass
    print("move is ", move)
    if len(move) == 1:
        move = move[0]
        print("move is ", move)
        if move == 'q':
            print("You'll never get anywhere in life being a quitter!")
            exit()
        elif move not in choices:
            print(f'\nValid options are q, n, s, w, e')
        elif move == 'n' and player.current_room.n_to is not None:
            player.current_room = player.current_room.n_to
        elif move == 's' and player.current_room.s_to is not None:
            player.current_room = player.current_room.s_to
        elif move == 'e' and player.current_room.e_to is not None:
            player.current_room = player.current_room.e_to
        elif move == 'w' and player.current_room.w_to is not None:
            player.current_room = player.current_room.w_to
    else:
        #    elif player.current_room.n_to is None or player.current_room.s_to is None or player.current_room.e_to is None or player.current_room.w_to is None:
        print("\nYou crazy? You can't do that!\n")
