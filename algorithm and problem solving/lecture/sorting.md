# bubble sort
swap the neighbours starting from left 

```
BubbleSort(arr):
    n = length(arr)
    for i from 0 to n-1:
        for j from 0 to n-i-2:
            if arr[j] > arr[j+1]:
                swap(arr[j], arr[j+1])
```

# selection sort
find the smallest and swap it with the first element of the unsorted list.

```
SelectionSort(arr):
    n = length(arr)a
    for i from 0 to n-1:
        min_index = i
        for j from i+1 to n:
            if arr[j] < arr[min_index]:
                min_index = j
        swap(arr[i], arr[min_index])
```

# insertion sort
build the sorted array one item at a time by comparing each new item to the already sorted items and inserting it in the correct position.

```
InsertionSort(arr):
    n = length(arr)
    for i from 1 to n:
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
```

# merge sort
divide the array into halves, sort each half, and then merge the sorted halves.

```
MergeSort(arr):
    if length(arr) > 1:
        mid = length(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        MergeSort(left_half)
        MergeSort(right_half)

        i = j = k = 0

        while i < length(left_half) and j < length(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < length(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < length(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
```

# quick sort
pick a pivot element, partition the array around the pivot, and recursively sort the partitions.

```
QuickSort(arr, low, high):
    if low < high:
        pi = Partition(arr, low, high)
        QuickSort(arr, low, pi - 1)
        QuickSort(arr, pi + 1, high)

Partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j from low to high - 1:
        if arr[j] < pivot:
            i += 1
            swap(arr[i], arr[j])
    swap(arr[i + 1], arr[high])
    return i + 1
```

# heap sort
build a max heap from the array, then repeatedly extract the maximum element from the heap and rebuild the heap.

```
HeapSort(arr):
    n = length(arr)
    for i from n // 2 - 1 to 0:
        Heapify(arr, n, i)
    for i from n - 1 to 0:
        swap(arr[0], arr[i])
        Heapify(arr, i, 0)

Heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        swap(arr[i], arr[largest])
        Heapify(arr, n, largest)
```

# counting sort
count the occurrences of each element, then use the counts to place the elements in the correct position.

```
CountingSort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * length(arr)

    for i from 0 to length(arr):
        count[arr[i]] += 1

    for i from 1 to max_val + 1:
        count[i] += count[i - 1]

    for i from length(arr) - 1 to 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    for i from 0 to length(arr):
        arr[i] = output[i]
```