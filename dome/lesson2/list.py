
a = ['a','b','c']
print('a:', a)
print('a[0]:', a[0])
print('a[1]:', a[1])
print('a[2]:', a[2])
print('a[-1]:', a[-1])
print('a[-2]:', a[-2])
print('a[-3]:', a[-3])
print('len(a):', len(a))

a.append('d')
print("after a.append('d'), a:", a)

a.insert(1, 'a1')
print("after a.insert(1, 'a1'), a:", a)
print("a.pop() =", a.pop())
print("after a.pop(), a:", a)

a[1] = 'a2'
print("after a[1] = 'a2', a:", a)

a.append(5)
print("after a.append(5), a:", a)
a.append(['e',7])
print("after a.append(['e',7]), a:", a)
print('a[5][1]:', a[5][1])


# tuple和list非常类似，但是tuple一旦初始化就不能修改
b = ('a', 'b', 'c')
print('b:', b)

c = ('a', 'b', 'c', [1,2])
print('c:', c)
c[3][1] = 3
print('after c[3][1] = 3, c:', c)

d = (1)
print('d:', d)
e = (1,)
print('e:', e)
print('d == e ?', d == e)