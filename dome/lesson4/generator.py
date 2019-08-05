

g = (x * x for x in range(10))
for n in g:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(5)
print(f)
for n in f:
    print(n)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

o = odd()
n1 = next(o)
print('next 1', n1)
n2 = next(o)
print('next 2', n2)
n3 = next(o)
print('next 3', n3)

f1 = fib(5)
while True:
    try:
        x = next(f1)
        print('x=', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

def triangles():
    arr = [1]
    while True:
        yield arr
        if len(arr) > 1:
            arr_t = []
            for index, item in enumerate(arr):
                if (index > 0):
                    arr_t.append(arr[index-1] + item)
                else:
                    arr_t.append(1)
            arr_t.append(1)
            arr = arr_t
        else:
            arr = [1,1]

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')