# Transit Detection Module

import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def run():
    print("Running transit detection...")
    df = pd.read_csv("data/kepler10_lightcurve.csv")
    time = df['time'].values
    flux = df['flux'].values

    peaks, _ = find_peaks(-flux, height=0.995, distance=100)
    
    plt.figure()
    plt.plot(time, flux)
    plt.plot(time[peaks], flux[peaks], "x")
    plt.title("Transit Detections")
    plt.xlabel("Time (days)")
    plt.ylabel("Normalized Flux")
    plt.savefig("data/transit_detection.png")
    print("Transit detection plot saved to data/transit_detection.png")
