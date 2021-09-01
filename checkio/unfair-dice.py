def winning_die(enemy_die):
    die = sorted(enemy_die)
    l = len(die)
    if die[-1] > l - 1:
        die[-1] -= l - 1
        for i in range(l - 1):
            die[i] += 1
    else:
        from_last = die[-1] - 1
        from_previous = l - 2 - from_last
        die[-1] = 1
        die[-2] -= from_previous
        for i in range(l - 2):
            die[i] += 1

    if set(die) == set(enemy_die):
        return []

    return die


if __name__ == '__main__':
    # These are only used for self-checking and not necessary for auto-testing
    def check_solution(func, enemy):
        player = func(enemy)
        total = 0
        for p in player:
            for e in enemy:
                if p > e:
                    total += 1
                elif p < e:
                    total -= 1
        # total = sum(1 if p > e else -1 for p in player for e in enemy)
        return total > 0


    assert check_solution(winning_die, [3, 3, 3, 3, 6, 6]), "Threes and Sixes"
    assert check_solution(winning_die, [4, 4, 4, 4, 4, 4]), "All Fours"
    assert check_solution(winning_die, [1, 1, 1, 4]), "Unities and Four"
    # assert winning_die([1, 2, 3, 4, 5, 6]) == [], "All in row -- No die"
    # assert winning_die([2, 3, 4, 5, 6, 7]) == [1, 1, 3, 7, 7, 8], "This can be beat though."
    # assert winning_die([1, 1, 3]) == [1, 2, 2]
    # assert winning_die([2, 2, 5, 5, 5, 5]) == [3, 3, 3, 3, 6, 6]
