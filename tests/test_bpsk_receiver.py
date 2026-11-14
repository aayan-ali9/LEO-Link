
import numpy as np

from src.receiver.bpsk import demodulate_bpsk


def test_noisy_bpsk_recovery():
    received = [0.9+0.1j, -1.2+0.3j, -0.7-0.4j, 1.1-0.2j]

    bits = demodulate_bpsk(received)

    np.testing.assert_array_equal(bits, [0, 1, 1, 0])
