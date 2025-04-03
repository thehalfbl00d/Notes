# Von Neumann Architecture

## Key Concepts
- Architecture matches ENIAC.
- Stores instructions and data in the same memory.
- Enables general-purpose computing by allowing changeable instructions.
- Stored program concept is fundamental and enduring.

## Core Components
- **Main Memory**: Stores data and instructions.
- **Arithmetic Logic Unit (ALU)**: Performs calculations.
- **Control Unit**: Manages instruction execution.
- **Input/Output (I/O)**: Handles external communication.
- **Bus**: Connects components for data flow.

## Fetch-Execute Cycle
- Instructions are fetched and executed sequentially.

## Memory Hierarchy
- **RAM**: Random access, equal access time.
- **ROM**: Read-only, stores firmware.
- **Registers**: Fast, expensive, used in Fetch-Execute Cycle.
- **Cache**: Fast RAM, accessed before main RAM.

## Memory Trade-offs
- Different memory types offer varying cost/performance balances.

## John von Neumann
- "Father of the modern computer."
- Professor at Princeton University.
- Contributed to ENIAC and published "First Draft" on its workings.

## Architecture Details
- Based on the "stored program concept."
- Single storage structure for instructions and data.
- Referential model for sequential architectures.
- Sub-components: memory, control, central processing, input/output.

## Memory Addressing
- Cell size (width) is the number of bits addressed at a time (minimum 1 byte).
- Each cell has a unique address.
- MAR (Memory Address Register) holds the address of a memory location.

## Input/Output (I/O)
- Human-machine interface (keyboard, screen).
- Machine-machine interface (mass storage).

## Arithmetic Logic Unit (ALU)
- Performs arithmetic and logic operations.
- Contains registers, flip-flops, and latches.

## Control Unit
- Drives the fetch and execute cycle.
- Loads cell address into MAR.
- Determines operation to be performed with data in MDR (Memory Data Register).
- Uses special memory registers and a hard-wired instruction set.
    - Program Counter (PC): Address of next instruction.
    - Instruction Register (IR): Holds instruction fetched from memory.
    - Instruction Decoder: Reads instruction from IR and activates the appropriate circuit.

## Instruction Set
- Basic, general instructions specific to the processor.
- Instructions are executed quickly.
- Instructions are encoded with unique binary codes.

## Fetch-Execute Cycle Details
- CPU fetches instructions from memory and executes them.
- **Fetch**: Load instruction from memory into a register and signal the ALU.
- **Execute**: Perform the operation required by the instruction; move/transform data.
- Can be interrupted.

## Memory Operations
- **Fetch**:
    - Cell address loaded into MAR.
    - Data copied from cell to MDR.
    - Non-destructive.
- **Store**:
    - Cell address loaded into MAR.
    - Data from accumulator copied into the cell.
    - Destructive (overwrites existing data).

## Registers in Fetch-Execute Cycle
- DR: Data Register
- M: Memory
- MAR: Memory Address Register - Holds the address of the memory location being accessed.
- MBR/MDR: Memory Buffer Register/Memory Data Register - Holds the data being transferred to or from memory.
- AC: Accumulator - Stores intermediate results during calculations.
- PC: Program Counter - Holds the address of the next instruction to be executed.
- IR: Instruction Register - Holds the current instruction being executed.
- ALU: Arithmetic Logic Unit - Performs arithmetic and logical operations.
- PCU: Program Control Unit - Coordinates all other units in the computer and directs the ALU.

## General Sequence of Fetch-Execute Cycle
1. [PC] -> MAR  - The address in the Program Counter is moved to the Memory Address Register.
2. [M] -> MBR  - The contents of the memory location specified by the MAR are moved to the Memory Buffer Register.
3. [PC]+1 -> PC - The Program Counter is incremented to point to the next instruction.
4. [MBR] -> IR  - The contents of the MBR (the instruction) are moved to the Instruction Register.
5. Decode       - The instruction is decoded to determine the operation to be performed.
6. Execute instruction - The instruction is executed.
7. Repeat         - The cycle repeats.

## Additional Notes
- Modern computers use multitasking (timesharing).
- Each task is a thread.
