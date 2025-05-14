### GPIO Register Family:

### 1. MODER 
Sets mode of each pin
### 2. IDR
Reads pin values
### 3. ODR
Outputs data register.
### 4. BSRR
Bit Set/Reset Register, useful to turn on off LEDS.

```c
// Turn on LED
GPIOA -> BSRR = (1<<2)

//Turn off LED
GPIOA -> BSRR = (1 << (2 + 16))
```