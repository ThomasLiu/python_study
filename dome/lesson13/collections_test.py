from collections import namedtuple, deque, defaultdict, OrderedDict

Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print('px =', p.x, ',py=', p.y)
print('isinstance(p, Point) =',isinstance(p, Point))
print('isinstance(p, tuple) =',isinstance(p, tuple))

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print('q=', q)


dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print("dd['key1'] =", dd['key1'])
print("dd['key2'] =", dd['key2'])

d = dict([('b', 2), ('a', 1), ('c', 3)])
print('d =', d)

od = OrderedDict([('b', 2), ('a', 1), ('c', 3)])
print('od =', od)