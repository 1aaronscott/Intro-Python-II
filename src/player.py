''' define the Player class '''
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    ''' Defines the player class.
    Input: who = name of player
    current_room = what room they're in
    '''

    def __init__(self, who, current_room, items=[]):
        self.current_room = current_room
        self.who = who
        self.items = items

    def who_am_i(self):
        ''' returns the name of player '''
        return self.who

    def where_am_i(self):
        ''' returns the location of player '''
        return self.current_room

    def get(self, thing):
        ''' method for picking up an item
        added to player
        removed from current room '''
        self.items.append(thing)
        self.current_room.items.remove(thing)

    def drop(self, thing):
        ''' method for dropping an item 
        removed from player
        added to current room '''
        self.items.remove(thing)
        self.current_room.items.append(thing)

    def __str__(self):
        ''' Print the stuff user is holding '''

        my_junk = "You've got:\n"

        for thing in self.items:
            my_junk += f'''\t{thing.name} - {thing.description}\n'''

        return my_junk
