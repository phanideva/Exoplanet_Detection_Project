# 🛰️ Exoplanet Detection & Material Estimation

This project builds an end-to-end **astronomical analysis pipeline** to detect exoplanets from light curve data and estimate their material composition using modern Python-based data science techniques.

---

## 🎯 Objective

- Detect exoplanets from real NASA Kepler mission light curve data.
- Analyze transit events (dips in brightness when a planet crosses its star).
- Use machine learning to classify transit likelihood.
- Estimate planet composition (rocky/gassy) using Bayesian inference.
- Generate plots and reports for interpretation.

---

## 🔬 Project Description

This pipeline mimics real workflows used in astrophysics and space missions like Kepler, TESS, and JWST. It combines:

- Astronomical data processing
- Signal processing for transit detection
- Machine learning classification
- Bayesian statistics for material estimation

The project demonstrates how to analyze light curve time-series data and infer planetary characteristics — a core task in modern exoplanetary science.

---

## 🧠 How It Works

### 🔭 1. Data Processing (`data_processing.py`)

- Downloads the light curve of the star **Kepler-10** from NASA’s Kepler mission.
- Normalizes and flattens the brightness curve.
- Saves data to `data/kepler10_lightcurve.csv`.

### 🌑 2. Transit Detection (`transit_detection.py`)

- Identifies brightness "dips" using signal processing.
- Detects candidate exoplanet transits.
- Saves a plot to `data/transit_detection.png`.

### 🧠 3. ML Classification (`ml_model.py`)

- Simulates an ML model that classifies transit likelihood based on light curve statistics.
- Uses Random Forest for mock classification.
- Saves accuracy to `models/ml_results.txt`.

### 🪨 4. Bayesian Material Estimation (`bayesian_composition.py`)

- Uses Bayesian inference (via PyMC) to estimate whether the exoplanet is **rocky or gaseous** based on albedo.
- Saves a traceplot to `data/bayesian_composition_trace.png`.

### 📊 5. Report Generator (`report_generator.py`)

- Outputs final cleaned light curve to `data/final_lightcurve.png`.

---

## 📁 Outputs

| File                                  | Description                             |
| ------------------------------------- | --------------------------------------- |
| `data/kepler10_lightcurve.csv`        | Light curve brightness vs. time         |
| `data/transit_detection.png`          | Transit event detection plot            |
| `models/ml_results.txt`               | ML classification accuracy              |
| `data/bayesian_composition_trace.png` | Posterior plot for composition estimate |
| `data/final_lightcurve.png`           | Final cleaned light curve visualization |

---

## 🚀 How to Run

### 📦 Setup

1. Clone the repo:

```bash
git clone https://github.com/your-username/Exoplanet_Detection.git
cd Exoplanet_Detection
```

🔍 How to Analyze the Results
Light Curve Plot: Dips indicate potential transits.

Transit Detection: "X" marks confirm possible planetary crossings.

ML Accuracy: Should reflect quality of signal classification.

Bayesian Traceplot: Visualizes confidence that the planet is rocky.

CSV File: Explore raw brightness data and patterns.

🌌 Real-World Applications
Automated exoplanet discovery pipelines (like NASA ExoMiner)

Analyzing planetary systems in Kepler and TESS archives

Simulating material compositions of Earth-like worlds

Training AI for next-gen space telescopes (JWST, PLATO)

🛠️ Future Ideas
Feature Description
LSTM Deep Learning Time-series classification of noisy light curves
Streamlit Dashboard Interactive UI for dynamic exploration
NASA PDS Material Integration Compare reflectance spectra to infer surface types
Real Confirmed Planets Use Kepler confirmed catalog for training ML

🤖 Tech Stack
Python 3.9+

Lightkurve

Pandas, NumPy, SciPy, Matplotlib

Scikit-learn (ML)

PyMC (Bayesian modeling)

Astropy (data formats)

Astroquery (NASA MAST access)
