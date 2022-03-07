"""Find the second largest number from a list of integers"""
l = int(input('Enter length of the list: '))
my_list = list(map(int, input('Enter the list of integers: ').split()))[:l]
my_list.remove(max(my_list))
print(max(my_list))