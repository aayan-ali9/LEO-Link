
import numpy as np


def modulate_qpsk(bits):
    """Convert pairs of bits into QPSK symbols."""

    bits = np.asarray(bits)

    if bits.ndim != 1 or bits.size == 0:
        raise ValueError("Input must be a nonempty 1D array")

    if bits.size % 2 != 0:
        raise ValueError("QPSK requires an even number of bits")

    if not np.all((bits == 0) | (bits == 1)):
        raise ValueError("Bits must contain only 0 and 1")

    # Group bits into pairs
    pairs = bits.reshape(-1, 2).astype(float)

    # Map each bit to +1 or -1
    i = 1.0 - 2.0 * pairs[:, 0]
    q = 1.0 - 2.0 * pairs[:, 1]

    # Construct normalized complex symbols
    symbols = (i + 1j * q) / np.sqrt(2)

    return symbols


if __name__ == "__main__":

    from src.transmitter.bit_generator import generate_bits

    bits = generate_bits(10, seed=42)
    symbols = modulate_qpsk(bits)

    print("Original bits:", bits)
    print("QPSK symbols:", np.round(symbols, 3))
    print("Number of symbols:", len(symbols))
    print("Average symbol energy:", np.mean(np.abs(symbols)**2))
