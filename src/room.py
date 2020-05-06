''' defines the room class '''
# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    ''' Defines the room class.
    Input: loc = name of the room
    description = info about the location
    '''

    def __init__(self, loc, description, n_to=None, s_to=None, e_to=None, w_to=None):
        self.loc = loc
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    # def what_location(self):
    #     '''returns current location of player'''
    #     return self.loc

    # def describe(self):
    #     '''returns description of player's current location'''
    #     return self.description

    def __str__(self):
        #         return f'''Current room: {self.loc}
        # Room description: {self.description}'''
        return f'''{self.loc} (where {self.description})'''
