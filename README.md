# Maritime ETA Risk & Uncertainty Modelling (Monte Carlo Simulation)

This project demonstrates how uncertainty in maritime operations can be quantified using Monte Carlo simulation.  
It models ship arrival time (ETA) variability driven by weather impact, route deviation, and port congestion, and translates uncertainty into actionable risk metrics.

---

## Problem Statement
In maritime operations, ETA predictions are affected by multiple uncertain factors such as weather conditions, routing changes, and port congestion.  
Point estimates alone are insufficient for operational planning.

This project answers:
- What is the **distribution** of possible arrival times?
- What is the **risk of late arrival** beyond a defined threshold?
- How does uncertainty propagate through the system?

---

## Approach
- Monte Carlo simulation with **20,000 stochastic runs**
- Explicit modelling of key uncertainty drivers:
  - Weather-driven speed reduction (lognormal distribution)
  - Route deviation (percentage increase in distance)
  - Port congestion delays (heavy-tailed distribution)
- Separation of concerns:
  - Simulation
  - Risk metrics
  - Visualisation

---

## Key Outputs
- Mean ETA ≈ **95 hours**
- P50 ETA ≈ **94 hours**
- P90 ETA ≈ **107 hours**
- P95 ETA ≈ **111 hours**
- Probability of late arrival (>110 hours) ≈ **6.2%**

These metrics enable risk-aware decision-making rather than relying on single-point predictions.

---

## Risk Metrics
The following risk measures are computed:
- Mean arrival time
- Percentile-based estimates (P50, P90, P95)
- Probability of breaching a late-arrival threshold
- Full ETA distribution for scenario analysis

---

## Assumptions
- Weather impact is modeled as a multiplicative speed factor
- Port congestion delays follow a heavy-tailed gamma distribution
- Route deviations are small positive distance adjustments
- Uncertainty sources are assumed independent

---

## Limitations
- Synthetic data is used (framework is extensible to real AIS or port datasets)
- Simplified maritime dynamics
- Independence assumptions may not hold in extreme scenarios

---

## How to Run
```bash
pip install -r requirements.txt
python run_demo.py

