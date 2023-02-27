from typing import List

import pandas as pd
from darts import TimeSeries
from pydantic import BaseModel


class DataPoint(BaseModel):
    """Data point for the model"""
    month: str  # YYYY-MM-01 format
    value: float


class ModelInput(BaseModel):
    """Input data for the model

    data should be scaled with darts.dataprocessing.transformers.Scaler
    """
    data: List[DataPoint]
    dataset_name: str = None

    @classmethod
    def from_df(cls, df: pd.DataFrame, dataset_name: str = None):
        """Load data from csv file
        this csv should only have two columns,
        one column must be Month and the other must be value but name doesn't matter
        """
        other_column = [col for col in df.columns if col != 'Month'][0]

        data = [DataPoint(month=str(row['Month']), value=float(row[other_column])) for _, row in df.iterrows()]
        return cls(data=data, dataset_name=dataset_name)

    def get_darts_timeseries(self):
        """Convert data to darts TimeSeries"""
        df = pd.DataFrame([{'Month': dp.month, 'value': dp.value} for dp in self.data])
        df['Month'] = pd.to_datetime(df['Month'])
        return TimeSeries.from_dataframe(df, time_col='Month', value_cols=['value'])


if __name__ == '__main__':
    # Example usage
    dataframe = pd.read_csv('../data/monthly-milk.csv')
    model_input = ModelInput.from_df(dataframe, 'test')
    print(model_input)
    series = model_input.darts_timeseries()
    print(series)
