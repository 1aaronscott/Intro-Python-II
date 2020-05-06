''' define the Player class '''
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    ''' Defines the player class.
    Input: who = name of player
    current_room = what room they're in
    '''

    def __init__(self, who, current_room):
        self.current_room = current_room
        self.who = who
