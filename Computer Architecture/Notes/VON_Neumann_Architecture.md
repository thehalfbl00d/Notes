
# Instruction Set

1. The processor's way of speaking.
2. Each instruction is designed to be smaller and simple, the cpu can execute it in nanoseconds.
3. They are like ASCII scheme, every instruction is given a unique binary code.

# Execution Cycle

1. Instructions and data are stored in binary form and stored in ram.
2. If info is needed it is moved to registers from ram
fetch to register -> execute -> fetch to register -> Execute


# Fetch and execute Cycle

### Polling: 

- Continuous check every 1 millionth of a second lol, if the device is there or not.

## Interrupt

- The device sends you a signal when its there so you dont have to check often.
#### Interrupt Handler (ISR)(Interrupt Service Routine)

- This is a piece of code that tells what to do when an interrupt occurs
- After it's done the CPU goes back to it's original state and continues what it was doing.

#### Cycle
### 1. Fetch
- Get instruction from memory using PC.
- Increment PC to point to next instruction.
### 2. Decode
- Decode the fetched instruction in the Control Unit.
- Identify whet operations and which operands are needed.
### 3. Execute
- Perform the operations (USING ALU)
- Store results, maybe in memory or register.


### C O M P O N E N T S
- DR  -> Data Register (Holds temporary data)
- M -> Memory (stores program, data, instructions)
- MAR -> memory address register
- MBR /MDR -> memory buffer/ data register ( holds data coming from or going to memory)
- AC -> accumulator (stores result of things done by ALU)
- PC -> program counter (holds memory address of next instruction to execute)
- IR -> Instruction Register (Holds the current instruction being executed)
- ALU -> Arithematic logic unit (does maths)
- PCU -> program control unit (directs data flow and who does what)

# S  T  E  P  S

[PC] -> MAR (put the address of pc in MAR)
[M] -> [MBR] (put the instruction at MAR at the MBR )
[PC] + 1 -> PC (Increment the pc counter)
[MBR] -> [IR] (put the instruction at the instruction register)

THEN EXECUTE
REPEAT
