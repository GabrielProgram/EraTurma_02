#Curso de Python
#teste
# asldkfjalskdjf çkl
#2020/04/29

while True:
    try:
        a = float(input('Tell me one side of the triangle:\n'))
    except ValueError:
        print('Please insert a valid real number and try again.')
        continue
    else:
        break

while True:
    try:
       b = float(input('Tell me other side of the triangle:\n'))
    except ValueError:
        print('Please insert a valid real number and try again.')
        continue
    else:
        break

while True:
    try:
       c = float(input('Tell me other side of the triangle:\n'))
    except ValueError:
        print('Please insert a valid real number and try again.')
        continue
    else:
        break

Test1 = abs(b - c) < a < (b + c)
Test2 = abs(b - c) < a < (b + c)
Test3 = abs(b - c) < a < (b + c)

Type = 'string'

# Type of the triangle.
if a == b == c:
    Type = 'equilateral'
elif a != b != c:
    Type = 'scalene'
else:
    Type = 'isosceles'


# Notes if it is a triangle and prints the type of the triangle.
if Test1 and Test2 and Test3:
    print('It is a {} triangle.'.format(Type))
else:
    print('It is not a triangle.')

