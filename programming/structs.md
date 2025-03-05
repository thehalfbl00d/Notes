To store different types of data in C, we use Structures or Structs.

## Structure Template:

```c
struct student_rec { // structure tag
    int student_ID; // structure members 
    char firstname[11];
    char surname[21];
    int results[5];
};
```

## Where to Define the Structure?

Define the structure outside the `main` function to make it globally accessible. If defined inside `main`, it becomes local to `main`.

## Creating Struct Variables

To create struct variables, use:

```c
struct student_rec student1, student2;
```

## Accessing Structure Members

To access a specific member of the struct:

```c
student1.student_ID = 18;
```

## String Assignment in Structs

You can't assign a string to a char array after declaration using the `=` operator. Use `strcpy` instead.

### Example:

This works:
```c
char name[10] = "akshat";
```

This won't work:
```c
char name[10]; 
name = "akshat"; // Error
```

Use `strcpy`:
```c
strcpy(name, "akshat");
```

## Caution with `gets`

`gets` reads everything from the input and can cause a buffer overflow for the destination. Avoid using `gets`.

## Using `fgets`

`fgets` also has an issue: the enter key is read as a newline character (`\n`). To fix this, read the `fgets` string and replace the newline character at the end:

```c
str[strlen(str) - 1] = '\0';
```
