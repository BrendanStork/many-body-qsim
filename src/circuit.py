import numpy as np
from .gates import GATES, apply_cnot


def build_full_operator(gate_matrix, target_qubit, num_qubits):
    if target_qubit >= num_qubits:
        raise ValueError("Invalid qubit index")

    ops = []

    for i in range(num_qubits):
        if i == target_qubit:
            ops.append(gate_matrix)     # already a matrix
        else:
            ops.append(GATES['I'])      # matrix
    #print(ops)
    full_op = ops[0]
    #print(full_op)
    for op in ops[1:]:
        full_op = np.kron(full_op, op)

    return full_op


class Quantum_Circuit:
    def __init__(self, numqubits):

        self.numqubits = numqubits
        self.state = np.zeros(2**numqubits, dtype=complex)
        self.state[0] = 1
        self.gate_count = 0

    def gate_op(self, gate, target):

    #qc = qc0.copy()

        bit = self.numqubits - 1 - target
    
        for i in range(len(self.state)):
    
            # only process "0" side of pair
            if ((i >> bit) & 1) == 0:
    
                j = (i | (1 << bit))
    
                a0 = self.state[i]
                a1 = self.state[j]
    
                self.state[i] = (
                    gate[0,0] * a0 + gate[0,1] * a1
                )
                self.state[j] = (
                    gate[1,0] * a0 + gate[1,1] * a1
                )

        return self.state
    

    def x(self, qubitIndex):
        return self.gate_op(GATES['X'], qubitIndex)
        #return self.gate_op(GATES['X'], qubitIndex)
        
    def y(self, qubitIndex):
        return self.gate_op(GATES['Y'], qubitIndex)
        
    def z(self, qubitIndex):
        return self.gate_op(GATES['Z'], qubitIndex)
        
    def h(self, qubitIndex):
        return self.gate_op(GATES['H'], qubitIndex)

    def s(self, qubitIndex):
        return self.gate_op(GATES['S'], qubitIndex)

    def t(self, qubitIndex):
        return self.gate_op(GATES['T'], qubitIndex)

    def sdag(self, qubitIndex):
        return self.gate_op(GATES['Sdag'], qubitIndex)

    def p(self, qubitIndex, theta):
        return self.gate_op(GATES['P'](theta), qubitIndex)

    def rx(self, qubitIndex, theta):
        return self.gate_op(GATES['RX'](theta), qubitIndex)

    def ry(self, qubitIndex, theta):
        return self.gate_op(GATES['RY'](theta), qubitIndex)
        
    def rz(self, qubitIndex, theta):
        return self.gate_op(GATES['RZ'](theta), qubitIndex)

    def cx(self, control, target):
        self.state = apply_cnot(self.state, control, target)
        return self.state
        
    def expectation_value(self, pauli_string):

        if len(pauli_string) != self.numqubits:
            raise ValueError('Pauli string length must equal number of qubits')

        operator = GATES[pauli_string[0]] # Builds operator
        for p in pauli_string[1:]:
            operator = np.kron(operator, GATES[p])
        return np.vdot(self.state, operator @ self.state).real # Expectation value
    
    def copy(self):

        new_qc = Quantum_Circuit(self.numqubits)
        new_qc.state = self.state.copy()

        return new_qc
