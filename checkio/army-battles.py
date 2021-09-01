# Taken from mission The Warriors

from itertools import count


class Warrior:
    def __init__(self) -> None:
        super().__init__()
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self) -> None:
        super().__init__()
        self.attack = 7


def fight(unit_1, unit_2):
    for round_ in count():
        if not (unit_1.is_alive and unit_2.is_alive):
            break

        if round_ % 2:
            unit_1.health -= unit_2.attack
        else:
            unit_2.health -= unit_1.attack

    return unit_1.is_alive


class Army(object):
    def __init__(self) -> None:
        self.units = []

    def add_units(self, cls, number):
        self.units.extend(cls() for _ in range(number))


class Battle(object):
    def fight(self, my_army, enemy_army):
        while my_army.units and enemy_army.units:
            my_unit_won = fight(my_army.units[0], enemy_army.units[0])
            if my_unit_won:
                enemy_army.units.pop(0)
            else:
                my_army.units.pop(0)

        return bool(my_army.units)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False

    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Warrior, 20)
    army_2.add_units(Warrior, 21)
    battle = Battle()
    assert battle.fight(army_1, army_2) == True
