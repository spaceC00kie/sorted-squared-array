

# [-2, -1, 0, 2, 3]

def sq_arr(arr):
    # iter over array
    for i, v in enumerate(arr):
        # mult by itself
        arr[i] = v**2
    # sort mutated array
    arr = sorted(arr)
    arr.sort()
    return arr


print(sq_arr([-2, -1, 0, 2, 3]))

