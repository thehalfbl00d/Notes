# <center> Arrays</center>

## syntax
```c
array_data_type array_name[size];
```
- Can only store data of one type.

## <font color = "red">Symbolic Names</font>
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


```c

for (int i = 0; i < 4; i++){
    scanf("%d", (array + i )); ✅
    scanf("%d", *(array + i)); ❌
}
```

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


# functions

```c
void function(void);
```
^return type    ^parameter type

no need to define names during making signature but is necessary when actually giving it definition


# passing parameters:

## by value

we pass a **COPY** 
```c
add(value) 
```

## By Reference
We pass the address
```c
add(int &num)
```

# Passing an array as parameter

```c
    // Function signature
    int sum_array(int[]);
```

## Passing 2d array as parameter

    when declaring 2d array
    - explicitly declare the number of column, required

```c
// Function signature
int sum_array(int [][COL]);

int array[][19];
```

# Storage classes

## 1. Auto Variable
- all variables defined inside a function are auto by default
```c
auto int num = 10;
```

## 2. Static Variable
- they are permanent to a function
- can be accessed when the function is called again
- os ignores their declaration for example as 0 when called again and holds the earlier value
```c
static int num = 10;
```

## 3. Register Variable
- stored in cpu
- best placed as index variable in a loop
```c
register int x;
```
## Extern Variable
- looks for globally created variables



# Strings

1. A string literal is anything enclosed within a "".
2. A string literal always ends with an NULL character "\0"

To display 
    " in a string you use   \"
    ' in a string you use   \'
    tab in a string you use \t
    to remove a space       \b
    to play alert sound     \a

Note :
In C characters are string of characters
```c
char greeting[6] =  {'H', 'E', 'L', 'L', 'O', '\0'};
char greeting[6] = "Hello";
```

if greeting[10] then the rest will be filled with '\0'

- to display a string in C we can:

```c
    printf("%s", gretting)
    printf("%20s", greeting) // this shifts it right
    printf("%20.3s", greeting) // prints first 3 letters of 20 words
```

## gets() and puts() and scanf()

### puts()
prints string to the terminal / moves the cursor to the next string automatically
```c
    char name[21];
    name = "hello";
    puts(name);
```

### gets()   // depreciated
```c
    char name[21];
    gets(name);
```

this shi deprecated, we use fgets
```c
    fgets(name, SIZE-1, stdin);
```

### scanf
this starts tweaking when we put a space, use fgets
```c
    char name[21];
    scanf("%s", name);
```

## pointer initialization of string

- char greeting[6] =  {'H', 'E', 'L', 'L', 'O', '\0'};
- char greeting[6] = "Hello";

```c
char *ptr = "Hello";  // this also puts a null character hence occupying 6 characters
```

note :

```c 
char *p = "hi";
char array[10] = "hi"

p = array; // this is ok as p is a memory address and they are mutable
array = p  // this is not ok
```

## String functions

### 1. strlen(string)

- This returns the length of string **excluding** the null character.

### 2. strcpy(destination, source)

- This copies source to destination assuming the destination is bigger than source
- the source string should be null terminated
- destination string should be able to hold the source string

### 3. strcat(destination, source)

- concatenates source string to the end of destination string
- both must be null terminated
- the destination should be large enough to hold the appended string

### 4. strcmp(string1, string2)

- returns 0 is both the strings are identical
- both strings should be null terminated

### 5. strchr(string, character)

- returns the first occurence of the character in string

### 6. strncmp (string1, string2, n)

- compares the first n characters of both the strings

### 7. strncpy (destination, source, n)

- copies the first n character of the source to destination

## Converting numeric string to numbers:

```c
#include <stdlib.h>

char num_string[4] = "123";
int mynum = atoi(num_string); // mynum is 123
```
#### to float

```c
#include <stdlib.h>

char num_string[4] = "123";
int mynum = atof(num_string); // mynum os 123.0000
```

## Creating an array of strings 
- this can be done by creating an array of pointers

```c
char *months[12] = {"jan","feb","march","april","june","july","august","september","october","November","december"};
```

# structs

### defining
```c
struct student{
    int marks;              |
    int id;                 |   Structure Members
    char name[12];          |
}
```

### creating 
```c
struct student student1, student2;
```

### working with them
```c

student1.id = 1234;
student1.name = "akshat"; // ❌ as C doesn't allow direct string assignment after declaring
strcpy (student1.name, "akshat");
```


