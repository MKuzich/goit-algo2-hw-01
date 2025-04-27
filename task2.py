def serch_kth_smallest(arr, k):
    if k < 1 or k > len(arr):
        return None

    def partition(left, right, pivot_index):
        pivot_value = arr[pivot_index]

        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left
        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1

        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index

    left, right = 0, len(arr) - 1
    while True:
        pivot_index = (left + right) // 2
        pivot_index = partition(left, right, pivot_index)
        
        if pivot_index == k - 1:
            return arr[pivot_index]
        elif pivot_index < k - 1:
            left = pivot_index + 1
        else:
            right = pivot_index - 1

arr = [3, 2, 1, 5, 4]
k = 3
print(f"The {k}-th smallest element is: {serch_kth_smallest(arr, k)}")