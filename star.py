'''
object-oriented
'''

class cat():
    def __init__(self, name):
        self.name = ""
        self.weight = 0
        self.colour = ""

    def meow(self):
        print(self.name, " says meow.")

class tiger(cat):
    """docstring for tiger."""
    def __init__(self):
        super(cat, self).__init__()


my_tiger = tiger()
