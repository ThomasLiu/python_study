import os

# print(os.name)
# print(os.uname())
# print('os.environ =', os.environ)

# print('PATH = ',os.environ.get('PATH'))

# print('x = ', os.environ.get('x', 'default'))

# print("os.path.abspath('.') =", os.path.abspath('.'))

# path = os.path.abspath('.')
# will_new_path = os.path.join(path, 'test_dir')
# print('will_new_path=', will_new_path)

# # os.mkdir(will_new_path)

# # os.rmdir(will_new_path)

# test_ps_path = os.path.join(path, 'test.txt')
# ps = os.path.split(test_ps_path)
# print(ps)
# ps = os.path.splitext(test_ps_path)
# print(ps)

# all_file = [x for x in os.listdir('.') if os.path.isdir(x)]
# print('all_file =', all_file)

# all_py_file = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
# print('all_py_file =', all_py_file)

def find_file_by_name(name, path='.'):
    all_dir = os.listdir(path)
    for dir_item in all_dir:
        item_path = os.path.join(path, dir_item)
        if os.path.isdir(item_path): 
            find_file_by_name(name, item_path)
        elif os.path.isfile(item_path) and os.path.split(item_path)[1].find(name) >= 0:
            print(item_path)
            
find_file_by_name('test')

