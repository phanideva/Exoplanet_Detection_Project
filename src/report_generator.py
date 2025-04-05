# Report Generator Module

import matplotlib.pyplot as plt
import pandas as pd

def run():
    print("Generating summary report...")
    try:
        df = pd.read_csv("data/kepler10_lightcurve.csv")
        plt.figure()
        plt.plot(df['time'], df['flux'])
        plt.title("Processed Light Curve")
        plt.xlabel("Time (days)")
        plt.ylabel("Flux")
        plt.savefig("data/final_lightcurve.png")
        print("Final light curve saved to data/final_lightcurve.png")
    except Exception as e:
        print("Failed to generate report:", e)
