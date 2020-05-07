#Curso de Python
#2020/04/21

print('Delta is equal to b square minus four times a times c:')


while True:
    try:
        a = float(input("Please type the value of a:\n"))
    except ValueError:
        print('Please insert a real number and try again.')
        continue
    else:
        break


while True:
    try:
        b = float(input("Please type the value of b:\n"))
    except ValueError:
        print('Please insert a real number and try again.')
        continue
    else:
        break


while True:
    try:
        c = float(input("Please type the value of c:\n"))
    except ValueError:
        print('Please insert a real number and try again.')
        continue
    else:
        break

delta = b**2 - (4*a*c)

print('The value of Delta is:')
print(delta)