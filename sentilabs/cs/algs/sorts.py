def quick_sort_3way(arr, left, right):
    def get_pivot_index():
        if right - left < 2:
            return left
        middle = (left + right)//2
        if arr[left] <= arr[middle]:
            if arr[middle] <= arr[right]:
                return middle
            elif arr[left] <= arr[right]:
                return right
            return left
        else: # arr[left] > arr[middle]
            if arr[middle] >= arr[right]:
                return middle
            elif arr[left] >= arr[right]:
                return right
            return left

    if left >= right:
        return

    pi = get_pivot_index()
    compare_to = arr[pi]
    arr[left], arr[pi] = arr[pi], arr[left]
    cur_left = left
    i = cur_left + 1
    cur_right = right
    while i <= cur_right:
        if arr[i] < compare_to:
            arr[cur_left], arr[i] = arr[i], arr[cur_left]
            i += 1
            cur_left += 1
        elif arr[i] > compare_to:
            arr[i], arr[cur_right] = arr[cur_right], arr[i]
            cur_right -= 1
        else:
            i += 1
    quick_sort_3way(arr, left, cur_left - 1)
    quick_sort_3way(arr, cur_right + 1, right)

