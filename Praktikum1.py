class hero:
    pass

hero1 = hero()
hero2 = hero()

hero1.name = "Superman"
hero2.name = "Batman"

hero1.power = "kuat"
hero2.power = "pintar"

print(hero1.name)
print(hero2.name)
print(hero1.power)
print(hero2.power)

print(hero1.__dict__)
print(hero2.__dict__)
