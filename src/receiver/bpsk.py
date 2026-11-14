
import numpy as np


def demodulate_bpsk(received):
    """Recover binary bits from BPSK symbols."""

    received = np.asarray(received, dtype=np.complex128)

    if received.ndim != 1 or received.size == 0:
        raise ValueError("Received symbols must be a nonempty 1D array")

    if not np.all(np.isfinite(received)):
        raise ValueError("Received symbols must be finite")

    # Positive real value = 0, negative = 1
    return (received.real < 0).astype(np.uint8)
