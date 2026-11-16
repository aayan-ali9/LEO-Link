
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

from src.analysis.ber import simulate_ber


def theoretical_bpsk_ber(eb_n0_db):
    """Calculate theoretical BPSK BER in AWGN."""

    eb_n0 = 10 ** (np.asarray(eb_n0_db) / 10)

    return 0.5 * erfc(np.sqrt(eb_n0))


def plot_ber():
    """Compare simulated and theoretical BPSK BER."""

    snr_values = np.array([0, 2, 4, 6, 8])
    num_bits = 200_000

    # Run the existing communication simulation
    simulated = np.array([
        simulate_ber(num_bits, snr, seed=42)
        for snr in snr_values
    ])

    # Calculate the theoretical BER curve
    snr_smooth = np.linspace(0, 8, 200)
    theoretical = theoretical_bpsk_ber(snr_smooth)

    # Plot both results
    plt.figure(figsize=(8, 5))

    plt.semilogy(
        snr_smooth, theoretical,
        label="Theoretical BPSK",
        linewidth=2
    )

    plt.semilogy(
        snr_values, simulated,
        "o", label="Simulated BPSK"
    )

    plt.xlabel("Eb/N0 (dB)")
    plt.ylabel("Bit Error Rate")
    plt.title("BPSK Performance in AWGN")
    plt.grid(True, which="both", alpha=0.3)
    plt.legend()
    plt.tight_layout()

    # Save the plot
    output = Path("results")
    output.mkdir(exist_ok=True)

    plt.savefig(output / "bpsk_ber.png", dpi=200)
    plt.show()

    # Print numerical results
    for snr, ber in zip(snr_values, simulated):
        theory = float(theoretical_bpsk_ber(snr))
        print(
            f"{snr} dB | "
            f"Simulated: {ber:.6f} | "
            f"Theoretical: {theory:.6f}"
        )


if __name__ == "__main__":
    plot_ber()
