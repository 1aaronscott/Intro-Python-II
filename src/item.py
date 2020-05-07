''' Items held by players or found in rooms.
Part of the text adventure game'''


class Item():
    ''' Items held by players or found in rooms.
    Base class for specialized item types.'''

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        ''' Status message from taking an item '''
        print(f'{self.name} taken!')

    def on_drop(self):
        ''' Status message for dropping an item '''
        print(f'{self.name} dropped!')
