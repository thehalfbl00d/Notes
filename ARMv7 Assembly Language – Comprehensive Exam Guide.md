
## **1. Basic Concepts and ARMv7 Architecture**

  

ARMv7 is a 32-bit RISC architecture known for its simplicity and efficiency. Key characteristics include:

- **Registers and Data Path:** Sixteen 32-bit _general-purpose registers_ (named R0–R15) are visible in user mode, plus a _Current Program Status Register (CPSR)_ for flags and mode bits . Among these, R13 is typically used as the Stack Pointer (SP), R14 as the Link Register (LR), and R15 as the Program Counter (PC). The architecture is _load/store_, meaning arithmetic/logic instructions only operate on registers; data must be loaded from memory into registers, processed, then stored back to memory (no direct memory-to-memory ALU operations) .
    
- **Memory and Endianness:** ARMv7 uses 32-bit addresses with _byte-addressable_ memory . Instructions must be word-aligned (4-byte alignment). ARMv7 is bi-endian: the system can be configured for little-endian or big-endian memory layout at boot . (Little-endian is most common, where the least significant byte of a word is at the lowest address.)
    
- **Pipeline:** ARMv7 (ARM state) implements a _3-stage pipeline_ (Fetch, Decode, Execute) to improve throughput . As a result, the PC (R15) often points _ahead_ of the currently executing instruction. In ARM state, when an instruction is executing, PC actually reads as the address of that instruction plus 8 bytes (two instructions ahead) . This is an important detail when using PC-relative addressing or reading the PC in code. (In Thumb state, PC reads as current address + 4.)
    
- **Instruction Set and Format:** ARM instructions are fixed 32 bits long . The instruction encoding includes a 4-bit _condition code field_ (more below), a 4-bit opcode, and operand specifiers. Most instructions use a _3-operand format_ (e.g., ADD Rd, Rn, Rm meaning Rd = Rn + Rm) . A combined ALU and barrel shifter allows many instructions to perform a shift or rotate on an operand _within the same cycle_, enabling efficient bit manipulations .
    
- **Operating Modes:** ARMv7 supports several CPU modes for different contexts. There are _seven_ execution modes: **User** (unprivileged mode for applications), **FIQ** (fast interrupt), **IRQ** (normal interrupt), **Supervisor** (OS kernel / reset), **Abort** (memory access violation), **Undefined** (invalid instruction), and **System** (privileged mode using the same registers as user mode) . Privileged modes (FIQ, IRQ, Supervisor, etc.) have some _banked registers_ — that is, separate R13 (SP), R14 (LR), and in the case of FIQ, R8–R12 — to allow fast context switching on exceptions . The CPSR holds the current mode identifier (in bits M4–M0) and other status flags.
    
- **Status Flags (CPSR):** The CPSR contains condition flags that reflect the results of arithmetic operations and control conditional execution. The main flags are **N** (Negative), **Z** (Zero), **C** (Carry/borrow or extend), and **V** (Overflow) . There are also interrupt disable bits **I** (IRQs disabled when I=1) and **F** (FIQs disabled when F=1) , and the **T** bit (Thumb state bit, T=0 for ARM state, T=1 for Thumb) . The mode bits in CPSR (M4–M0) indicate the current mode (e.g., User, FIQ). User-mode code cannot directly change modes; mode changes happen on exceptions or via special instructions.
    

  

**Figure: Simplified ARM CPSR format and flags** (bits shown in brackets):

```
[N][Z][C][V] ... [I][F][T] ... [M4 M3 M2 M1 M0]
  |  |  |  |         |  |          \___ Mode bits (e.g., 10000 = User)
  |  |  |  |         |  \_____________ Thumb state (0=ARM, 1=Thumb)
  |  |  |  |         \________________ FIQ disable (1 = FIQ off)
  |  |  |  \__________________________ IRQ disable (1 = IRQ off)
  |  |  \_____________________________ Carry/Borrow flag
  |  \________________________________ Zero flag
  \___________________________________ Negative flag
```

Overall, ARMv7’s design (fixed-length instructions, load/store architecture, conditional execution, and simple pipeline) exemplifies RISC principles, enabling most instructions to execute in a single cycle (unless they involve memory access or multi-step operations).

  

## **2. Data Processing Instructions**

  

ARM’s data processing instructions perform arithmetic or logical operations on registers. These instructions do **not** directly access memory (they use register operands) . Common data processing instructions include:

- **Arithmetic:** ADD (addition), ADC (add with carry), SUB (subtract), SBC (subtract with carry), RSB (reverse subtract), etc. For example, ADD R0, R1, R2 computes R0 = R1 + R2. There are also multiply instructions like MUL Rdest, Rm, Rs (Rdest = Rm * Rs) and longer multiply-accumulate variants (e.g., MLA). Division is not a single instruction in ARMv7-A (some cores have a hardware divide instruction, but many use software routine for division).
    
- **Logical/Bitwise:** AND (bitwise AND), ORR (bitwise OR), EOR (XOR), BIC (bit clear – AND with inverted operand), and MOV (move register or immediate). For example, AND R2, R1, #0xFF will mask R1’s lower 8 bits into R2. The MOV instruction copies a value into a register (often used with an immediate). A related instruction MVN (move NOT) sets a register to the bitwise NOT of an operand (useful for loading inverted immediates or ones-complement operations)【25†Ward 32】.
    
