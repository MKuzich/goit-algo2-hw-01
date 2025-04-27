def minMax(arr):
    if not arr:
        return None

    if len(arr) == 1:
        return arr[0], arr[0]

    mid = len(arr) // 2
    left_min_max = minMax(arr[:mid])
    right_min_max = minMax(arr[mid:])

    return min(left_min_max[0], right_min_max[0]), max(left_min_max[1], right_min_max[1])

arr = [3, 2, 1, 5, 4]
print(f"Minimum and Maximum of the array are: {minMax(arr)}")