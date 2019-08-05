from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key,'=',value)

for ch in 'ABCD':
    print(ch)

print("isinstance('abc', Iterable) =", isinstance('abc', Iterable))
print("isinstance([1,2,3], Iterable) =", isinstance([1,2,3], Iterable))
print("isinstance(123, Iterable) =", isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
    
for x, y in [(1,1), (2,4), (3,9)]:
    print(x, y)


def findMinAndMax(L):
    if len(L) > 0:
        max = L[0]
        min = L[0]
        for i in L:
            if i > max:
                max = i
            if i < min:
                min = i
        return (min, max)
    return (None, None)

if findMinAndMax([]) != (None, None):
    print('1测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('2测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('3测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('4测试失败!')
else:
    print('测试成功!')