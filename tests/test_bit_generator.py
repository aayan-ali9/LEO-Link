
import numpy as np

from src.transmitter.bit_generator import generate_bits


def test_bit_count():
    bits = generate_bits(1000, seed=42)

    assert len(bits) == 1000


def test_binary_values():
    bits = generate_bits(1000, seed=42)

    assert np.all((bits == 0) | (bits == 1))


def test_reproducibility():
    bits1 = generate_bits(1000, seed=42)
    bits2 = generate_bits(1000, seed=42)

    assert np.array_equal(bits1, bits2)
