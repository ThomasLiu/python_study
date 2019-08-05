

print(r'\u4e2d\u6587 is', '\u4e2d\u6587' )


print(r"'ABC'.encode('ascii') == b'ABC' ?", 'ABC'.encode('ascii') == b'ABC')
print(r"b'ABC'.decode('ascii') == 'ABC' ?", b'ABC'.decode('ascii') == 'ABC')

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(r"b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')=", b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
print('Age: %s. Gender: %s' % (25, True))
print('%.2f' % 3.1415926)

x=72
y=85
r=(y-x)/x*100
print("小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.xx%'，只保留小数点后2位：")
print('Hello, {0}, 成绩提升了 {1:.2f}%'.format('小明', r))
print('Hello, %s, 成绩提升了 %.2f%%' % ('小明', r))

a = input('Input a character:')
print('ord():', ord(a))

b = input('Input a number:')
print('chr():', int(chr(b)))

