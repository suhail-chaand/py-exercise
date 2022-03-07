"""Print all odd numbers between num1 and num2"""
num1 = int(input('Num-1: '))
num2 = int(input('Num-2: '))
print('The odd numbers are: ',end='')
for num in range(num1+1,num2):
    if num%2!=0:
        print(num,end=' ')
print()