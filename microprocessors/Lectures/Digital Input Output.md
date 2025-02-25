so there are input outpust modules, mainly 4 for now.

1. gpio ports
2. Timers
3. Communications
3. Analogue I/0

so basically a single pin can be operated by any of the above modules.

each pin can be configured to be an input or an output


# the CPU
a microcontroller have multiple i/o ports, this is the not the breadboard pins but the actual pins on the cpu.

pins(mcu) are divided into gpioa, gpiob .... and there are 16 pins in one gpioa which is a port.
gpioa, b , c, d.... are ports

every port is on one memory location, only one.
one port have 16 pins in STM32L031, one pin can have 2 values, 0 or 1. each port sends one operation at a time.


every port have unique set of registers:
some of them are: 
1. MODER(mode register)
--each pin can be set to input, output, analog or alternate function
--each pin have 2 bits of storage on MODER, this is the above value
--example 00, 01, 10, 11

2. IDR(Input Data Register):
--sets the pin to high or low
--if a pin set to high receives a high signal it will be an input

3. ODR(Ouput Data Register):
--same as idr but for output

So output voltage is 3.3v.
Basically AFR[1] means for pin 1, the property is ....idk


# struct 
-is a datatype
-can be referenced using a pointer
-is like a memory block
-every member is continuous, so if a var address is at 8 the next one will be at 12 (assuming it takes 4 memory bits)

typedef is used to refernce struct without the struct keyword

example :

typedef struct person{
    int age;
    float height;
} person;

## Referencing a struct:

define an instance : 
person p1;

then call that instance:
p1.age = 3;
p2.height = 7.1;


# bitwise OR

so |= is bitwise or, it performs an or operation and assigns the result to the left variable

- -- - 
in BSSR Register which is used to turn leds on and orr the lower Range(0-15) is used to turn the lights on and upper range(16-31) to turn the led off.
- -- -



```

```