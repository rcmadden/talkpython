
# fibonacci numbers
# 1, 1, 2, 3, 5, 8, 13, 21, ...

def fibonacci(limit):
    nums = []

    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current

        nums. append(current)
    return nums

print(fibonacci(100))

for n in fibonacci(100):
    print(n, end=', ')


def fibonacci_co():
    current = 0
    next = 1

    # while current < limit:
    while True:
        current, next = next, next + current
        yield current

print('with yield')
for n in fibonacci_co():
    if n > 1000:
        break
    print(n, end=', ')