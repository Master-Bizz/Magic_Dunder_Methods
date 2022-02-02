# Magic or Dunder methods
x = (32+8)
print(32+8)
print(int.__add__(32,8))
print(dir(x))

print('r'+ 't')
print(str.__add__('r','t'))

from todo import Todo

k_william = Todo(name = 'William')
print(k_william)
print(repr(k_william))  # repr = representation
u_william = Todo(name = 'Uilliam')
print(str(k_william))
print(str(u_william))
print(u_william)
print(repr(u_william))

print(len(k_william))
k_william.add('Buy Salad')
k_william.add('get money')
k_william.add('gain health & wealth')
print(len(k_william))

print(k_william > u_william)
print(k_william < u_william)
