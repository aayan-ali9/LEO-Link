
import numpy as np


def modulate_bpsk(bits):
    """Convert binary bits into BPSK symbols."""

    bits = np.asarray(bits)

    if bits.ndim != 1 or bits.size == 0:
        raise ValueError("Input must be a nonempty 1D array")

    if not np.all((bits == 0) | (bits == 1)):
        raise ValueError("Input must contain only 0 and 1")

    # Map 0 to +1 and 1 to -1
    symbols = 1.0 - 2.0 * bits.astype(float)

    return symbols.astype(np.complex128)


if __name__ == "__main__":

    from src.transmitter.bit_generator import generate_bits

    bits = generate_bits(10, seed=42)

    symbols = modulate_bpsk(bits)

    print("Original bits:", bits)
    print("BPSK symbols:", symbols)
    print("Symbol energy:", np.mean(np.abs(symbols)**2))
