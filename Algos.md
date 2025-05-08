
### Insertion Sort:

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Shift elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# Example usage
arr = [9, 3, 5, 1, 4]
insertion_sort(arr)
print("Sorted array:", arr)
```

### Selection Sort

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i  # Assume current is the smallest

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Found smaller element

        # Swap the found minimum with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example usage
arr = [9, 3, 5, 1, 4]
selection_sort(arr)
print("Sorted array:", arr)
```

### Merge Sort
```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Midpoint
        left = arr[:mid]
        right = arr[mid:]

        # Recursively sort both halves
        merge_sort(left)
        merge_sort(right)

        # Merge the sorted halves
        i = j = k = 0

        # Merge while both have elements
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Leftovers
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Example usage
arr = [9, 3, 5, 1, 4]
merge_sort(arr)
print("Sorted array:", arr)
```

### Tower of Hanoi

```python
def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)

# Example usage
tower_of_hanoi(3, 'A', 'B', 'C')
```
