
- Serial means data is sent over the wire in bits
#### Hardware Serial Communication

1. UART -> Universal Asynchronous Receiver and Transmitter
2. USART -> Universal Synchronous/ Asynchronous Receiver/Transmitter

#### USART

Here’s what **USART2** typically has (STM32-style):
##### USART Registers :
1. **BRR** – Baud Rate Register
2. **CR1** – Control Register 1
3. **CR2** – Control Register 2
4. **CR3** – Control Register 3
5. **ISR** – Interrupt & Status Register
6. **ICR** – Interrupt Flag Clear Register
7. **RDR** – Receive Data Register
8. **TDR** – Transmit Data Register    
9. **PRESC** – Prescaler Register
10. **RTOR** – Receiver Timeout Register   
11. **RQR** – Request Register    
12. **GTPR** – Guard Time and Prescaler Register

### This is what it looks like:
![[Screenshot 2025-04-20 at 19.36.59.png]]

---

### **Imagine USART as the**  **"big buff data bouncer"**

- **CPU says:** “Yo, send this byte.”
    
- **USART grabs it**, chops it into bits, slaps a start bit, maybe a parity bit, and a stop bit — **puts it in TDR**.
    
- **TDR**: “I got this” → _starts firing bits out the TX pin_.
    
- The bits travel across the line like digital pigeons 🐦.
    



### **On the other end…**

- **USART (other side)** is chilling, watching for a **start bit** like a sniper 👀.
    
- Once it sees the start, it starts **sucking in the bits**.
    
- It **melts them back together** in **RDR** (Receive Data Register).
    
- Then it’s like, “Hey CPU, here’s your byte, fresh off the wire.”



### Ex.

```c
void eputchar(char c)  
{  
while( (USART2->ISR & (1 << 6))==0); // wait for ongoing transmission to finish  
// any non zero value is a truthy value
USART2->TDR = c;  
}  
char egetchar()  
{  
while( (USART2->ISR & (1 << 5))==0); // wait for character to arrive  
return (char)USART2->RDR;  
}
```
#### FLAGS (these are the thing used up in the code for condition checking)
![[Screenshot 2025-04-20 at 20.19.54.png]]

---


