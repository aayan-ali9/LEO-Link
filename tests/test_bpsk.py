
import numpy as np
import pytest

from src.transmitter.bpsk import modulate_bpsk
from src.transmitter.bit_generator import generate_bits


def test_symbol_mapping():
    bits = np.array([0, 1, 1, 0])
    expected = np.array([1, -1, -1, 1])

    symbols = modulate_bpsk(bits)

    np.testing.assert_array_equal(symbols, expected)


def test_generated_bits():
    bits = generate_bits(1000, seed=42)
    symbols = modulate_bpsk(bits)

    assert len(symbols) == len(bits)
    assert np.iscomplexobj(symbols)


def test_unit_energy():
    bits = generate_bits(1000, seed=42)
    symbols = modulate_bpsk(bits)

    energy = np.mean(np.abs(symbols)**2)

    assert np.isclose(energy, 1.0)


def test_invalid_bits():
    with pytest.raises(ValueError):
        modulate_bpsk([0, 1, 2, 0])


def test_empty_input():
    with pytest.raises(ValueError):
        modulate_bpsk([])
