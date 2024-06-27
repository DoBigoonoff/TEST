def find_index(array):
    total = sum(array)
    leftside = 0
    for i, value in enumerate(array):
        total -= value
        if leftside == total:
            return i
        leftside += value
    return -1

array = (3, 4, 5, 1, 6)
index = find_index(array)
if index != -1:
    print(f"Equilibrium index from array: {index}")
else:
    print("No equilibrium index.")