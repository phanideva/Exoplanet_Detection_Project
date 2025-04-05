# Bayesian Composition Module with PyMC v4

import pymc as pm
import matplotlib.pyplot as plt
import arviz as az

def run():
    print("Estimating planetary composition using Bayesian inference...")

    with pm.Model() as model:
        albedo = pm.Uniform('albedo', lower=0.0, upper=1.0)
        rocky_prob = pm.Deterministic('rocky', pm.math.sigmoid(10 * (0.35 - albedo)))
        trace = pm.sample(1000, tune=1000, chains=2, target_accept=0.9)

    az.plot_trace(trace)
    plt.savefig("data/bayesian_composition_trace.png")
    print("Trace plot saved to data/bayesian_composition_trace.png")
