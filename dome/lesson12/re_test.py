import re

r = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print('r=', r)
r = re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
print('r=', r)

s = 'a b   c'.split(' ')
print('s=', s)
s = re.split(r'\s+', 'a b   c')
print('s=', s)
s = re.split(r'[\s\,]+', 'a,b, c  d')
print('s=', s)
s = re.split(r'[\s\,\;]+', 'a,b;; c  d')
print('s=', s)

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print('m.group(0) =', m.group(0))
print('m.group(1) =', m.group(1))
print('m.group(2) =', m.group(2))

t = '19:05:30'

m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print('m.groups() =', m.groups())

print(re.match(r'^(\d+)(0*)$', '102300').groups())
print(re.match(r'^(\d+?)(0*)$', '102300').groups())


re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())


def is_valid_email(addr):
    return re.match(r'^(\w+[\.|\_]*\w+)@(\w+)\.([a-zA-Z]+)$', addr)

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

def name_of_email(addr):
    r = re.match(r'^<(\w+\s*\w+)>', addr)
    r2 = re.match(r'^(\w+[\.|\_]*\w+)@', addr)
    if r:
        print('r.groups() =', r.groups()) 
        return r.group(1)
    elif r2:
        print('r2.groups() =', r2.groups()) 
        return r2.group(1)
    else:
        return None

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
