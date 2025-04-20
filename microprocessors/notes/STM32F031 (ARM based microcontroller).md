	Specifications : 
		1. 32kb (programs + constant) memory
		2. 4kb ram (variables)
		3. CPU: ARM Cortex M0, 48MHz

Our arm cortex m0 have 2 stage pipeline (Fetch And Execute)
Instruction 1: 	     Fetch        Execute
Instruction 2: 		                   Fetch         Execute
Instruction 3:                                             Fetch           Execute

### Cache
When you ask for memory address 100 from ram, the cache goes and fetches the nearby the data from memory address too, like 104, 108, 112, 116.


### Memory Protection
when an os loads a process, it gives it memory in blocks

every block have metadata:

1. start address
2. size
3. permissions (rwx)

