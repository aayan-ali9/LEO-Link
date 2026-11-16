LEO-Link
Satellite Communications & Digital Signal Processing Simulator

LEO-Link is a software-only engineering project exploring the transmission and recovery of digital data across a satellite communications link. The project is developed primarily in Python, with MATLAB/Simulink validation and Blender visualization planned for later stages.

The current development stage focuses on a BPSK communication chain with an additive white Gaussian noise (AWGN) channel. Orbital geometry, Doppler shift, physical link budgets, and higher-fidelity receiver models are planned extensions.
Current communication chain
Random bits --> BPSK modulation --> AWGN channel --> BPSK demodulation --> BER analysis
- Bit generation: Reproducible pseudorandom binary sequences using NumPy.
- BPSK transmitter: Maps bit 0 to +1 and bit 1 to -1 as complex baseband symbols.
- AWGN channel: Adds complex Gaussian noise at a specified energy-per-bit-to-noise-density ratio (Eb/N0).
- BPSK receiver: Uses hard decisions on the real component to recover binary data, assuming ideal carrier synchronization.
- BER analysis: Compares transmitted and recovered bits to measure the bit error rate.
- Automated tests: Tests for symbol mapping, reproducibility, AWGN behavior, demodulation, and end-to-end BER calculations.
Mathematical model
For BPSK, transmitted symbols are
\[
s_k = 1 - 2b_k, \qquad b_k \in \{0,1\}.
\]
The channel adds Gaussian noise:
\[
r_k = s_k + n_k.
\]
The bit error rate is
\[
\mathrm{BER} = \frac{\text{incorrectly recovered bits}}{\text{total transmitted bits}}.
\]
For coherent, uncoded BPSK over AWGN, the theoretical BER is
\[
P_b = \frac{1}{2}\operatorname{erfc}\!\left(\sqrt{E_b/N_0}\right).
\]
Comparing simulated BER against this theoretical expression is the next validation milestone.

Current assumptions: Symbol-level complex baseband, ideal timing and carrier synchronization, uncoded BPSK, and AWGN. The model does not yet represent a complete satellite RF downlink.
Running the project
From the repository root, create a Python virtual environment and install the dependencies (Windows PowerShell):
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Run the end-to-end BER simulation:
.\.venv\Scripts\python.exe -m src.analysis.ber
Run automated tests:
.\.venv\Scripts\python.exe -m pytest -q
The simulation reports the measured BER at several Eb/N0 values. Finite sample sizes cause small deviations from theoretical results.
Repository structure
src/
├── transmitter/
│   ├── bit_generator.py
│   └── bpsk.py
├── channel/
│   └── awgn.py
├── receiver/
│   └── bpsk.py
└── analysis/
    └── ber.py
tests/
requirements.txt
README.md
Development roadmap
- [x] Initialize Git repository and Python environment
- [x] Implement reproducible binary data generation
- [x] Implement BPSK symbol modulation
- [x] Implement complex AWGN channel
- [x] Implement BPSK hard-decision receiver
- [x] Connect transmitter, channel, and receiver for BER measurement
- [ ] Compare simulated BER against theoretical BPSK performance and plot results
- [ ] Add QPSK modulation and demodulation
- [ ] Add pulse shaping, filtering, and synchronization
- [ ] Model orbital visibility, Doppler, and satellite link budgets
- [ ] Validate selected components independently in MATLAB/Simulink
- [ ] Build a Blender visualization driven by simulation data
Development approach
LEO-Link is developed through small, focused Git commits. Each feature is tested before being integrated into the next stage. This repository documents the mathematical models, assumptions, verification work, and engineering tradeoffs as the simulator grows.