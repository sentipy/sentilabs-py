def quick_sort_3way(arr):
    quick_sort_3wayEx(arr, 0, len(arr) - 1)


def quick_sort_3wayEx(arr, left, right):
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
    quick_sort_3wayEx(arr, left, cur_left - 1)
    quick_sort_3wayEx(arr, cur_right + 1, right)


def mergeSort(arr):
    mergeSortEx(arr, 0, len(arr) - 1)


def mergeSortEx(arr, left, right):

    def merge(arr1, arr2):
        newArr = list()
        i1 = 0
        i2 = 0
        len1 = len(arr1)
        len2 = len(arr2)
        while i1 < len1 and i2 < len2:
            if arr1[i1] < arr2[i2]:
                newArr.append(arr1[i1])
                i1 += 1
            else:
                newArr.append(arr2[i2])
                i2 += 1
        while i1 < len1:
            newArr.append(arr1[i1])
            i1 += 1
        while i2 < len2:
            newArr.append(arr2[i2])
            i2 += 1
        return newArr

    if left >= right:
        return
    middle = (left + right)//2
    mergeSortEx(arr, left, middle)
    mergeSortEx(arr, middle + 1, right)
    arr[left:right + 1] = merge(arr[left:middle + 1], arr[middle + 1: right + 1])