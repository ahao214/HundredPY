class Player():
    def __init__(self, name, ph):
        self.name = name
        self.ph = ph

    def print_role(self):
        print('%s:%s' % (self.name, self.ph))

    def updateName(self, newName):
        self.name = newName


userTom = Player("Tom", 30)
userJerry = Player("Jerry", 28)

userTom.print_role()
userJerry.print_role()

userTom.updateName("Wlian")
userTom.print_role()