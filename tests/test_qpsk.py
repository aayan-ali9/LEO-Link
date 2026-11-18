
import numpy as np
import pytest

from src.transmitter.qpsk import modulate_qpsk
from src.transmitter.bit_generator import generate_bits


def test_symbol_mapping():
    bits = [0, 0, 0, 1, 1, 1, 1, 0]

    expected = np.array([
        1 + 1j,
        1 - 1j,
        -1 - 1j,
        -1 + 1j
    ]) / np.sqrt(2)

    symbols = modulate_qpsk(bits)

    np.testing.assert_allclose(symbols, expected)


def test_symbol_count():
    bits = generate_bits(1000, seed=42)
    symbols = modulate_qpsk(bits)

    assert len(symbols) == 500


def test_unit_energy():
    bits = generate_bits(1000, seed=42)
    symbols = modulate_qpsk(bits)

    energy = np.mean(np.abs(symbols)**2)

    assert np.isclose(energy, 1.0)


def test_complex_output():
    symbols = modulate_qpsk([0, 1, 1, 0])

    assert np.iscomplexobj(symbols)


@pytest.mark.parametrize("bits", [
    [],
    [0, 1, 1],
    [0, 2],
    [[0, 1], [1, 0]]
])
def test_invalid_input(bits):
    with pytest.raises(ValueError):
        modulate_qpsk(bits)
