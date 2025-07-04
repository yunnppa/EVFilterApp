from app.filters import EVFilter
import pandas as pd
from app.filters import EVFilter

def test_filters_by_brand(tmp_path):
    data = {
        "Brand": ["Tesla", "Nissan", "Tesla"],
        "Model": ["Model S", "Leaf", "Model 3"],
        "BatteryCapacity(kWh)": [100, 40, 75],
        "Range(km)": [600, 240, 500],
        "Seats": [5, 5, 5]
    }
    test_file = tmp_path / "test_ev.csv"
    pd.DataFrame(data).to_csv(test_file, index=False)

    ev_filter = EVFilter(test_file)
    results = ev_filter.filter_by_brand("Tesla")
    assert len(results) == 2
    assert results[0].model == "Model S"
