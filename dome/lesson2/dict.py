
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print('Michael:', d['Michael'])

d['Adam'] = 67
print('Adam:', d['Adam'])

print('Bob:', d['Bob'])
d['Bob'] = 70
print("After d['Bob'] = 70, Bob:", d['Bob'])

print('Thomas in d ?', 'Thomas' in d)
print('Thomas:', d.get('Thomas'))
print('Thomas:', d.get('Thomas', 'Not in d'))

d.pop('Bob')
print("After d.pop('Bob'), Bob:", d.get('Bob'))

