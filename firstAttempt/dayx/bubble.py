def bubbleSort(array):
    minimum = array[0]
    for i in range(len(array) - 1):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    print(array)

a = [4, 2, 1, 8, 9, 10, 3, 13]
bubbleSort(a)