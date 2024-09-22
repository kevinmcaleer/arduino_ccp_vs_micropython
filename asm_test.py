# Matts Assembler Test
import time

@micropython.asm_thumb
def loop(r0):
    b(loop_entry)     # Branch to loop_entry
    label(loop1)      # Label for loop1
    sub(r0, r0, 1)    # Subtract 1 from r0
    label(loop_entry) # Label for loop_entry
    cmp(r0, 0)        # Compare r0 to 0
    bgt(loop1)        # Branch if greater than

s = time.ticks_ms()
loop(1_000_000)
e = time.ticks_ms()
print(f"\nresult is: {e - s}")

