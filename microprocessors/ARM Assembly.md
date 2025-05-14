## 🧠 Core Instructions

| Instruction         | Meaning                                  |
|---------------------|------------------------------------------|
| `mov rX, #val`      | Load immediate value into register       |
| `add rD, rN, rM`    | `rD = rN + rM`                            |
| `sub rD, rN, rM`    | `rD = rN - rM`                            |
| `mul rD, rN, rM`    | `rD = rN * rM`                            |
| `cmp rN, #val`      | Compare register with value (sets flags) |
| `b label`           | Branch unconditionally                   |
| `bl label`          | Branch + link (store return address in LR) |
| `bx lr`             | Return from subroutine                   |
| `push {rX, ...}`    | Push registers onto stack                |
| `pop {rX, ...}`     | Pop registers from stack                 |

---

## 📦 Registers

| Register | Purpose                              |
|----------|--------------------------------------|
| `r0–r3`  | Function arguments / return values   |
| `r4–r12` | General-purpose                      |
| `sp`     | Stack Pointer                        |
| `lr`     | Link Register (return address)       |
| `pc`     | Program Counter                      |
| `ir`     | Instruction Register (internal use)  |

---

## 📥 Memory Instructions

| Instruction       | Meaning                             |
| ----------------- | ----------------------------------- |
| `ldr rX, [rY]`    | Load value from memory              |
| `str rX, [rY]`    | Store value to memory               |
| `ldr rX, =0xADDR` | Load constant/address (pseudo-inst) |

---

## 📐 Addressing Modes

| Syntax            | Meaning                    |
|-------------------|----------------------------|
| `[rX]`            | Direct address             |
| `[rX, #offset]`   | Pre-indexed                |
| `[rX], #offset`   | Post-indexed               |
| `[rX, rY]`        | Register offset            |

---

## 🔁 Subroutines

- Call with: `bl function_name`
- Return with: `bx lr`
- Parameters passed in: `r0`, `r1`, ...
- Result returned in: `r0`
- Use `push`/`pop` to save/restore if needed