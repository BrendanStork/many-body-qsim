import numpy as np
from many_body_qsim.circuits import Quantum_Circuit
from scipy.optimize import minimize

def vqe_energy(
    init_params,
    H,
    ansatz,
    layers=1):
    
    '''
    The number of qubits in this iteration is half the number of initial parameters 
    divided by the number of layers
    '''
    
    num_qubits = int(len(init_params)/2/layers)
    qc = Quantum_Circuit(num_qubits)
    
    ansatz(
        qc,
        init_params,
        layers=layers
    )

    energy = 0


    for pauli, coefficient in H.items():

        expectation = qc.expectation_value(pauli)
        energy += coefficient * expectation

    return energy
    
    
def run_vqe(
    H,
    *,
    ansatz,
    method,
    layers=1):

    num_parameters = 2 * len(next(iter(H))) * layers
    init_params = np.random.uniform(0, 2*np.pi, size=num_parameters)

    result = minimize(
        vqe_energy,
        init_params,
        args=(
            H,
            ansatz,
            layers
        ),
        method=method
        #options={'maxiter':10000}
    )


    return result
