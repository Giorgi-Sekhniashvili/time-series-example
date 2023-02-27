import pandas as pd
import requests

from src.data_model import ModelInput


def send_test_request():
    df = pd.read_csv('data/random-time-series.csv')
    model_input = ModelInput.from_df(df, 'test')
    response = requests.get('http://localhost:8000/predict/',
                            json=model_input.dict())

    print(response.json())
    print(len(response.json()['prediction']['data']))


if __name__ == '__main__':
    send_test_request()
