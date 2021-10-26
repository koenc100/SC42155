# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 13:31:33 2021

@author: koen6
"""


class Mealy(object):
    """Mealy Machine : Finite Automata with Output """

    def __init__(self, states, input_alphabet, output_alphabet, transitions, initial_state):
        """
        6 tuple (Q, ∑, O, δ, X, q0) where −
        states is a finite set of states.
        alphabet is a finite set of symbols called the input alphabet.
        output_alphabet is a finite set of symbols called the output alphabet.
        transitions is the resultant data dictionary of input and output transition functions
        initial_state is the initial state from where any input is processed (q0 ∈ Q).
        """
        self.states = states
        self.input_alphabet = input_alphabet
        self.output_alphabet = output_alphabet
        self.transitions = transitions
        self.initial_state = initial_state

    def get_output_from_string_or_list(self, string, in_list=True):
        """Return Mealy Machine's output when a given string is given as input"""

        if in_list == False:
            temp_list = list(string)
        else:
            temp_list = string
        current_state = self.initial_state
        
        output = ''
        for x in temp_list:

            output_transform = self.transitions[current_state][x][1]

            if isinstance(output_transform, list):
                output_transform = ' '.join(output_transform)
            
            output+= output_transform
            output += ' '
            current_state = self.transitions[current_state][x][0]

        return output, current_state 
    
    def __str__(self):
        output = "\nMealy Machine" + \
                 "\nStates " + str(self.states) + \
                 "\nTransitions " + str(self.transitions) + \
                 "\nInital State " + str(self.initial_state) + \
                 "\nInital Alphabet " + str(self.input_alphabet) + \
                 "\nOutput Alphabet" + str(self.output_alphabet)

        return output

def string_to_list(string):
    return string.split()
   
    
###########################################################################################

# QUESTION 2.2

###########################################################################################

# insert a sequence of on and off switches 
test_list = ['on2', 'on3', 'off3', 'off2', 'on3', 'off1', 'on1', 'on2', 'off3', 'off3']

Q_22 = ['S01', 'S12', 'S23', 'S3>']
input_alphabet_22 = ['on1', 'on2', 'on3', 'off1', 'off2', 'off3']
output_alphabet_22 = ['on1', 'on2', 'on3', 'off1', 'off2', 'off3', 'E']

transitions_22 = {'S01': {'on1': ['S12', 'on1'], 
                'on2': ['S01', 'E'],
                'on3': ['S01', 'E'],
                'off1': ['S01', 'E'],
                'off2': ['S01', 'E'],
                'off3': ['S01', 'E']},
            'S12':
                {'on1': ['S12', 'E'], 
                'on2': ['S23', 'on2'],
                'on3': ['S12', 'E'],
                'off1': ['S01', 'off1'],
                'off2': ['S12', 'E'],
                'off3': ['S12', 'E']},
            'S23':
                {'on1': ['S23', 'E'], 
                'on2': ['S23', 'E'],
                'on3': ['S3>', 'on3'],
                'off1': ['S23', 'E'],
                'off2': ['S12', 'off2'],
                'off3': ['S23', 'E']},
            'S3>':
                {'on1': ['S3>', 'E'], 
                'on2': ['S3>', 'E'],
                'on3': ['S3>', 'E'],
                'off1': ['S3>', 'E'],
                'off2': ['S3>', 'E'],
                'off3': ['S23', 'off3']}
                }
 
initial_state_22 = 'S12'

Mealy_22 = Mealy(Q_22, input_alphabet_22, output_alphabet_22, transitions_22, initial_state_22)

print('The transformed sequence Mealy 2.2: ')
print(Mealy_22.get_output_from_string_or_list(test_list)[0])
print('final state: ', Mealy_22.get_output_from_string_or_list(test_list)[1])

##########################################################################################

# converts output of Mealy 2.2 into input of Mealy 2.3 
input_23 = string_to_list(Mealy_22.get_output_from_string_or_list(test_list)[0])

Q_23 = ['S01', 'S12', 'S23', 'S3>']
input_alphabet_23 = ['on1', 'on2', 'on3', 'off1', 'off2', 'off3', 'E']
output_alphabet_23 = ['w1o', 'w3o', 'w1s', 'w3s', 'E']

transitions_23 = {'S01':
                  
                  {'on1': ['S12', ['w1o', 'w3s']], 
                'E': ['S01', 'E']},
                  
            'S12':
                {'on2': ['S23', ['w1s', 'w3o']], 
                'off1': ['S01', ['w1o', 'w3o']],
                'E': ['S12', 'E']},
                
            'S23':
                {'on3': ['S3>', ['w3s', 'w1s']], 
                'off2': ['S12', ['w1o', 'w3s']],
                'E': ['S23', 'E']},
 
            'S3>':
                {'off3': ['S23', ['w3o', 'w1s']], 
                'E': ['S3>', 'E']}
                }
    
initial_state_23 = 'S12'

Mealy_23 = Mealy(Q_23, input_alphabet_23, output_alphabet_23, transitions_23, initial_state_23)

print('')
print('The last 2 gate positions are the final')
print('The transformed sequence after Mealy 2.3: ')
print(Mealy_23.get_output_from_string_or_list(input_23)[0])
print('final state: ', Mealy_23.get_output_from_string_or_list(input_23)[1])