



# print absolute value of an integer:
a = int(input('input a number:'))
if a >= 0:
    print(a, 'is >= 0')
else:
    print(a, 'is < 0')


x = float(input('输入身高(m)：'))
y = float(input('输入体重(kg)：'))
bmi = y/(x**2)
r = ''
if bmi < 18.5:
    r = '过轻'
elif bmi < 25:
    r = '正常'
elif bmi < 28:
    r = '过重'
elif bmi < 32:
    r = '肥胖'
else:
    r = '严重肥胖'

print('你的BMI为 %s, 属于 %s' % (bmi, r))