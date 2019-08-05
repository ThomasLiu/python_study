import functools
import time

def now():
    print('now func')

f = now
f()

print('now.__name__ = ', now.__name__)
print('f.__name__ = ', f.__name__)


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now1():
    print('now1 func')

now1()
f1 = now1
f1()

print('now1.__name__ = ', now1.__name__)
print('f1.__name__ = ', f1.__name__)


def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log2('execute')
def now2():
    print('now2 func')

now2()
f2 = now2
f2()

print('now2.__name__ = ', now2.__name__)
print('f2.__name__ = ', f2.__name__)


def log3(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log4(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log3
def now3():
    print('now3 func')

@log4('execute')
def now4():
    print('now4 func')


now3()
f3 = now3
f3()

print('now3.__name__ = ', now3.__name__)
print('f3.__name__ = ', f3.__name__)


now4()
f4 = now4
f4()

print('now4.__name__ = ', now4.__name__)
print('f4.__name__ = ', f4.__name__)



def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('%s executed in %s ms' % (fn.__name__, time.time()))
        return fn(*args, **kw)
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')