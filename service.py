from darts.dataprocessing.transformers import Scaler
from darts.models import NBEATSModel
from fastapi import FastAPI

from src.data_model import ModelInput

app = FastAPI()
model = NBEATSModel.load('data/models/nbeats_model')


@app.get('/predict')
def predict(input_data: ModelInput, values_to_predict: int = 10):
    print(input_data, values_to_predict)

    series = input_data.get_darts_timeseries()
    series = Scaler().fit_transform(series)
    prediction = model.predict(n=values_to_predict, series=series)
    output_data = ModelInput.from_df(prediction.pd_dataframe().reset_index(), input_data.dataset_name)
    return {'prediction': output_data}


@app.post('/train')
def train(train_data_path: str):
    # the idea is that, when hitting this endpoint,
    # the model should trigger training job on another server
    return {'message': 'Model training started successfully'}
