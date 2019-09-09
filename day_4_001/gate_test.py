from andgate import *

assert (xor_gate(1,0)==1) 
assert (xor_gate(1,1)==0)
assert (xor_gate(0,1)==1)
assert (xor_gate(0,0)==0)

assert (or_gate(1,0)==1)
assert (or_gate(1,1)==1)
assert (or_gate(0,1)==1)
assert (or_gate(0,0)==0)

assert (and_gate(1,0)==0)
assert (and_gate(1,1)==1)
assert (and_gate(0,1)==0)
assert (and_gate(0,0)==0)

assert (not_gate(0)==1)
assert (not_gate(1)==0)