def get_squares(n):
    return [a ** 2 for a in range(n)]


def get_squares_generator(n):
    for a in range(n):
        yield a ** 2


def get_squares_yield_from(start, end):
    yield from (a ** 2 for a in range(start, end))


def counter(start=0):
    current = start
    while True:
        yield current
        current+= 1


print(get_squares(6))

squares = get_squares_generator(6)
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))

yielder = get_squares_yield_from(4, 23)
print(next(yielder))
print(next(yielder))
print(next(yielder))
print(next(yielder))
print(next(yielder))

my_counter = counter()
for i in range(24):
    print(next(my_counter))

