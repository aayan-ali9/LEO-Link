
import numpy as np


def generate_bits(num_bits, seed=None):
    """Generate a sequence of random binary bits."""

    if num_bits <= 0:
        raise ValueError("Number of bits must be positive")

    rng = np.random.default_rng(seed)

    bits = rng.integers(0, 2, size=num_bits, dtype=np.uint8)

    return bits


if __name__ == "__main__":

    bits = generate_bits(20, seed=42)

    print("Generated bits:", bits)
    print("Total bits:", len(bits))
    print("Fraction of ones:", np.mean(bits))
