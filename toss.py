from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
import numpy as np

def getStates(pattern):
	l = len(pattern)
	states = {'phi'}
	for i in range(1, l+1):
		states.add(str(i))
	return states

def getTransitions(pattern):
	l = len(pattern)

	transition = {}

	if pattern[0] == 'H':
		transition['phi'] = {'H': {'phi', '1'}, 'T': {'phi'}}
	elif pattern[0] == 'T':
		transition['phi'] = {'H': {'phi'}, 'T': {'phi', '1'}}

	for i in range(1, l):
		transition[str(i)] = {pattern[i]: {str(i+1)}}

	transition[str(l)] = {}

	return transition

def markovNFA(pattern):
	st = getStates(pattern)

	nfa = NFA(
		states = st,
		input_symbols = {'H', 'T'},
		transitions = getTransitions(pattern),
		initial_state = 'phi',
		final_states = {str(len(pattern))}
	)

	return nfa

def markovDFA(pattern):
	nfa = markovNFA(pattern)
	return DFA.from_nfa(nfa)

def markovChain(pattern):
	dfa = markovDFA(pattern)

	# Setup Markov States
	markovStates = list(dfa.states)
	numStates = len(markovStates)
	initialState = dfa.initial_state
	finalState = dfa.final_states.pop()

	# Get the finalState at the end (ease of indexing)
	markovStates.remove(finalState)
	markovStates.append(finalState)

	# Coin bias
	p = 0.5

	# Markov Transition Matrix
	P = []

	# Initialize with zeroes
	for i in range(0, numStates):
		P_i = [0] * numStates
		P.append(P_i)

	# Fill in the transition matrix using DFA transitions
	for i in range(0, numStates):
		i_state = markovStates[i]

		if i_state == finalState:
			P[i][i] = 1
			continue

		i_trans = dfa.transitions[i_state]

		heads = i_trans['H']
		h_index = markovStates.index(heads)
		P[i][h_index] = p

		tails = i_trans['T']
		t_index = markovStates.index(tails)
		P[i][t_index] = 1-p

	# Remove final state column from the transition matrix
	f = markovStates.index(finalState)
	subP = [row[:f] + row[f+1:] for row in (P[:f]+P[f+1:])]
	for i in range(0, numStates-1):
		subP[i][i] = subP[i][i] - 1

	# Using numpy to solve for X in AX=B
	v = [-1] * (numStates-1)
	x = np.linalg.solve(subP, v)
	i = markovStates.index(initialState)
	return x[i]


pattern = input("pattern=")
for i in pattern:
	if not i == 'H' and not i == 'T':
		print("Invalid Pattern")
		exit()
print(markovChain(pattern))
