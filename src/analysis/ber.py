
import numpy as np

from src.transmitter.bit_generator import generate_bits
from src.transmitter.bpsk import modulate_bpsk
from src.channel.awgn import add_awgn
from src.receiver.bpsk import demodulate_bpsk


def calculate_ber(original, recovered):
    """Calculate the fraction of incorrect bits."""

    original = np.asarray(original)
    recovered = np.asarray(recovered)

    if original.ndim != 1 or original.size == 0:
        raise ValueError("Original bits must be a nonempty 1D array")

    if original.shape != recovered.shape:
        raise ValueError("Bit sequences must have matching shapes")

    errors = np.count_nonzero(original != recovered)

    return errors / len(original)


def simulate_ber(num_bits, eb_n0_db, seed=42):
    """Simulate BPSK transmission through an AWGN channel."""

    bits = generate_bits(num_bits, seed=seed)
    symbols = modulate_bpsk(bits)

    # Transmit through noisy channel
    noise_seed = None if seed is None else seed + 1
    received = add_awgn(symbols, eb_n0_db, seed=noise_seed)

    # Recover bits
    recovered = demodulate_bpsk(received)

    return calculate_ber(bits, recovered)


if __name__ == "__main__":

    num_bits = 100_000

    for eb_n0 in [0, 4, 8]:
        ber = simulate_ber(num_bits, eb_n0)

        print(f"Eb/N0: {eb_n0} dB | BER: {ber:.6f}")
