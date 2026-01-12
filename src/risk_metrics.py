import numpy as np


def summarize_risk(samples: np.ndarray, late_threshold_hours: float) -> dict:
    samples = np.asarray(samples)

    return {
        "mean": float(np.mean(samples)),
        "p50": float(np.percentile(samples, 50)),
        "p90": float(np.percentile(samples, 90)),
        "p95": float(np.percentile(samples, 95)),
        "prob_late": float(np.mean(samples > late_threshold_hours)),
    }

