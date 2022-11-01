# Data Types: Int Float String Bool
print(1, 4.5, "Hello", False)

name = input('Name: ')

# Arithmetic: + - / * // %
number = input('Number: ')
print(int(number) - 5)

# String Method
hello = 'hello'
print(type(hello))
print(hello.upper())
print(hello.capitalize())
print(hello.count('l'))

# Conditional: if elif else == != <= >= < >
x = input('Name: ')

if x == 'Ivan':
  print('You are correct!')
elif x == 'Tim':
  print('Bye Tim')
elif x == 'Ann':
  print('Bye Ann')
else:
  print('Bye')

# List
y = [4, True, 'hi']
print(len(y))
print(y.append('hello'))
print(y.extend([1,2,3,4,5]))
print(y.pop())
print(y[2])

# Tuple - Immutable list
x = (0,1,2,3,4)

# for loop
for i in range(10):
  print(i)

for i in [2,3,4,5,5]:
  print(i)

x = [x for x in range(5)]
print(x)

# while loop
i = 0
while i < 10:
  print('yes')
  i += 1

# Slice [start:stop:step]
sliced = y[0:4:2]
print(sliced)

# Set - No duplicate - Useful for look ups
x = set()
s = {4, 32, 2, 2}
s2 = {3,4,22,1}
print(s.union(s2))
print(s.difference(s2))

# Dictionary - Key Value Pairs
x = {'key': 4}
print(x['key'])

# Function
def func(x, y):
  print('run', x , y)

func(5, 6)

# Exceptions
try:
  x = 7/0
except Exception as e:
  print(e)

# Lambda
x = lambda x: x + 5

print(x(2))

# Map


# Filter