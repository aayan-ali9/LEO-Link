
import numpy as np


def add_awgn(symbols, eb_n0_db, bits_per_symbol=1, seed=None):
    """Add complex AWGN at a chosen Eb/N0 to baseband symbols."""

    symbols = np.asarray(symbols, dtype=np.complex128)

    if symbols.ndim != 1 or symbols.size == 0:
        raise ValueError("Symbols must be a nonempty 1D array")

    if not np.all(np.isfinite(symbols)):
        raise ValueError("Symbols must be finite")

    if not np.isfinite(eb_n0_db):
        raise ValueError("Eb/N0 must be finite")

    if not isinstance(bits_per_symbol, (int, np.integer)) or bits_per_symbol < 1:
        raise ValueError("bits_per_symbol must be a positive integer")

    # Average transmitted symbol energy
    symbol_energy = np.mean(np.abs(symbols) ** 2)

    if symbol_energy == 0:
        raise ValueError("Average symbol energy must be positive")

    # Convert Eb/N0 from dB to linear
    eb_n0 = 10.0 ** (eb_n0_db / 10.0)

    # Calculate the noise level
    n0 = symbol_energy / (bits_per_symbol * eb_n0)
    noise_std = np.sqrt(n0 / 2.0)

    # Generate complex Gaussian noise
    rng = np.random.default_rng(seed)

    noise = noise_std * (
        rng.standard_normal(symbols.size)
        + 1j * rng.standard_normal(symbols.size)
    )

    return symbols + noise


if __name__ == "__main__":
    from src.transmitter.bit_generator import generate_bits
    from src.transmitter.bpsk import modulate_bpsk

    bits = generate_bits(10_000, seed=42)
    symbols = modulate_bpsk(bits)

    eb_n0_db = 6.0
    received = add_awgn(symbols, eb_n0_db, seed=7)

    measured_noise_power = np.mean(np.abs(received - symbols) ** 2)
    expected_noise_power = 10.0 ** (-eb_n0_db / 10.0)

    print("Transmitted symbols:", symbols[:8])
    print("Received symbols:", np.round(received[:8], 3))
    print(f"Expected noise power: {expected_noise_power:.4f}")
    print(f"Measured noise power: {measured_noise_power:.4f}")
