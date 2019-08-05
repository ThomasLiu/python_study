from functools import reduce

def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))

def f(x):
    return x * x

r = map(f, range(1, 10))
print('r=',r)
print('list(r)=',list(r))

r = map(str, range(1, 10))
print('list(r)=',list(r))

def add2(x, y):
    return x + y

l = [x for x in range(1, 10) if x % 2 == 1]
r = reduce(add2, l)
print('r=',r)

def fn(x, y):
    return x * 10 + y

r = reduce(fn, l)
print('r=',r)

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

r = reduce(fn, map(char2num, '13579'))
print('r=',r)
r = str2int('13579')
print('r=',r)


def normalize(name):
    def up(c):
        o = ord(c)
        if o > 91 and o < 123:
            c = chr(o - 32)
        return c
    def low(c):
        o = ord(c)
        if o > 64 and o < 91:
            c = chr(o + 32)
        return c
    if isinstance(name, str):
        s = up(name[:1])
        for c in name[1:]:
            s += low(c)
        return s
    else:
        print('it is not a str')  

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    def fn(x, y):
        return x * y
    return reduce(fn, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

def str2float(s):
    if isinstance(s, str):
        i, f = s.split('.')
        ii = reduce(lambda x, y: x * 10 + y, map(char2num, i))
        ff = reduce(lambda x, y: x * 0.1 + y, map(char2num, f[::-1]))
        return ii + ff * 0.1
    else: 
        print('it is not a str')  

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')



