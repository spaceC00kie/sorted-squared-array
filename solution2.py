
def sq_arr2(arr):
    # arr
    out = []
    # pointers
    left = 0
    right = len(arr) - 1
    # while pointers haven't crossed
    while left < right:
        # see which one is bigger
        if abs(arr[left]) < abs(arr[right]):
            out.append(arr[right]**2)
            right -= 1
        else:
            out.append(arr[left]**2)
            left += 1
    out.reverse()
    return arr

