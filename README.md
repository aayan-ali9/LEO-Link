
# LEO-Link

**Satellite Communications & Signal Processing Simulator**

LEO-Link is a Python project aimed at simulating how a satellite sends digital data to a ground station. The goal is to see how noise and other signal problems affect the data we receive, then develop ways to recover it reliably.

I'm building the communications system one part at a time. The current version covers a basic BPSK transmitter and receiver with simulated channel noise. Satellite-specific effects, including Doppler shift and changing signal strength, will be added later.

## How it works

```text
Generate bits → BPSK transmitter → Noisy channel → BPSK receiver → Measure errors
```

1. **Generate bits:** Create a repeatable sequence of zeros and ones.
2. **Modulate:** Convert each bit into a BPSK symbol (`0 → +1`, `1 → -1`).
3. **Add noise:** Simulate random noise in the communication channel.
4. **Receive:** Estimate the original bits from the noisy symbols.
5. **Measure errors:** Compare the received bits with the original data.

The main performance measure is **bit error rate (BER)**:

$$
\mathrm{BER}=\frac{\text{incorrectly received bits}}{\text{total transmitted bits}}
$$

A lower BER means fewer errors. Right now, the model assumes the transmitter and receiver are perfectly synchronized. More realistic receiver behavior will come later.

## Run it

From the project folder, using Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Run the end-to-end BPSK simulation:

```powershell
.\.venv\Scripts\python.exe -m src.analysis.ber
```

Run the tests:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

The simulation prints the measured BER for several signal-to-noise conditions. The exact values vary slightly because the channel noise is random.

## Project structure

```text
src/
  transmitter/
    bit_generator.py   # Generate bits
    bpsk.py            # Convert bits to BPSK symbols
  channel/
    awgn.py            # Add Gaussian noise
  receiver/
    bpsk.py            # Recover bits
  analysis/
    ber.py             # Calculate bit error rate
tests/                  # Automated tests
requirements.txt
README.md
```

## Progress

- [x] Generate reproducible binary data
- [x] Build a BPSK modulator
- [x] Add an AWGN noise model
- [x] Build a BPSK receiver
- [x] Connect the system and calculate BER
- [ ] Plot BER and compare it with theoretical results
- [ ] Add QPSK modulation
- [ ] Add filtering and receiver synchronization
- [ ] Model a LEO satellite link, including Doppler and path loss
- [ ] Compare selected results with MATLAB/Simulink
- [ ] Create a Blender visualization using simulation data

## Tools

**Python:** NumPy, SciPy, Matplotlib, pytest  
**Planned:** MATLAB/Simulink, Blender

I'm keeping the Git history incremental, with separate commits for each feature and its tests.
