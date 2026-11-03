from automata.fa.nfa import NFA

# Define NFA
nfa = NFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {
            'a': {'q0', 'q1'},
            'b': {'q0'}
        },
        'q1': {
            'a': set(),
            'b': {'q2'}
        },
        'q2': {
            'a': {'q2'},
            'b': {'q2'}
        }
    },
    initial_state='q0',
    final_states={'q2'}
)

# Test input strings
strings = ['ab', 'aab', 'bab', 'baba', 'aaa', 'bbb', 'aba']

print("NFA Validation Results")

for s in strings:
    if nfa.accepts_input(s):
        print(s, "-> Accepted")
    else:
        print(s, "-> Rejected")