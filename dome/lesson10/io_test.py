
try:

    f = open('test.txt','r')
    print(f)
    f_str = f.read() # 自可以调用一次，调用两次没有效果
    print(f_str)
    print('f.read() = ', f.read())
finally:
    if f:
        f.close()


with open('test.txt','r') as f:
    print('with: ', f.read())

with open('test.txt','r') as f:
    for line in f.readlines():
        print('line =', line)
        print('line.strip() =', line.strip()) # 把末尾的'\n'删掉
    

with open('test.jpeg','rb') as f:
    # print('with: ', f.read())
    pass

with open('w_test.txt', 'w') as f:
    f.write('Hello, world!')


with open('w_test.txt', 'r') as f:
    print('with: ', f.read())