
def sq_arr1(arr):
    # iter over array
    for i, v in enumerate(arr):
        # mult by itself
        arr[i] = v**2
    # sort mutated array
    arr = sorted(arr)
    arr.sort()
    return arr