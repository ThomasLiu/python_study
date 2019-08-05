
# 重复元素在set中自动被过滤
s = set([1, 1, 2, 2, 3, 3])
print('s=',s)

s.add(1)
print('After s.add(1), s=',s)

s.remove(2)
print('After s.remove(2), s=',s)

s1 = set([1, 2])
s2 = set([2, 3])
print('s1 & s2 =', s1 & s2)
print('s1 | s2 =', s1 | s2)