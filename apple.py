from random import randint

def spawn_apple(size):
    x = randint(1, size - 2)
    y = randint(1, size - 2)
    return (x, y)