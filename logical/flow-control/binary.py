"""Compute the binary equivalent of an integer"""
num = int(input("Enter an Integer: "))
bin_list = []
print('Binary equivalent of {} is '.format(num), end='')
while num!=0:
    bin_list.append(num%2)
    num = num//2
for i in range(len(bin_list)):
    print(bin_list[i],end='')
print()