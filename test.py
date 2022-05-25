def quicksort(array):
    less = []
    pivotList = []
    more = []
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        for i in array:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quicksort(less)
        more = quicksort(more)
        return less + pivotList + more


numbers = [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]
print(numbers)
numbers = quicksort(numbers)
print(numbers)
