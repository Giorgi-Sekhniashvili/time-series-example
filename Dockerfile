FROM hiredscorelabs/pytorch:python3.9.5-1.7.1-cuda10.1-cudnn7-runtime


RUN apt-get update

WORKDIR /code
EXPOSE 8000


COPY requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt

COPY . /code

CMD ["uvicorn", "service:app", "--host", "0.0.0.0", "--port", "8000"]