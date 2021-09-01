def checkio(number):
    birds, fed_birds, minutes = 1, 1, 1
    while number > birds:
        number -= birds
        fed_birds = birds
        minutes += 1
        birds += minutes
    return max((fed_birds, number))
