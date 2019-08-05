import math

n1 = 255
n2 = 1000
print('hex(255):', hex(255))
print('hex(1000):', hex(1000))

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x

print('my_abs(11):', my_abs(11))
print('my_abs(-11):', my_abs(-11))
# print("my_abs('x'):", my_abs('x'))


def nop():
    pass

nop()

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny
    

r = move(100, 100, 60, math.pi / 6)
x, y = r
print(r)
print(x, y)


def quadratic(a, b, c):
    ro = b**2 - 4*a*c
    if ro < 0:
        print('该方程没有实根')
        return
    r1 = math.sqrt(ro)
    r2 = (2*a)

    return (-b + r1)/r2, (-b - r1)/r2

rr1 = quadratic(2,3,1)
rr2 = quadratic(1,3,-4)

print('quadratic(2,3,1) = ', rr1)
print('quadratic(1,3,-4) = ', rr2)
print('quadratic(1,1,1) = ', quadratic(1,1,1))


if rr1 != (-0.5, -1.0):
    print('测试失败')
elif rr2 != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n*n
    return sum

print('calc(1,2,3,4) =', calc(1,2,3,4))
print('calc() =', calc())

nums = [1,2,3,4]
print('calc(*nums) =', calc(*nums))

# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Bob', 35, **extra)

# 命名关键字参数
def person2(name, age, *, city, job):
    print('name:', name, 'age:', age, 'city:', city, 'job:', job)

person2('Jack', 24, city='Beijing', job='Engineer')
person2('Jack', 24, job='Engineer', city='Beijing')

# 带可变参数的命名关键字参数定义方式
def person3(name, age, *args, city, job):
    print(name, age, args, city, job)

person3('Jack', 24, city='Beijing', job='Engineer')
person3('Jack', 24, 12, 14, job='Engineer', city='Beijing')

# 参数组合， 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)


def product(x, *args):
    for n in args:
        x *= n
    return x

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))

if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print('fact(1) =', fact(1))
print('fact(5) =', fact(5))

if fact(5) != 120:
    print('测试失败!')
elif fact(1) != 1:
    print('测试失败!')
else:
    try:
        fact(10000)
        print('测试失败!')
    except BaseException as e:
        print('测试成功!', e)

# 尾递归函数

def fact_b(n):
    return fact_item(n, 1)
def fact_item(num, product):
    if num == 1:
        return product
    return fact_item(num-1, num * product)

print('fact_b(1) =', fact_b(1))
print('fact_b(5) =', fact_b(5))

if fact_b(5) != 120:
    print('测试失败!')
elif fact_b(1) != 1:
    print('测试失败!')
else:
    print('测试成功!')


def han_move(n,a,b,c):
    if n == 1:
        print(a, '-->', c)
    else:
        han_move(n-1,a,c,b)
        han_move(1,a,b,c)
        han_move(n-1,b,a,c)

han_move(2,'A','B','C')
print("test han_move(3,'A','B','C')")
han_move(3,'A','B','C')