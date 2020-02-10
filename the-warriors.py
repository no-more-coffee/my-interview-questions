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


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

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

    print("Coding complete? Let's try tests!")
