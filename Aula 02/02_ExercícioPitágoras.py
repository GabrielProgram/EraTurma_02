#Curso de Python
#2020/04/22

print('This program calculates the Pythagorean Theorem, would you mind inserting the values of two sides of the '
      'triangle and it will give you the third\n')

while True:
    try:
       SideOne = float(input('Please insert the first side of the triangle:\n'))
    except ValueError:
        print('Please insert a valid real number and try again.')
        continue
    else:
        break

while True:
    try:
       SideTwo = float(input('Please insert the second side of the triangle:\n'))
    except ValueError:
        print('Please insert a valid real number and try again.')
        continue
    else:
        break

PyTheo = (SideOne**2 + SideTwo**2)**(1/2)

print('The result is:')
print(PyTheo)