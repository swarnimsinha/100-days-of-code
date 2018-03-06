def merge(left,right):
    if len(left) == 0:
        return left
    if len(right) == 0:
        return right
    i,j = 0,0
    result = []
    while len(result) < len(left) + len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result

def mergeSort(array):
    if len(array) < 2:
        return array
    middle = len(array)//2
    left = mergeSort(array[:middle])
    right = mergeSort(array[middle:])
    return merge(left, right)

a = [4, 2, 1, 8, 9, 10, 3, 13]
print(mergeSort(a))