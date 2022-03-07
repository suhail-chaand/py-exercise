"""Check if a number is divisible by 
    i. 5 => print 'five'
    ii. 3 => print 'three'
    iii. 15 => print 'fifteen'
"""
num = int(input('Enter an Integer '))
# A number divisible by 15 is also divisible by 5 and 3
if num%15==0:
    print('fifteen')
elif num%5==0:
    print('five')
elif num%3==0:
    print('three')
else: print('NA')