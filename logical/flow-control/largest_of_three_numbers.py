"""Find the largest of three numbers"""
num1 = int(input('Num-1: '))
num2 = int(input('Num-2: '))
num3 = int(input('Num-3: '))
if num1>num2:
    if num1>num3:
        print('The largest number is {}'.format(num1))
    else:
        print('The largest number is {}'.format(num3))
else:
    if num2>num3:
        print('The largest number is {}'.format(num2))
    else:
        print('The largest number is {}'.format(num3))