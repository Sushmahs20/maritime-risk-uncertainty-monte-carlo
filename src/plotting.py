import numpy as np
import matplotlib.pyplot as plt


def plot_eta_distribution(samples, save_path=None):
    plt.figure()
    plt.hist(samples, bins=60)
    plt.xlabel("ETA (hours)")
    plt.ylabel("Frequency")
    plt.title("Simulated ETA distribution")

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")

    plt.show()

