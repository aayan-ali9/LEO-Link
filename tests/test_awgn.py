
import numpy as np
import pytest

from src.channel.awgn import add_awgn
from src.transmitter.bit_generator import generate_bits
from src.transmitter.bpsk import modulate_bpsk


def test_received_signal_shape():
    symbols = modulate_bpsk(generate_bits(100, seed=42))
    received = add_awgn(symbols, eb_n0_db=6, seed=1)

    assert received.shape == symbols.shape
    assert np.iscomplexobj(received)


def test_reproducible_noise():
    symbols = modulate_bpsk(generate_bits(100, seed=42))

    first = add_awgn(symbols, eb_n0_db=6, seed=1)
    second = add_awgn(symbols, eb_n0_db=6, seed=1)

    np.testing.assert_array_equal(first, second)


def test_noise_power_matches_theory():
    symbols = modulate_bpsk(generate_bits(100_000, seed=42))
    received = add_awgn(symbols, eb_n0_db=10, seed=1)

    measured = np.mean(np.abs(received - symbols) ** 2)
    expected = 10 ** (-10 / 10)

    assert np.isclose(measured, expected, rtol=0.03)


def test_higher_ebn0_means_less_noise():
    symbols = modulate_bpsk(generate_bits(1000, seed=42))

    low = add_awgn(symbols, eb_n0_db=0, seed=1)
    high = add_awgn(symbols, eb_n0_db=10, seed=1)

    low_power = np.mean(np.abs(low - symbols) ** 2)
    high_power = np.mean(np.abs(high - symbols) ** 2)

    assert high_power < low_power


@pytest.mark.parametrize("symbols,eb_n0_db,bits_per_symbol", [
    ([], 6, 1),
    (np.ones((2, 2)), 6, 1),
    ([np.nan], 6, 1),
    ([0j, 0j], 6, 1),
    ([1 + 0j], np.nan, 1),
    ([1 + 0j], 6, 0),
])
def test_invalid_inputs(symbols, eb_n0_db, bits_per_symbol):
    with pytest.raises(ValueError):
        add_awgn(symbols, eb_n0_db, bits_per_symbol)
