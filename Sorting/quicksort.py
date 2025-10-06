def quick_sort(array):
    if len(array) == 0: return []

    a,b,c = array[0], b[len(array)//2], c[-1]

    pivot = array[-1]
    left, right = [], []
    for i in range(len(array) - 1):
        if array[i] <= pivot:
            left.append(array[i])
        else:
            right.append(array[i])
    return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == "__main__":
    array = [1,4,3,2,66,5,44,67,54,3,4,7,0,6]
    result = quick_sort(array)
    print(array)
    print(result)

#PIVOT random element => O(n * log n) 