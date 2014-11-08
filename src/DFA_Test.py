from DFA import DFA

"""
The following parameters specify a DFA D which recgonizes the following language
L(D) = {s | s contains an even number of zeros}
"""

set_states = {"s1", "s2"}
set_alphabet = {"0", "1"}
transition_dict = {("s1","0"): "s2", ("s1","1"):'s1', ("s2","0"):"s1", ("s2","1"):"s2"}
start_state = "s1"
set_final_states = {"s1"}

D= DFA(set_states, set_alphabet, transition_dict, start_state, set_final_states)

str = "100101010110111110101"
print("{0} is accepted by D: {1}" .format(str, D.process_string(str)))