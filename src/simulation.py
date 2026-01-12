import numpy as np


def simulate_eta_hours(
    distance_nm: float,
    expected_speed_knots: float,
    n_sims: int = 10000,
    seed: int = 7,
):
    rng = np.random.default_rng(seed)

    weather_factor = rng.lognormal(mean=-0.03, sigma=0.10, size=n_sims).clip(0.6, 1.1)
    port_congestion = rng.gamma(shape=2.0, scale=2.0, size=n_sims)
    route_dev = rng.normal(0.02, 0.015, size=n_sims).clip(0.0, 0.2)

    effective_distance = distance_nm * (1 + route_dev)
    sea_time = effective_distance / (expected_speed_knots * weather_factor)

    noise = rng.normal(0, 1.0, size=n_sims)
    eta_hours = (sea_time + port_congestion + noise).clip(0.1, None)

    return eta_hours

