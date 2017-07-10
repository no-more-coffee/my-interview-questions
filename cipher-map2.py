def generate_4(cipher_grille, ciphered_password):
    for i in range(4):
        for j in range(4):
            if cipher_grille[i][j] == 'X':
                yield (ciphered_password[i][j])


def generate_all(cipher_grille, ciphered_password):
    for i in range(4):
        yield from generate_4(cipher_grille, ciphered_password)
        cipher_grille = list(zip(*cipher_grille[::-1]))


def recall_password(cipher_grille, ciphered_password):
    return ''.join(generate_all(cipher_grille, ciphered_password))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
