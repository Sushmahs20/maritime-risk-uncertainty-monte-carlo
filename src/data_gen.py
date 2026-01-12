import numpy as np
import pandas as pd


def generate_voyages(n: int = 5000, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    distance_nm = rng.uniform(200, 2500, size=n)
    base_speed = rng.normal(14, 2.0, size=n).clip(8, 22)

    weather_factor = rng.lognormal(mean=-0.03, sigma=0.08, size=n).clip(0.65, 1.05)
    port_congestion_hours = rng.gamma(shape=2.0, scale=2.0, size=n)
    route_deviation_pct = rng.normal(0.02, 0.015, size=n).clip(0.0, 0.15)

    effective_distance = distance_nm * (1 + route_deviation_pct)
    sea_time_hours = effective_distance / (base_speed * weather_factor)

    noise = rng.normal(0, 1.5, size=n)
    actual_travel_hours = (sea_time_hours + port_congestion_hours + noise).clip(1, None)

    return pd.DataFrame({
        "distance_nm": distance_nm,
        "base_speed_knots": base_speed,
        "weather_factor": weather_factor,
        "port_congestion_hours": port_congestion_hours,
        "route_deviation_pct": route_deviation_pct,
        "actual_travel_hours": actual_travel_hours,
    })

