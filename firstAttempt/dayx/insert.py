def insertSort(alist):
    for index in range(1, len(alist)):
        j = index
        current = alist[index]
        while j > 0 and current < alist[j-1]:
            alist[j] = alist[j-1]
            j = j-1
        alist[j] = current
    print(alist)

a = [4, 2, 1, 8, 9, 10, 3, 13]
insertSort(a)