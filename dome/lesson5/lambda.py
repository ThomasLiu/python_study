

l = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print('l=', l)

f = lambda x: x * x
print('f=', f)
print('f(5)=', f(5))


def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
print('L=', L)

L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print('L=', L)