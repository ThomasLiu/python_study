

print('I\'m ok')
print('I\'m "Ok"')
print('yes man1\nI\'m ok')
print('\\\t\\')

# 还允许用r''表示''内部的字符串默认不转义
print(r'\\\t\\')

# 如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
print('''line1
line2
line3
end''')

print(r'''hello,\n
world''')

a = 'ABC'
b = a
a = 'XYZ'
print('b=',b)
print('a=',a)

print('10/3=',10/3)
print('9/3=',9/3)
print('10//3=',10//3)
print('10%3=',10%3)
# Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。
