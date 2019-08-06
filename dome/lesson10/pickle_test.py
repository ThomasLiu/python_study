import pickle
d = dict(name='Bob', age=20, score=88)
b = pickle.dumps(d)
print('b=', b)

with open('pickle_test.txt', 'wb') as f:
    pickle.dump(d, f)

with open('pickle_test.txt', 'rb') as f:
    dd = pickle.load(f)
    print('dd=', dd)

import json
j = json.dumps(d)
print('j=', j)
jd = json.loads(j)
print('jd=', jd)

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)