1.  convert 0xef00 & (1<<15)

so 0x tells that the leading stuff is hexadecimal
so  0xef00 is       1110 1111 0000 0000
    1<<15 is        1000 0000 0000 0000
    &               1000 0000 0000 0000

2.  convert 0x28a8 | 0xdc45

so  0x28a8is        0010 1000 1010 1000
    0xdc45          1101 1100 0010 0101
    |               1111 1100 1110 1101


## Notes

0x1234

little endians: 
    make a stack, if you represent, the 12 on the top storage of the 34 it will be called little endian in memory.

        if sending data convert it to big endian
    
## ---------
    1<<(2*4) 
    so 0000 0000 0000 0001 the 1 is shifter 8 jumps so it's value is 2^8

## ---------