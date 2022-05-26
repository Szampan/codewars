def move_zeros(array):
    return list(filter(lambda x: x != 0, array)) + [0] * array.count(0)


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))