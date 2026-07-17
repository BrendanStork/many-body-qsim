import numpy as np

from many_body_qsim.gates import GATES

X = GATES['X']
Y = GATES['Y']
Z = GATES['Z']
H = GATES['H']
I = np.eye(2)

def test_pauli_square():
    """Pauli matrices squared should equal identity."""

    np.testing.assert_allclose(X @ X, I)
    np.testing.assert_allclose(Y @ Y, I)
    np.testing.assert_allclose(Z @ Z, I)


def test_hadamard_is_unitary():
    
    np.testing.assert_allclose(
        H.conj().T @ H,
        np.eye(2), atol=1e-15
    )
