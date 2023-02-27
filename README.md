# Time Series Example

## Introduction

This is the implementation of simple time series.  
[NBEATSModel](https://arxiv.org/abs/1905.10437) was trained on two datasets in [notebook](notebooks/nbeat_model.ipynb):

1. air_passengers - [dataset](https://github.com/unit8co/darts/blob/master/datasets/AirPassengers.csv)
2. milk_production - [dataset](https://github.com/unit8co/darts/blob/master/datasets/monthly-milk.csv)

For evaluation of the model last 36 data points were held out.

## Deployment

With Docker

```bash
docker build -t time-series-example .
docker run -d -p 8000:8000 --name time-series-example time-series-example
```

*but you need NBEATSModel to be saved in data/models/nbeats_model

Once it is up and running you can test it by running, by default it will predict 10 datapoints

```bash
python send_request.py
```

Also, there is api endpoint called train which should be used to train the model. On another server but it's not
actually implemented, simply because it's out of the scope, and it needs resources to train.

You could use AWS Sagemaker to start training exps there.
