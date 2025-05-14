
# C
### Insertion Sort:


```c
void insertionSort(int arr[], int n) {

    for (int i = 1; i < n; i++) {
        int key = arr[i];  // element to be inserted
        int j = i - 1;
        
        // Move elements greater than key to one position ahead
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        // Place key at the correct position
        arr[j + 1] = key;
    }
}
```

### Selection Sort

```c
#include <stdio.h>
// Selection Sort function
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;

        // Find the smallest element in the unsorted part
        for (int j = i + and 1; j < n; j++) {
            if (arr[j] < arr[min_idx])
                min_idx = j;
        }

        // Swap it with the first element of the unsorted part
        if (min_idx != i) {
            int temp = arr[i];
            arr[i] = arr[min_idx];
            arr[min_idx] = temp;
        }
    }
}
```

### Merge Sort
```c
void merge(int arr[], int left, int mid, int right) {

    int n1 = mid - left + 1;
    int n2 = right - mid;

    int L[n1], R[n2];
    
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;

    while (i < n1 && j < n2)
        arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
        
    while (i < n1)
        arr[k++] = L[i++];
    while (j < n2)
        arr[k++] = R[j++];

}

void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }

}
```

### Bubble Sort

```c
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // swap arr[j] and arr[j+1]
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
```

### Binary Search
```c
int binarySearch(int arr[], int n, int target) {
    int low = 0, high = n - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;  // safer than (low + high) / 2

        if (arr[mid] == target)
            return mid;  // target found

        if (arr[mid] < target)
            low = mid + 1;  // go right
        else
            high = mid - 1; // go left
    }
}
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
### Power
```python
def power(num, exp):
    if exp == 1:
        return num
    return num * power(num, exp - 1)

print(power(2, 2))
```

# Haskell

```haskell
-- GCD using Euclidean algorithm
gcd' :: Int -> Int -> Int
gcd' a 0 = a
gcd' a b = gcd' b (a `mod` b)

-- Fibonacci
fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib (n - 1) + fib (n - 2)

-- Factorial
factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n - 1)
```


## Time Complexity
| **Algorithm**      | **Best Case** | **Average Case** | **Worst Case** | **Space Complexity** |
| ------------------ | ------------- | ---------------- | -------------- | -------------------- |
| **Bubble Sort**    | O(n)          | O(n²)            | O(n²)          | O(1)                 |
| **Selection Sort** | O(n²)         | O(n²)            | O(n²)          | O(1)                 |
| **Insertion Sort** | O(n)          | O(n²)            | O(n²)          | O(1)                 |
| **Merge Sort**     | O(n log n)    | O(n log n)       | O(n log n)     | O(n)                 |
| **Quick Sort**     | O(n log n)    | O(n log n)       | O(n²)          | O(log n) (stack)     |
| **Heap Sort**      | O(n log n)    | O(n log n)       | O(n log n)     | O(1)                 |