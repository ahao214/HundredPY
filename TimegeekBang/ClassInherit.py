class Monster():
    def __init__(self, hp=100):
        self.hp = hp

    def Run(self):
        print("怪物在跑动")

    def WhoAmI(self):
        print("I am the Monster")


class Animals(Monster):
    def __init__(self, hp=100):
        super().__init__(hp)


class Boss(Monster):
    def __init__(self, hp=500):
        super().__init__(hp)

    def WhoAmI(self):
        print("I am the BOSS")

a1 = Monster(100)
print(a1.hp)
a1.Run()
a1.WhoAmI()

a2 = Animals(200)
print(a2.hp)
a2.Run()

a3 = Boss()
a3.WhoAmI()