- **Comparison and Test:** CMP (compare) and CMN (compare negative) subtract or add values and set flags without storing a result (e.g., CMP R1, #0 sets flags as if R1 - 0 was computed)【25†Ward 30】. TST (bit test) and TEQ (test equal) perform an AND or XOR and set flags to test specific bits or equality. These instructions only update the condition flags (NZCV) in CPSR, not the operands【25†Ward 30】.
    
- **Shifts and Rotates:** Rather than having separate shift instructions that only shift, ARM allows shifting as part of many data instructions. An operand can be shifted left/right or rotated before the ALU uses it. For example, ADD R0, R1, R2, LSL #2 will take R2 left-shifted by 2 bits (multiply by 4) and add to R1. This is encoded in a single instruction and executes in one cycle. There are also stand-alone shift instructions like LSL/LSR (logical shift), ASR (arithmetic right shift), ROR (rotate right), but often the integrated form is used.
    

  

**Immediate Values:** In ARM’s 32-bit instruction encoding, immediate constants are encoded in 12 bits in a compact form (8-bit value plus a 4-bit rotate). This means not every 32-bit constant can be represented directly in one instruction. If you use an immediate that can’t be encoded, the assembler will typically generate a strategy to load it (for example, loading from a literal pool or using multiple instructions). As a programmer, you can use a pseudo-instruction like MOV R0, =0x12345678, and the assembler will produce the appropriate sequence to load that value into R0.

- **Setting Flags:** By default, data processing instructions do **not** update the condition flags in CPSR, except for the compare/test instructions (CMP, CMN, TST, TEQ) which _always_ update flags . Other instructions can be made to set flags by appending an S (for “set condition codes”). For example, ADDS R5, R1, R2 performs R5 = R1 + R2 and updates N, Z, C, V in CPSR according to the result . This is useful if you want the result of an arithmetic operation to influence a subsequent conditional branch or instruction.
    

  

**Example: Basic Arithmetic and Logic**

```
MOV    R0, #5        @ R0 = 5 (move immediate)
ADD    R1, R0, R0    @ R1 = R0 + R0 = 10
SUB    R2, R1, #3    @ R2 = R1 - 3 = 7
CMP    R2, #0        @ Compare R2 with 0, sets flags (R2 is 7, so Z=0, N=0)
MOVEQ  R3, #1        @ If Z==1 (equal), set R3 = 1; here this won't execute
MOVNE  R3, #2        @ If Z==0 (not equal), set R3 = 2; R3 will be 2 after this
AND    R4, R2, #0x3  @ R4 = R2 AND 0x3 (mask lower 2 bits of 7 -> result 3)
ORR    R5, R4, #0x4  @ R5 = R4 OR 0x4 (bitwise OR, sets bit 2: 3 | 4 = 7)
```

In the above example, notice the use of CMP and the conditional MOVEQ/MOVNE instructions – this shows how a comparison can set flags and then subsequent instructions can execute based on those flags. Also note that AND and ORR perform bit masking and combining operations on registers.

  

## **3. Branching and Control Flow**

  

Control flow in ARM assembly is managed with branch instructions and conditional execution:

- **Unconditional Branch (B):** The B instruction causes an unconditional jump to a label (PC-relative). For example, B LOOP sets the PC to the address labeled LOOP. The target is specified as an offset in the instruction encoding (range ~±32 MB in ARM state due to 24-bit offset). Simply put, use B to jump to loops or skip sections of code.
    
- **Branch with Link (BL):** This instruction is used to call subroutines (functions). BL label will branch to the target **and** store the return address in the Link Register (R14 or LR) . Specifically, LR is set to the address of the next instruction (the return point) when executing a BL. After the called subroutine finishes, it can return by branching back to the LR (more on this in the function section). Example: BL FUNCT jumps to function FUNCT and LR = address of the instruction after the BL.
    
- **Branch Exchange (BX):** BX Rm is used to branch to an address contained in register Rm. It also optionally switches instruction set state: if Rm’s least significant bit is 1, it will switch to Thumb mode on branch (if 0, remain in ARM mode). Commonly, BX LR is used to _return from a subroutine_, because it jumps to the address in LR (which was set by a BL) and properly handles switching back to Thumb if needed. For ARMv7, a simple MOV PC, LR in ARM state would also return, but BX LR is preferred for compatibility with Thumb state. BX is also used to call function pointers or jump to an address in a register.
    
- **Conditional Execution:** A powerful feature of ARM (in ARM state) is that **almost every instruction can be made conditional** based on the flags in CPSR . Each instruction has a 4-bit condition code field (the **Cond** field) that is checked to decide if the instruction executes. For example, the suffix EQ means “execute if Z (zero flag) is set”, and NE means “execute if Z is clear”. Some commonly used condition suffixes:
    
    - EQ (equal, Z==1) / NE (not equal, Z==0)
        
    - PL (plus, N==0) / MI (minus, N==1)
        
    - CS or HS (carry set/unsigned higher or same, C==1) / CC or LO (carry clear/unsigned lower, C==0)
        
    - GT (signed greater than, Z==0 and N==V) / LT (signed less than, N!=V)
        
    - GE (signed greater or equal, N==V) / LE (signed less or equal, Z==1 or N!=V)
        
    - AL (always – this is the default if no condition suffix is given) .
        
    
    To use conditional execution, you append the condition code to the instruction mnemonic. For example, BNE LOOP means “branch to LOOP if the Zero flag is not set (Z==0)”, and ADDEQ R0,R1,R2 means “if Z==1 (equal), then R0 = R1 + R2; otherwise do nothing” . Non-taken conditional instructions essentially act as no-ops but still consume one cycle (they are fetched and decoded, but not executed).
    
    Conditional execution allows small if-then operations without actual branch instructions, which can save cycles by avoiding pipeline flushes. However, be mindful not to overuse this feature, as long strings of conditionally executed instructions can become hard to read.
    

  

**Branches and Labels Example:**

```
    MOV   R0, #10       @ Initialize loop counter = 10
loop:
    ; (do something with R0 or other registers here)
    SUBS  R0, R0, #1    @ Decrement counter and set flags
    BNE   loop          @ If Z flag is 0 (R0 not zero), branch back to loop
    ; (execution continues here when R0 becomes zero)
```

In this loop, SUBS subtracts 1 from R0 and updates flags. The BNE loop will keep branching back to loop until the Zero flag is set (which happens when the subtraction resulted in 0, i.e., after 10 iterations). This is a common loop pattern: using SUBS (or ADDS) to affect the Z flag and a conditional branch to loop.

  

Another example, using conditional instructions without an explicit branch:

```
    CMP   R1, R2        @ Compare R1 and R2
    MOVGT R3, R1        @ If (R1 > R2) set R3 = R1
    MOVLE R3, R2        @ If (R1 <= R2) set R3 = R2
```

This code finds the maximum of R1 and R2 and puts it in R3, without any explicit branching. MOVGT executes only if the comparison showed R1 > R2 (greater than), and MOVLE executes only if R1 <= R2. Exactly one of those MOVs will actually write to R3. This logic is equivalent to an if-else in C.

  

## **4. Load/Store Instructions and Addressing Modes**

  

ARM is a _load/store architecture_, so only the **load (LDR)** and **store (STR)** instructions access memory, while all other instructions operate on registers . This means to manipulate data in memory, you first load it into a register, then process it, then store it back.

  

**Basic Load/Store:**

- LDR Rt, [Rn, <offset>] loads a 32-bit word from memory into register Rt.
    
- STR Rt, [Rn, <offset>] stores a 32-bit word from Rt into memory.
    

  

The address is given by a base register (Rn) plus an optional offset. For example, LDR R0, [R1, #4] loads the word at address (R1 + 4) into R0 . Similarly, STR R3, [R0, #-8] would store R3 to the address (R0 - 8). If no offset is given (e.g., LDR R1, [R5]), it means offset 0 (load from address in R5) .

  

**Addressing Modes:** ARM’s addressing modes are flexible:

- _Immediate offset:_ [Rn, #imm] – the address is Rn + imm. The immediate offset can be up to 4095 for word accesses. The offset can also be negative (written as #[-imm] or a minus sign before the number). The base register Rn is not modified in this mode. Example: LDR R4, [R5, #12] loads from address R5+12.
    
- _Register offset:_ [Rn, Rm] – the address is Rn + Rm. You can also scale the register offset with a shift: [Rn, Rm, LSL #s] adds Rm shifted left by s bits (i.e., Rm * 2^s). For instance, LDR R0, [R1, R2, LSL #2] loads from address R1 + (R2<<2) – useful for indexing arrays where R2 is an index and elements are 4 bytes each.
    
- _Pre-indexed with write-back:_ [Rn, #imm]! or [Rn, Rm]! – the address is Rn + offset, and this updated address is also written back into Rn (i.e., Rn is incremented or decremented by the offset). The ! indicates _write-back_. Example: STR R0, [R1, #12]! stores R0 at address (R1+12) _and then_ increases R1 by 12 . After this instruction, R1 = R1 + 12.
    
- _Post-indexed:_ [Rn], #imm or [Rn], Rm – the address used is the original Rn (no offset), but after the access, Rn is modified by the offset. For example, LDR R2, [R3], #4 will load from address R3, and then increment R3 by 4. Essentially, the memory access happens at the old address, then R3 = R3 + 4. Post-indexing is another way to auto-increment or auto-decrement addresses.
    

  

> **Note:** ARM does not have a separate “direct” addressing mode (where an absolute address is encoded in the instruction). Instead, to load from a fixed address, you often use a PC-relative load. For example, LDR R0, =SomeAddress is an assembler pseudo-op that loads the 32-bit address of SomeAddress into R0 using a literal pool. Under the hood this might use the PC (which points ahead) plus an offset to get the constant . In general, the assembler will handle literal pools so you can easily load constants or addresses.

  

- **Size Extensions:** By default, LDR/STR work on 32-bit words. Variants exist for smaller data types:
    
    - LDRB / STRB for 8-bit bytes (load/store byte).
        
    - LDRH / STRH for 16-bit halfwords.
        
    - LDRSB/LDRSH to load a byte/halfword and sign-extend it to 32 bits (useful for signed data).
        
    - (ARMv7 also has LDRD/STRD for 64-bit doublewords on aligned pairs of registers.)
        
    

  

When loading or storing less than 32 bits, the address can be any byte address (not necessarily aligned to the data size, though misalignment might incur a performance penalty or fault on some cores if not supported).

  

**Multiple Registers:** ARMv7 provides block data transfer instructions that can load or store multiple registers in one instruction. These are LDM (Load Multiple) and STM (Store Multiple). They are very powerful for saving/restoring state or moving chunks of data. The syntax is LDM<mode> Rn!, {RegList} and STM<mode> Rn!, {RegList}, where <mode> specifies how the address in Rn is updated as it goes through the list. Common modes:

- IA (Increment After), IB (Increment Before),
    
- DA (Decrement After), DB (Decrement Before).
    

  

To simplify, the assembler provides aliases for typical stack usage:

-  **PUSH**  is an alias for STMDB SP!, {RegList} (Store Multiple Decrement Before). This means decrement SP _before_ storing each register, which is appropriate for pushing onto a full descending stack (the ARM stack typically grows downward). For example, PUSH {R4,R5,LR} will subtract 4 bytes for each register from SP and store R4, R5, and LR at the new addresses. This effectively pushes those registers onto the stack.
    
-  **POP**  is an alias for LDMIA SP!, {RegList} (Load Multiple Increment After). This will load multiple values from the stack into the given registers and then increment SP to release that stack space. For example, POP {R4,R5,PC} will load values into R4, R5, and the PC (which pops the saved program counter or LR into PC, thus returning from a function) and then increment SP appropriately.

  

Using multiple load/store (LDM/STM) is an efficient way to save/restore registers on the stack in function prologues/epilogues. They can also be used to copy memory (though one must be careful with order and overlap).

  

**Example: Using addressing modes**

```
    LDR   R0, [R1]            @ Load word from address in R1 into R0
    LDR   R2, [R1, #4]        @ Load word from R1+4 into R2
    STR   R2, [R1, R3]        @ Store R2 at address (R1 + R3)
    LDR   R4, [R1, R3, LSL #2]@ Load from R1 + (R3<<2) into R4
    LDR   R5, [R1], #4        @ Load from R1 into R5, then increment R1 by 4
    STR   R6, [R7, #-8]!      @ Store R6 at (R7-8), and update R7 = R7 - 8
```

In these examples, you can see immediate vs. register offsets, pre-index (!) vs. post-index, and a scaled register offset. The use of these modes can make array and structure accesses very efficient.

  

## **5. Stack Operations and Function Calling Conventions**

  

The **stack** is a region of memory used for dynamic storage, local variables, and saving registers across function calls. ARM typically uses a _full descending_ stack: it grows downward (to lower addresses) and SP points to the last used address (top of stack). When you “push” data, you decrement SP first and then store; when you “pop”, you load then increment SP.

  

**Stack Pointer (SP/R13):** By convention R13 is used as the stack pointer. The hardware doesn’t enforce its use, but all software and ABI standards assume R13 is SP . At reset, SP is initialized to the end of RAM, and it grows downward.

  

**Push/Pop (Stack Operations):** As mentioned, ARM doesn’t have single-register push/pop instructions, but the assembler maps them to STM/LDM. For example:

```
    PUSH {R4,R5,LR}   @ pushes R4, R5, and LR onto the stack (decrement SP, store)
    ...
    POP  {R4,R5,PC}   @ pops values into R4, R5, and PC (load then increment SP)
```

The POP {…, PC} pattern is often used to return from a function because it restores the PC from the stack (which was the saved LR), effectively jumping back to the caller.

  

Under the hood, PUSH {R4,R5,LR} is equivalent to STMDB SP!, {R4,R5,LR} , and POP {R4,R5,PC} is equivalent to LDMIA SP!, {R4,R5,PC}. The ! in the STM instruction indicates write-back to SP.

  

**Link Register (LR/R14) and PC (R15):** When a function is called via BL, the return address is stored in LR (which is R14) . The callee (called function) can use LR as a temporary register if it saves it, but typically, the first thing a function does is save LR on the stack (so it can use R14 for other things or nest further calls). To return from a function, the contents of LR are placed back into PC . This can be done by MOV PC, LR or more commonly by popping directly into PC (as above) or using BX LR. If a function calls other functions (nested calls), it must push LR to preserve the return address of its caller .

  

**Function Calling Convention (AAPCS - ARM Procedure Call Standard):** ARMv7 follows a well-defined calling convention for interoperability:

- **Parameter passing:** The first four 32-bit function arguments are passed in registers R0, R1, R2, R3. If there are more arguments, they are passed on the stack (memory) at higher addresses above the return address. For floating point or 64-bit arguments, there are additional rules (NEON/SIMD registers, alignment, etc., beyond the basics here).
    
- **Return values:** The result of a function is returned in R0 (and if it’s a 64-bit result, R1 is used for the high 32 bits). So R0 is both an input (arg0) and output register.
    
- **Caller-saved (volatile) registers:** R0–R3 and R12 (and LR to an extent) are considered volatile (caller-saved) . This means a function can freely use these registers, but if the caller needs their values preserved across the call, the caller must save them before the call. In practice, R0-R3 will often contain parameters, so they’re expected to be clobbered. R12 (sometimes called IP or intra-procedure call scratch) can be used as a scratch register, often by the linker or for temporary calculations.
    
- **Callee-saved registers:** R4–R11 are non-volatile (callee-saved) registers . If a function uses any of these, it must save the original value (usually by pushing them on the stack at function entry) and restore them before returning. This ensures the caller sees them unchanged. R9 is sometimes a special register (platform specific, e.g., it might be used as a thread pointer or static base on certain systems), but if not used specially, it’s treated as callee-saved.
    
- **Special registers:** R13 is SP (stack pointer) and must be maintained. A function should leave SP as it was on entry (minus any pushed data, which should be popped before return). R14 is LR (link register) which holds return address; if a function calls another, it must push LR to save its own return address. R15 is PC and is obviously modified only through flow control instructions.
    
- **Frame Pointer:** R11 is often used as a Frame Pointer (FP) in ARM (older APCS calls it FP, in AAPCS it’s just one of the callee-saved). Not all code uses a frame pointer (modern compilers often omit it for leaf functions or when not needed to reduce overhead), but when it is used, a typical function prologue might be:
    

```
PUSH {R11, LR}    @ save old frame pointer and return address
ADD  R11, SP, #0  @ set R11 (FP) = current SP (this marks the start of this frame)
SUB  SP, SP, #N   @ allocate N bytes on stack for local variables
```

- and the epilogue (return sequence) would be the reverse:
    

```
ADD  SP, R11, #0  @ restore SP to the value of frame pointer (undo local allocation)
POP  {R11, PC}    @ restore old frame pointer into R11, and pop return address into PC
```

- This sets up a stable reference (FP) to access local variables and parameters at fixed offsets, which can simplify debugging and certain tasks. But again, FP is optional; many functions just use SP directly for locals.
    

  

**In summary**, a simple function will often:

- Push any callee-saved registers it plans to use (e.g., PUSH {R4,R5,LR}).
    
- Do its work (using R0-R3 for args, producing result in R0).
    
- Before returning, restore saved registers and return (e.g., POP {R4,R5,PC} which restores R4,R5 and loads PC with LR to return).
    

  

The stack must be **aligned** to 8 bytes at calls as per the ABI (this detail means that if you push an odd number of 4-byte registers, you might need an extra push of a dummy register or adjust SP to keep it aligned). This alignment is needed for compliance with data types like double (8 bytes) on the stack.

  

## **6. Writing and Calling Functions in Assembly**

  

Using the stack and calling convention above, we can write and call functions in ARM assembly. Here’s a step-by-step example of a simple function that computes the sum of an array of 32-bit integers:

  

**Example: Sum of an integer array (function sum_array)**

  

Assume a function prototype like int sum_array(int *arr, int length) – it takes a pointer to an array (arr) and the number of elements (length), and returns the sum in R0.

```
        @ Function: int sum_array(int *arr, int length)
        @ On entry: 
        @    R0 = arr (pointer to int array)
        @    R1 = length (number of elements)
        @ Uses R2,R3 as temporaries (caller-saved, so OK)
        @ Returns:
        @    R0 = sum of array elements
sum_array:
        PUSH   {R4, LR}         @ Save callee-saved R4 and link register (return addr)
        MOV    R2, #0           @ R2 will accumulate the sum, start at 0
        MOV    R3, #0           @ R3 will be our index (i = 0)
loop:
        CMP    R3, R1           @ Compare index with length
        BEQ    done             @ if index == length, break out of loop
        LDR    R4, [R0, R3, LSL #2] @ R4 = arr[i]  (LSL #2 multiplies index by 4)
        ADD    R2, R2, R4       @ sum += arr[i]
        ADD    R3, R3, #1       @ i++ (increment index)
        B      loop             @ repeat until i == length
done:
        MOV    R0, R2           @ move sum result into R0 (function return)
        POP    {R4, LR}         @ restore R4 and LR
        BX     LR               @ return to caller (jump to address in LR)
```

**Breakdown:** On entry, arr is in R0 and length in R1. We push {R4, LR} because we’ll use R4 in our loop (and LR needs to be saved to return correctly since we’ll use BX LR at the end). We use R2 to accumulate the sum, initialized to 0, and R3 as an index.

  

In the loop:

- We compare R3 (index) with R1 (length). If they are equal, we’ve processed all elements, so branch to done.
    
- We load the array element: the address of arr[i] is arr + i*4. R0 has base address, R3 is i, so [R0, R3, LSL #2] computes the address. The loaded value goes into R4.
    
- Add the value to R2 (our running sum).
    
- Increment the index R3 and loop back.
    

  

When done, the sum is in R2, so we copy it to R0 for the return value. Then we pop R4 and LR. Popping LR restores the return address into LR, and then BX LR jumps back to that address (returning to the caller). We could combine the last two lines by doing POP {R4, PC} instead, which would pop R4 and directly load PC (effectively returning), but here we show BX for clarity.

  

This function adheres to the calling convention: it preserved R4 (callee-saved) by pushing and popping it, and it didn’t disturb any other callee-saved registers. It used R0,R1 as inputs and returns R0 as output. The caller would be responsible for R0-R3 volatility (in this case, R0,R1 were inputs anyway).

  

To call this function from another assembly routine (or from C), you would:

- Place the array address in R0, length in R1.
    
- Do BL sum_array.
    
- After the BL, R0 will contain the result (sum).
    

  

For example, if calling from assembly:

```
    LDR   R0, =my_array   @ R0 = address of array
    MOV   R1, #100        @ R1 = length (say 100 elements)
    BL    sum_array       @ call the function
    @ Upon return, R0 has the sum. Use it as needed.
```

Where my_array is a label for an array defined elsewhere (or passed in from C, etc.).

  

**Recursive Function Example:** To illustrate function calls and the use of LR further, here is a simple recursive factorial function in ARM assembly (for a non-negative integer n in R0, it returns n! in R0):

```
factorial:
    CMP   R0, #1          @ if n <= 1:
    BLE   base_case       @ return 1 (base case)
    PUSH  {R0, LR}        @ save n (in R0) and return address (LR) on stack
    SUB   R0, R0, #1      @ n = n - 1
    BL    factorial       @ recursive call: factorial(n-1)
    POP   {R1, LR}        @ restore original n into R1, and return addr into LR
    MUL   R0, R0, R1      @ multiply result by n (R0 = (n-1)! * n)
    BX    LR              @ return (result is in R0)
base_case:
    MOV   R0, #1          @ return 1
    BX    LR
```

Let’s walk through this: If n <= 1, we hit base_case and just return 1. Otherwise, we push R0 and LR. Why push R0? Because R0 holds n, and we need that after the recursive call returns (to multiply with (n-1)! result). Pushing it saves n on the stack. We also push LR to save our return address. Then we decrement n by 1 and do BL factorial (recursive call). When that returns, R0 has (n-1)! (the result of factorial(n-1)). We then pop into R1 and LR. R1 now has the original n, and LR has the return address. We multiply R0 (which has (n-1)!) by R1 (which has n) to get n!, and then branch to LR to return to the caller. This shows how LR is used for return addresses and how recursion requires saving LR on the stack so that each call can return to the correct place. It also shows a use of multiple return values: here we needed both the returned factorial and the original n; we got the factorial in R0 and retrieved n from stack into R1.

  

## **7. Interrupt Handling and Exception Modes**

  

ARMv7 supports a variety of **exceptions** (interrupts, software interrupts, fault handlers) that switch the CPU into privileged modes. As mentioned in section 1, there are several modes: User and System (non-interrupt modes), and FIQ, IRQ, Supervisor, Abort, Undefined (exception modes) . Each exception mode has its own banked SP and LR (and FIQ has more banked registers) , as well as a Saved Program Status Register (SPSR) to hold the prior CPSR value .

  

**Exception Entry (e.g., Interrupts):** When an exception occurs (like an IRQ interrupt), the ARM hardware will do the following steps _atomically_:

- Switch to the corresponding mode (e.g., IRQ mode for an IRQ interrupt).
    
- Save the current PC into the LR of that mode, usually with an adjustment. For example, on an IRQ, LR_irq = address of the next instruction after the one that was interrupted + 4. (On ARM, when the pipeline is flushed for an exception, the PC that gets saved might be one or two instructions ahead due to pipelining.)
    
- Save the current CPSR into the SPSR of the new mode.
    
- Disable further interrupts of the same or lower priority (for IRQ, the I bit in CPSR is set to 1 automatically; for FIQ, both I and F bits may be set) .
    
- Load the PC with the vector address for the exception.
    

  

On ARMv7 (in the classic ARM vector table configuration), the exception vectors are fixed addresses in low memory. For example:

- 0x00000000 – Reset vector (jump on reset, enters Supervisor mode)
    
- 0x00000004 – Undefined instruction vector (enters Undefined mode)
    
- 0x00000008 – Software Interrupt (SWI/SVC) vector (enters Supervisor mode)
    
- 0x0000000C – Prefetch Abort (instruction fetch memory fault) vector (enters Abort mode)
    
- 0x00000010 – Data Abort (data memory fault) vector (enters Abort mode)
    
- 0x00000014 – (Reserved or for Hypervisor in newer ARM)
    
- 0x00000018 – IRQ interrupt vector (enters IRQ mode)
    
- 0x0000001C – FIQ interrupt vector (enters FIQ mode)
    

  

Each vector contains a branch to the actual handler routine (often just a jump instruction at those addresses to the real code, to keep the table small).

  

**Handling an Interrupt:** The interrupt handler is just an assembly routine (often) that runs in the exception mode. It has to be careful to save any registers it uses (it might have some banked registers to use freely). For example, in IRQ mode, R0-R12 are the _same as_ user-mode’s (not banked), so the handler should push any of those it needs to use. R13_irq is a dedicated stack pointer for IRQ mode (the OS typically sets up a separate stack for interrupts), and R14_irq (LR) contains the return address. The handler would do what it needs (e.g., read/write device registers, acknowledge the interrupt), then restore state and exit.

  

**Returning from Exception:** To return from an interrupt or exception, simply restoring PC = LR is not enough, because you also need to restore the CPSR (the status flags and mode, etc.) to what they were. ARM provides special instructions for this, like:

- SUBS PC, LR, #4 (commonly used for IRQ return in ARM state): This does PC = LR - 4, but the S means it will also restore CPSR from SPSR. The offset #4 accounts for the fact that for IRQ, LR was set to PC+4. (This detail can vary: for different exceptions the adjustment might be different, but the idea is LR holds the return address offset by a constant).
    
- Alternatively, MOVS PC, LR can be used in some cases (for exceptions where LR = PC+something already appropriate), which will copy SPSR to CPSR as well when executed in an exception mode.
    

  

In ARMv7-A, typically an instruction like MOVS PC, LR (with proper value in LR) or the equivalent LDMFD sp!, {..., PC}^ (the ^ indicates to restore CPSR from SPSR) is used to return from the exception and restore the previous program state. These instructions will switch the mode back to the previous mode (user or whatever) and re-enable interrupts (since CPSR is restored).

  

**FIQ vs IRQ:** FIQ (Fast Interrupt) is a higher-priority interrupt than IRQ. The key difference in ARM is that FIQ mode has five extra banked registers (R8_fiq–R12_fiq) in addition to its own R13_fiq and R14_fiq. This is designed so that a FIQ handler can do more work without needing to save/rest of general registers (it has a set of its own registers to use), making it faster to respond. Typically, systems use FIQ for a very time-critical single source (like a high-speed data acquisition), and IRQ for all the normal interrupts. The ARM hardware will disable normal IRQs when an FIQ is taken (so an FIQ can’t be interrupted by an IRQ), but not vice versa (an IRQ won’t disable FIQs, so an FIQ could preempt an IRQ if it comes in).

  

**Software Interrupt (SWI/SVC):** This is a mechanism for user-mode code to call an OS service (system call). The SWI #imm (also called SVC #imm in ARMv7) instruction triggers a Supervisor Call exception, causing the CPU to switch to Supervisor mode, LR_svc = return address, and jump to the SVC handler at 0x08. The immediate operand is often used as a syscall number to indicate which service is requested . The OS then performs the service and returns to user mode via the usual exception return mechanism.

  

**Abort and Undefined:** The Prefetch Abort and Data Abort are used for memory faults (like page faults or bus errors). The Undefined exception occurs when an undefined instruction is executed (often used to implement software emulation of unimplemented instructions or as a way to extend the instruction set).

  

From a programmer’s perspective (especially in an OS or bare-metal context), writing an interrupt handler means writing an assembly (or compiler inlined) routine that:

1. Lives at the vector or is branched to by the vector.
    
2. Saves context (if needed), handles the device/condition, clears the interrupt source, possibly signals to other code that the event happened.
    
3. Restores context and executes the appropriate return (moving SPSR to CPSR and jumping back).
    

  

In high-level terms, interrupts behave like automatic function calls initiated by hardware, with LR holding the return point and a special return mechanism to also restore processor state. ARM’s banked registers and fast context switching features help minimize the overhead of entering and exiting these handlers.

  

## **8. Inline Assembly in C (with examples)**

  

Sometimes you may want to write a few assembly instructions _inside_ a C function for performance or hardware access. ARM, using GCC or Clang, supports **inline assembly** using the asm (or __asm__) keyword. The syntax can be a bit tricky, as you need to inform the compiler about any inputs, outputs, and clobbered registers. Here’s a brief overview:

  

The general form (GNU Extended ASM) is:

```
asm volatile (
    " <assembly template> "
    : /* output operands */
    : /* input operands */
    : /* list of clobbered registers */
);
```

The assembly template is a literal string. You can include C expressions (variables) in the assembly by using placeholders like %0, %1, etc., in the template, and then providing corresponding C expressions in the input/output sections. Each operand is described by a constraint (like "r" meaning any register) and a C variable.

  

**Example 1:** A simple inline assembly to add two numbers:

```
#include <stdio.h>

int main() {
    int a = 5, b = 7, result;
    __asm__ volatile (
        "ADD %0, %1, %2"      /* assembly: result = a + b */
        : "=r" (result)       /* output %0 in any register */
        : "r" (a), "r" (b)    /* inputs %1 = a, %2 = b (in registers) */
        : /* no clobbers */
    );
    printf("Sum = %d\n", result);
    return 0;
}
```

Here, the template "ADD %0, %1, %2" will be filled in by the compiler with appropriate register names for %0, %1, %2. We tell the compiler that %0 (the destination of ADD) will be an output ("=r"(result) means assign to C variable result, using a register for it). The inputs are "r"(a) and "r"(b), meaning load a and b into registers for the assembly. The compiler will choose registers and substitute them in place of %0, %1, %2. After this asm executes, result will contain the sum (just as if we did result = a + b; in C). This inline asm communicates with C variables, so the compiler “knows” it sets result and that it used a and b.

  

**Example 2:** Inline assembly to toggle an LED on a microcontroller (hypothetical):

```
#define GPIO_PORT  ((volatile unsigned int*)0x40000000)  // base address of a GPIO port
#define LED_BIT    (1 << 3)  // LED is on bit 3 for example

void toggle_led() {
    __asm__ volatile(
        "LDR r0, %[addr]    \n\t"  /* r0 = address of GPIO port */
        "LDR r1, [r0]       \n\t"  /* r1 = *GPIO_PORT (read current value) */
        "EOR r1, r1, %[mask]\n\t"  /* r1 = r1 XOR LED_BIT (flip that bit) */
        "STR r1, [r0]       \n\t"  /* *GPIO_PORT = r1 (write back toggled value) */
        :
        : [addr] "m" (*GPIO_PORT), [mask] "r" (LED_BIT)
        : "r0", "r1", "cc"  /* clobbered regs and flags */
    );
}
```

In this example, we use named placeholders %[addr] and %[mask] for clarity. We pass in the address ("m"(*GPIO_PORT) tells the compiler to treat the memory at GPIO_PORT as an input and it will provide its address) and the mask (LED_BIT) into a register. We explicitly clobber r0, r1, and condition codes ("cc"), to tell the compiler those are used/changed by our code. The assembly loads the GPIO port value, XORs the LED bit to flip it, and writes it back, thus toggling the LED. We mark the address as memory "m" because we want the compiler to know we are accessing that memory location (so it doesn’t reorder other memory accesses around this code incorrectly).

  

**Important notes for inline assembly:**

- Always list the registers you use in the clobber list _if_ they are not listed as outputs. Failing to do so can lead to the compiler assuming those registers still contain some prior values when they don’t.
    
- If your assembly changes memory (writes to some memory address that the compiler doesn’t know about), use "memory" in the clobber list. This tells the compiler that “memory has been changed” and it should not cache memory values across this asm.
    
- Use volatile for asm statements that should not be optimized out or moved. Without volatile, the compiler might decide to omit the asm if it thinks the outputs are not used, etc.
    
- You cannot blindly use any register name in extended asm (like r0); the compiler will allocate registers for you for operands. If you really need a specific register or to use a special instruction that requires a particular register (like dealing with sp or special regs), there are ways (contraints or using basic asm with .asm directives), but that’s advanced usage.
    
- For simple tasks, extended inline asm is powerful, but for bigger sections of assembly, it may be easier to write a separate .s file or use intrinsics provided by the compiler.
    

  

**Basic asm vs Extended asm:** The above is _extended_ asm. GCC also allows _basic_ inline asm of the form asm("instruction"); which doesn’t have the operands/clobbers sections. However, basic asm is much less safe because the compiler has no idea what your assembly is doing. In ARM context, basic asm is rarely used except perhaps for inserting a single instruction like a no-op (asm("NOP");). It’s better to use extended asm so the compiler can properly coordinate with your assembly code.

  

In summary, inline assembly lets you hand-tune parts of your code while still in the C environment. The examples above show adding two numbers and toggling hardware bits directly. You should use it only when needed, as it can make code less portable and harder to maintain. But for an exam, understanding the mechanism is useful.

  

## **9. ARM in Embedded Systems: Memory-Mapped I/O and Peripherals**

  

One common use of assembly (or low-level C) in embedded systems is interacting with hardware registers. ARM (like many modern architectures) uses **memory-mapped I/O**, meaning that device registers (for GPIO, UART, timers, etc.) are mapped to specific memory addresses. Reading from or writing to those addresses using normal load/store instructions will actually interact with the hardware .

  

For example, suppose a device’s LED control register is at address 0x40010000. To turn the LED on, you might need to write a specific value to that address. In C you would do something like:

```
*((volatile unsigned int*)0x40010000) = 1;  // set LED on
```

The volatile tells the compiler not to optimize the access away. In assembly, you can achieve the same with:

```
    LDR   R0, =0x40010000    @ R0 = address 0x40010000
    MOV   R1, #1             @ R1 = 1 (value to turn LED on)
    STR   R1, [R0]           @ *(R0) = R1  (write 1 to the LED register)
```

This uses an immediate addressing (the pseudo-instruction LDR R0, =addr will put the 32-bit address in R0, possibly via a literal pool). Then we store the value 1 to that address. If the LED hardware is mapped there, it will turn on.

  

Memory-mapped I/O means there is no separate I/O instruction; you just use LDR/STR on those special addresses. The peripherals recognize accesses to their addresses and respond accordingly . For instance, reading from an ADC register address might give you the current sensor reading, writing to a UART data register sends a byte out the serial port, etc.

  

Because compilers know how to handle memory, you leverage normal load/store. The only thing is to prevent the compiler from optimizing or reordering these, you typically mark the pointers as volatile. In assembly, you as the programmer are in direct control, so each load/store will happen exactly where you put it.

  

**Memory barriers:** In more complex systems (with caches, reordering, etc.), sometimes you need memory barrier instructions (e.g., ARM’s DMB, DSB, ISB) to ensure ordering of memory-mapped I/O operations relative to other operations. This might be an advanced topic, but just be aware that when writing device drivers, you occasionally use special instructions to prevent the CPU from moving loads/stores across these barriers.

  

**Example: Toggling a GPIO pin (abstract)** – combining what we learned:

Suppose a GPIO output register is at address 0x50000000 and bit 0 controls an LED. The following pseudocode in assembly toggles it:

```
    LDR   R0, =0x50000000   @ address of GPIO output register
    LDR   R1, [R0]          @ load current value
    EOR   R1, R1, #1        @ toggle bit0 (XOR with 1)
    STR   R1, [R0]          @ store back new value
```

This is essentially what we showed in the inline assembly example but in pure assembly. Toggling means if it was 1 it becomes 0, if 0 becomes 1.

  

**Interfacing with peripherals:** Often, each peripheral has multiple registers (control, status, data registers, etc.), and you’ll have a reference manual providing those addresses and bit meanings. In assembly, you might define these addresses at the top as constants or use labels. For example:

```
UART_DR   EQU 0x4000_3000   @ Data register
UART_STAT EQU 0x4000_3004   @ Status register (bit 5 TX empty, etc.)

    LDR R0, =UART_STAT
wait:
    LDR R1, [R0]
    TST R1, #0x20           @ test TX empty flag (bit5 for example)
    BEQ wait                @ if not empty, wait
    ; now it's empty, send next char
    LDR R0, =UART_DR
    MOV R1, #0x41           @ 'A'
    STR R1, [R0]            @ write 'A' to UART data register
```

This kind of code waits for a UART transmit buffer to be empty, then writes a character. It’s a simple polling loop, common in bare-metal embedded programming.

  

In summary, _memory-mapped I/O_ allows assembly code to interact with hardware by reading and writing memory addresses. No special opcodes are required beyond normal loads and stores . This makes the CPU design simpler and the programming model uniform (memory is memory, whether it’s RAM or a device register). The key is knowing the correct addresses and required operations from the hardware’s documentation.

  

## **10. Common Patterns and Pitfalls for Beginners**

  

Writing ARM assembly gets easier with practice. Here are some common patterns to recognize, and pitfalls to avoid:

- **Looping Patterns:** A typical countdown loop uses the SUBS instruction on a counter and a conditional branch. For example:
    

```
MOV   R0, #N       @ R0 = loop count N
```

  

  

loop:

; loop body

SUBS  R0, R0, #1   @ decrement counter and set flags

BNE   loop         @ if not zero, loop again

````
This pattern uses the Zero flag to determine when to exit (after N iterations). Ensure you use the `S` suffix on the subtract (or add) so that the flags are updated for the branch.

- **Using Conditional Instructions:** Beginners sometimes forget that conditional execution applies to more than just branches. If you do use it, ensure the preceding instruction indeed set the condition codes appropriately. Also, remember that a sequence of conditional instructions all depend on the original flags until something changes them. If one of them executes and changes a register needed by another path, logic can get complex. Keep it simple: usually only 1-3 instructions in a row with the same condition.

- **Saving and Restoring Registers:** One of the most frequent mistakes is failing to preserve the link register or other registers across function calls. If your function calls another (`BL`), then before that call you *must* preserve your own LR (since BL will overwrite LR). That usually means `PUSH {LR}` at the start of the function (or as part of pushing other regs). Similarly, if you use any callee-saved registers (R4-R11), push them on entry and pop on exit. On the flip side, if you’re the caller and you need a value in R0-R3 or R12 after a function call, you need to save it before the call (since the callee might destroy it). These convention details are critical for correct program execution. A bug in saving/restoring registers can cause wild jumps (e.g., returning to the wrong address) or corrupted data.

- **Alignment and Access Issues:** When using `LDR`/`STR`, remember that ARMv7 requires the address to be aligned for the data size (unless using certain CPUs with unaligned support). For instance, loading a word from an address not divisible by 4 can cause an abort on some ARM systems. Ensure your data is properly aligned. This is usually handled by the compiler or assembler (it aligns word-sized variables to 4 bytes), but if you manually construct addresses, keep alignment in mind.

- **Immediate value limitations:** As mentioned, not every arbitrary 32-bit value can be moved into a register with a single `MOV`. If you do something like `MOV R0, #0x12345678`, the assembler might throw an error if it can’t encode it. Instead, either use the literal pool (`LDR R0, =0x12345678`) or break it into two instructions (e.g., on ARMv7 you could use `MOVW`/`MOVT` pair, if available, to set lower 16 bits and high 16 bits). The assembler’s `<constant>` syntax (`=value`) is easiest – it automatically generates a literal in a nearby pool and a PC-relative LDR to get it.

- **Not Understanding PC-relative addressing:** On ARM, `LDR Rd, =label` is a pseudo-instruction that many use to get addresses or constants. Under the hood, this often translates to something like `LDR Rd, [PC, #offset]`. Due to the pipeline, when that LDR executes, PC is not exactly the address of that LDR, but 8 bytes ahead (in ARM state). The assembler abstracts this, but if you ever manually compute addresses relative to PC, recall the PC is ahead by 8. This is a gotcha if you try to do tricks like `ADR R0, label` (ADR gives an address of a label, using PC relative add) – you must trust the assembler or carefully account for it. If you treat PC in data operations, know about the pipeline offset [oai_citation:52‡web.eecs.utk.edu](https://web.eecs.utk.edu/~mbeck/classes/cs160/lectures/11_ARM_overview.pdf#:~:text=%E2%80%A2%20When%20the%20processor%20is,on%20stack%20in%20linked%20branch) [oai_citation:53‡web.eecs.utk.edu](https://web.eecs.utk.edu/~mbeck/classes/cs160/lectures/11_ARM_overview.pdf#:~:text=%E2%80%A2%20The%20PC%20points%20to,back%20to%20Register%20Bank%20PC).

- **Using the Wrong Return Instruction:** In ARMv7, always prefer `BX LR` or `POP {PC}` to return from subroutines. A common mistake is to do `MOV PC, LR`. This works in ARM state *if you’re staying in ARM state*, but if your code might be called from Thumb state (for example, many OS or libraries might call your assembly function from Thumb code), then `MOV PC, LR` will not switch back to Thumb – it will attempt to execute LR address in ARM mode, likely causing a fault. `BX LR` uses the lower bit of LR to switch mode appropriately (ARM/Thumb). So it’s a safer return mechanism. (If you know everything is ARM, it’s fine, but it’s good practice to use BX.)

- **Stack pointer management:** Always clean up the stack properly. Every push should have a matching pop before return (assuming the function is supposed to restore the stack to the state it was on entry). If you allocate space on the stack by subtracting from SP, make sure to add it back. If you forget, you’ll accumulate stack usage and likely crash or overwrite data eventually. Also, remember the stack grows down: doing `SUB SP, SP, #16` allocates 16 bytes. A common error is to accidentally do the opposite (e.g., add to SP when you meant to subtract).

- **Banked registers misunderstanding:** If you’re writing simple user-mode programs, you won’t deal with banked registers much. But if you happen to write interrupt handlers, remember that in IRQ mode, for example, you have a different R13 and R14 (and that’s intentional, to keep a separate stack for IRQ). If you push/pop in the wrong mode’s stack or use the wrong LR, chaos ensues. Typically, an OS sets up those stacks and you, as a programmer, just use `PUSH`/`POP` normally; just be mindful that an interrupt handler running in IRQ mode should not try to return with `BX LR` without restoring SPSR -> CPSR (use `subs pc, lr, #4` for IRQ or similar), as described earlier.

- **Floating-point and SIMD registers:** Not covered in depth here, but note that if you use FPU (VFP) registers (s0-s31/d0-d15), or NEON (q0-q15) in assembly, there are additional calling convention rules (those registers are typically caller-saved except a few that might need special handling). Also, one must ensure to enable and save them in an OS context switch. For basic integer assembly, you won’t touch these.

- **Symmetric code block pitfalls:** Because ARM’s conditional execution can eliminate branches, you might be tempted to do things like:
```asm
CMP R0, #0
ADDEQ R1, R2, R3
ADDNE R1, R2, R4
````

expecting R1 to be set either to R2+R3 or R2+R4. This works because exactly one of those ADDs will execute. But be cautious if the conditions are not opposites (complementary) or if there are more than two paths – you can easily create a situation where no instruction executes (if conditions fail) or multiple do (if logic is wrong). For more complex conditional logic, it might be clearer to use actual branches.

- **Assembler directives and syntax issues:** Beginners might forget to declare global labels or use the correct syntax. For example, if writing in a file, you need .global func_name if you want it accessible from C. Also, note ARM assembly syntax: by default, ARM assemblers use the _unified syntax_, which is similar to ARM’s traditional syntax. Be mindful of the distinction between B (branch) and B.X in older syntax for Thumb, etc. Using a modern assembler with unified syntax simplifies this (it infers based on .thumb or .arm state). Typically in ARMv7, you might see .syntax unified at the top of assembly files and directives like .thumb_func or .arm. If writing inline assembly, these are handled by the compiler. But if writing standalone assembly, ensure you specify the correct mode and global labels as needed.
    

  

In short, follow the calling convention, manage the stack carefully, and test small pieces of code thoroughly. Use the condition flags and conditional instructions to your advantage, but keep track of them. These practices will help avoid the common pitfalls.

  

## **11. Sample Programs and Step-by-Step Breakdowns**

  

Let’s solidify understanding with a couple of sample programs, explained line by line. We already did a detailed breakdown for sum_array in section 6. Here we will present another example and an exercise:

  

**Example: Computing the maximum of an array (assembly program)**

  

This program will find the largest number in an array of signed integers. We assume the array address is in R0 and length in R1 (similar to earlier, just for demonstration). The result (max value) will be in R0.

```
        @ int max_array(int *arr, int length)
        @ Entry: R0 = arr, R1 = length
        @ Exit:  R0 = max value
max_array:
        PUSH   {R4, LR}        @ Save R4 (will use for current max) and LR
        CMP    R1, #0          @ if length == 0:
        BEQ    done_zero       @    return (we'll return 0 for empty array, or could handle differently)
        LDR    R4, [R0], #4    @ Load first element into R4, post-increment R0 to point to second element
        SUB    R1, R1, #1      @ Decrease length count (we've consumed one element)
loop_max:
        CMP    R1, #0          @ have we checked all elements?
        BEQ    end_loop        @ if count == 0, done looping
        LDR    R3, [R0], #4    @ R3 = *arr++, and increment pointer (post-indexing)
        SUB    R1, R1, #1      @ count--
        CMP    R3, R4          @ compare new element with current max (R4)
        BLE    loop_max        @ if R3 <= R4, current max is bigger, continue loop
        MOV    R4, R3          @ else, update current max to R3
        B      loop_max
end_loop:
        MOV    R0, R4          @ place max value in R0 for return
done_zero:
        POP    {R4, LR}        @ restore R4 and return address
        BX     LR              @ return to caller
```

**Explanation:** We save R4 and LR. R4 will hold the current maximum. If length is 0, we immediately branch to done_zero (which just pops and returns; here we leave whatever was in R4 as return, not explicitly handled – in a real implementation, we might define behavior for empty input).

  

If not empty, we load the first element into R4, and also increment the array pointer (R0) to the next element (LDR R4, [R0], #4 does that in one go). We decrement R1 (length) since we processed one element.

  

Then in the loop, as long as R1 (elements remaining) is not zero, we load the next element into R3 (again using post-increment to advance the pointer each time) and decrement R1. We compare the new element (R3) with the current max (R4). If the new element is less or equal (BLE) to R4, we just loop back without changing R4. If the new element is greater, the BLE is not taken, and the next instruction MOV R4, R3 executes, updating the current max. We then loop back. After the loop, R4 holds the max, so we move it to R0 as the return value. We then pop R4 and LR and return. This demonstrates use of post-index addressing to simplify pointer arithmetic and a typical compare-and-update routine for max.

  

**Key takeaways from this example:**

- Post-increment in LDR simplifies pointer incrementing in loops.
    
- We carefully manage the loop counter (R1) and pointer (R0) so that we don’t run past the array.
    
- We preserved callee-saved R4 and LR properly.
    
- Conditionals were used to skip the update of max when not needed, making the loop efficient.
    

  

**Exercises for practice:** To solidify your understanding, you can try writing the following in ARMv7 assembly (paper or assembler):

1. **Array reversal:** Write a routine that reverses an array of 32-bit integers in place. (Hint: use two pointers, one at start and one at end, swap elements moving inward.)
    
2. **Count occurrences:** Given a value and an array, count how many times the value appears in the array. (Loop through, use a conditional increment.)
    
3. **Fibonacci (iterative):** Compute the n-th Fibonacci number iteratively using a loop (0,1,1,2,3,5… sequence). Use registers to hold the two previous values and update in a loop.
    
4. **Bit count:** Count the number of 1 bits in a 32-bit register (population count). Try doing this by shifting the register and using a counter.
    

  

Each of these exercises will involve using the instructions and patterns discussed: loops, conditionals, loads/stores, arithmetic, etc. Make sure to document each step and follow calling conventions if you implement them as separate functions.

  

By practicing and analyzing these patterns, you’ll become fluent in ARM assembly. Good luck on your exam – with a solid understanding of registers, instructions, and conventions, you’ll be well-prepared to tackle ARMv7 assembly programming problems!