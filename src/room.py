''' defines the room class '''
# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    ''' Defines the room class.
    Input: loc = name of the room
    description = info about the location
    '''

    def __init__(self, loc, description):
        self.loc = loc
        self.description = description
