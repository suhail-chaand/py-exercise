"""Check if the input year is a leap year
    A year is a leap year if:
        - it is divisible by 4 and not by 100
        - it is divisible by 4, 100 and 400
"""
yr=int(input('Enter a year '))
if yr%4==0:
    if yr%100==0:
        if yr%400==0:
            print('The year is a leap year')
        else:
            print('The year is not a leap year')
    else:
        print('The year is a leap year')
else:
    print('The year is not a leap year')