so there are input outpust modules, mainly 4 for now.

1. gpio ports
2. Timers
3. Communications
3. Analogue I/0

so basically a single pin can be operated by any of the above modules.

each pin can be configured to be an input or an output


# the CPU
a microcontroller have multiple i/o ports, this is the not the breadboard.

pins(mcu) are divided into gpioa, gpiob .... and there are 15 pins in one gpioa which is a port.
gpioa, b , c, d.... are ports

every port is on one memory location, only one.
one port have 16 pins in STM32L031, one pin can have 2 values, 0 or 1. each port sends one operation at a time.

every port have unique set of registers