def bubble_sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
           print(array)
           break
        
    return array

if __name__ == '__main__':
    x=[1,2,10,4,5]
    print(x)
    bubble_sort(x)
