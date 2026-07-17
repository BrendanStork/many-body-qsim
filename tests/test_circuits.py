
import numpy as np

from many_body_qsim.circuits import Quantum_Circuit


def test_single_qubit_x_gate():

    qc = Quantum_Circuit(1)

    qc.x(0)

    state = qc.state

    np.testing.assert_allclose(
        state,
        np.array([0,1])
    )
