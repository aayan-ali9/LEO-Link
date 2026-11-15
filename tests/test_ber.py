
import numpy as np
import pytest

from src.analysis.ber import calculate_ber, simulate_ber


def test_known_errors():
    original = [0, 1, 0, 1]
    recovered = [0, 0, 0, 1]

    assert calculate_ber(original, recovered) == 0.25


def test_perfect_transmission():
    bits = [0, 1, 1, 0]

    assert calculate_ber(bits, bits) == 0.0


def test_higher_snr_reduces_errors():
    low_snr = simulate_ber(100_000, 0)
    high_snr = simulate_ber(100_000, 8)

    assert high_snr < low_snr


def test_reproducibility():
    first = simulate_ber(100_000, 4, seed=42)
    second = simulate_ber(100_000, 4, seed=42)

    assert first == second


def test_invalid_length():
    with pytest.raises(ValueError):
        calculate_ber([0, 1, 0], [0, 1])
