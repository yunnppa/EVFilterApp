import pandas as pd
from app.models import EV



class EVFilter:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)

    def filter_by_brand(self, brand):
        results = self.df[self.df['Brand'].str.lower() == brand.lower()]
        return [
            EV(
                row['Brand'],
                row['Model'],
                row['BatteryCapacity(kWh)'],
                row['Range(km)'],
                row['Seats']
            ) for _, row in results.iterrows()
        ]
