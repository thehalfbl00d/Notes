# Syntax
```c
array_data_type array_name[size];
```
- Can only store data of one type.

## Symbolic Names
- Prevents hard coding, declared once at the top.

```c
#define SIZE 20
```
- Note: Try making symbolic names bold.

# Multi-dimensional Arrays

## 2D Array:
```c
int array[3][2]; // This is a 3x2 array, 3 rows and 2 columns.
```

### Initializing 2D Array:
Method 1 (automatically does the job for you):
```c
int number[2][3] = {1, 2, 3, 4, 5, 6};
```

Method 2 (artistic):
```c
int numbers[2][3] = {1, 2, 3,
                     4, 5, 6};
```

Method 3 (artistic):
```c 
int numbers[2][3] = {{1, 2, 3},
                     {4, 5, 6}};
```

# Pointers

## Pointer Variables
```c
int *variable; // You need to declare the data type of the pointer variable.
char *character;
```

### Dereference Pointer
```c
int var;
int *var1;

var1 = &var;
printf("%d", *var1);
```

- Declaring more than one pointer at a time:
```c
    int *ptr1, *ptr2, *ptr3; ✅
    int *ptr1, ptr2, ptr3; ❌
```


# Array and Pointers;

a is equal to &a[0]
a + 1 is equal to &a[1]
a + 2 is equal to &a[2]

      *(a + 2) is equal to a[2]
pointer notation     subscript notation

# Dynamic Memory Allocation

## malloc() function
allocates continuous block of memory(Bytes) and returns the starting point:
```c
    pointer = malloc(size);
    free(pointer); // don't forget to free the pointer to save space
```

## calloc() function
does it differently:
- note: initializes everything with 0
```c
    pointer = calloc(number_of_data_items, size_of_each_element);

```

## realloc() function
reallocates the memory block:

```c
pointer = realloc(pointer, new_size)
```
