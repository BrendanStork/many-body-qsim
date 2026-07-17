import numpy as np

from many_body_qsim.circuits import Quantum_Circuit
from many_body_qsim.evolution import exact_evolve, trotter_evolve
from many_body_qsim.gates import GATES

'''Test if norm is preserved after evolution'''

H = {'XHXH' : 5}

def test_exact_evolve_norm():
    t = 1
    qc0 = Quantum_Circuit(4)
    qc = qc0.copy()
    exact_evolve(qc, H, t)

    assert np.isclose(np.linalg.norm(qc.state), 1.0)
    
def test_trotter_evolve_norm():
    t = 1
    qc0 = Quantum_Circuit(4)
    qc = qc0.copy()
    trotter_evolve(qc, H, time = t, trotter_steps = 10)

    assert np.isclose(np.linalg.norm(qc.state), 1.0)
