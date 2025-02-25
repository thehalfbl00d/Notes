# Summary of Strings in C

## String Literals
- A **string literal** is a sequence of characters enclosed in double quotes, stored in a **contiguous** block of memory, ending with a **NULL character** (`\0`).
- Example: `char *str = "Hello";`
- **Escape characters:** `\n` (new line), `\t` (tab), `\\` (backslash), `\"` (double quote), `\0` (NULL character).

## Strings and Arrays
- Strings in C are arrays of characters ending with `\0`.
- Example: `char greeting[6] = "Hello";` (array of 6 including `\0`).
- Array size **must** accommodate the NULL character.

## Displaying Strings
- Using `printf("%s", str);` to print.
- `puts(str);` prints with an automatic newline.
- `gets(str);` (deprecated) reads input including spaces; `fgets(str, size, stdin);` is safer.

## Assigning Strings
- Three ways:
  1. `char greeting[6] = {'H', 'e', 'l', 'l', 'o', '\0'};`
  2. `char greeting[] = "Hello";`
  3. `char *ptr = "Hello";` (stored in read-only memory, modifying leads to **undefined behavior**).

## String Functions (Requires `<string.h>`)
| Function | Description |
|----------|-------------|
| `strlen(str)` | Returns the length of the string (excluding `\0`). |
| `strcpy(dest, src)` | Copies `src` into `dest` (ensure `dest` is large enough). |
| `strcat(dest, src)` | Appends `src` to `dest` (ensure `dest` is large enough). |
| `strcmp(str1, str2)` | Compares two strings (returns `0` if equal, nonzero otherwise). |

## Additional String Functions
| Function | Description |
|----------|-------------|
| `strchr(str, ch)` | Finds first occurrence of `ch` in `str`. |
| `strncmp(str1, str2, n)` | Compares first `n` characters of two strings. |
| `strncpy(dest, src, n)` | Copies first `n` characters of `src` to `dest`. |

These concepts cover the fundamentals of handling strings in C.