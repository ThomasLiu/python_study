

import types

def fn():
    pass

print(type(123)==type(456))
print(type(123)==int)
print(type('abc')==type('123'))
print(type('abc')==str)
print(type('abc')==type(123))

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

print(dir('ABC'))

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print("有属性'x'吗？", hasattr(obj, 'x'))
print('obj.x =', obj.x)
print("有属性'y'吗？", hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print("有属性'y'吗？", hasattr(obj, 'y'))
print("getattr(obj, 'y') =", getattr(obj, 'y'))
print('obj.y =', obj.y)
print("getattr(obj, 'z', 404) =", getattr(obj, 'z', 404))

print("有属性'power'吗？", hasattr(obj, 'power'))
print("getattr(obj, 'power') =", getattr(obj, 'power'))
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
print('fn=', fn)
print('fn() =', fn())



class Student(object):
    name = 'Student'

s = Student() # 创建实例s
print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name) # 打印类的name属性
s.name = 'Michael' # 给实例绑定name属性
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
del s.name # 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了


class Student2(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student2.count += 1


# 测试:
if Student2.count != 0:
    print('测试失败!')
else:
    bart = Student2('Bart')
    if Student2.count != 1:
        print('测试失败!')
    else:
        lisa = Student2('Bart')
        if Student2.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student2.count)
            print('测试通过!')