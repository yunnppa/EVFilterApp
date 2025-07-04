import pandas as pd
from app.filters import EVFilter


def test_filter_by_brand():
    test_data = {
        "Brand": ["Tesla", "Nissan", "Tesla"],
        "Model": ["Model S", "Leaf", "Model 3"],
        "BatteryCapacity(kWh)": [100, 40, 75],
        "Range(km)": [600, 240, 500],
        "Seats": [5, 5, 5]
    }
    df = pd.DataFrame(test_data)
    df.to_csv("data/test_ev_data.csv", index=False)

    ev_filter = EVFilter("data/test_ev_data.csv")
    results = ev_filter.filter_by_brand("Tesla")
    assert len(results) == 2
    assert results[0].model == "Model S"
    assert results[1].range_km == 500
