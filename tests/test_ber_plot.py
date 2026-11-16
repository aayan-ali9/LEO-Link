
import numpy as np

from src.analysis.ber import simulate_ber
from src.analysis.ber_plot import theoretical_bpsk_ber


def test_theoretical_ber():
    result = theoretical_bpsk_ber(0)

    assert np.isclose(result, 0.0786496, rtol=1e-5)


def test_ber_matches_theory():
    num_bits = 200_000

    for snr in [0, 4, 8]:
        measured = simulate_ber(num_bits, snr, seed=42)
        expected = float(theoretical_bpsk_ber(snr))

        # Allow for random sampling uncertainty
        standard_error = np.sqrt(
            expected * (1 - expected) / num_bits
        )

        tolerance = 5 * standard_error + 1 / num_bits

        assert abs(measured - expected) < tolerance
