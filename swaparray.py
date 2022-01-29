array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if len(array) % 2 == 0:
    for i in range(0, len(array), 2):
        array[i], array[i+1] = array[i+1], array[i]

print(array)
