# Status report

I have implemented the functions:
- malloc
- free
- get_bit
- set_bit
- claim_bit
- alloc_sz_is_free_at_idx
- claim_alloc_sz_at_idx
- free_alloc_sz_at_idx

All functions use stack instructions only where possible. The zero page is only used for the error variable, and functions that I did not write. I only call constants from the absolute memory that already exist. Otherwise, I derive each variable and juggle them on the stack.  

Unit tests for all functions fully pass, except for malloc, where 4/5 tests pass.  

All integration tests pass, except for integration test 8, which doesn't even run.  

I believe atleast one of these issues is due to a stack underflow at some point, where I am incorrect about my world view / stack state when I am preparing the stack for a `JMP2r` instruction. I have double checked the stack state at each instruction, and I have tried observing the stack in a debugger. However, I cannot find my mistake.  