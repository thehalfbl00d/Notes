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
// Add example code here
```


