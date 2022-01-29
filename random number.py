import random

mylist = []

for i in range(0, 100):
    x = random.randint(1, 100)
    mylist.append(x)
print(mylist)

max_value = max(mylist)
print('Maximum is: ', max_value)

min_value = min(mylist)
print('Minimum is: ', min_value)
