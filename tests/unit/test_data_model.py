from unittest import TestCase

import pandas as pd

from src.data_model import ModelInput


class TestDataModel(TestCase):

    def test_model_input(self):
        model_input = ModelInput(
            dataset_name='test',
            data=[
                {'month': '2020-01-01', 'value': 1},
                {'month': '2020-01-02', 'value': 2},
                {'month': '2020-01-03', 'value': 3},
            ]
        )

        self.assertEqual(model_input.dataset_name, 'test')
        self.assertEqual(len(model_input.data), 3)

    def test_model_input_from_df(self):
        df = pd.read_csv('data/random-time-series.csv')
        model_input = ModelInput.from_df(df, 'test')
        self.assertEqual(model_input.dataset_name, 'test')
        self.assertEqual(len(model_input.data), 42)

    def test_to_series_and_back(self):
        df = pd.read_csv('data/random-time-series.csv')
        model_input = ModelInput.from_df(df, 'test')
        series = model_input.get_darts_timeseries()
        model_input2 = ModelInput.from_df(series.pd_dataframe().reset_index(), 'test')
        self.assertEqual(model_input2.dataset_name, 'test')
        self.assertEqual(len(model_input2.data), 42)
