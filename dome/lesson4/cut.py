
L = list(range(100))
print(L[:10])
print(L[-10:])
print(L[10:20])
print(L[:10:2])
print(L[::5])
print(L[:])

print((1,2,3,4)[:3])

print('ABCDEFG'[:3])
print('ABCDEFG'[::2])

def trim(s):
    if s[:1] == ' ':
        s = trim(s[1:])
    elif s[-1:] == ' ':
        s = trim(s[:-1])
    return s
    
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')