class Hero:

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


hero1 = Hero("Kirito",100, 250, 25)
hero2 = Hero("Asuna",100, 175, 50)
hero3 = Hero("Berak",150, 200, 0)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)