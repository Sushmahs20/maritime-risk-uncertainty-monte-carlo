from src.simulation import simulate_eta_hours
from src.risk_metrics import summarize_risk
from src.plotting import plot_eta_distribution


def main():
    samples = simulate_eta_hours(
        distance_nm=1200,
        expected_speed_knots=14,
        n_sims=20000
    )

    summary = summarize_risk(samples, late_threshold_hours=110)
    print("Risk summary:", summary)

    plot_eta_distribution(samples, save_path="reports/figures/eta_hist.png")


if __name__ == "__main__":
    main()
