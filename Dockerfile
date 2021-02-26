FROM python:3.7

WORKDIR /src

RUN mkdir app

COPY ./app ./app

RUN cd app\
    && pip install pipenv\
    && pipenv install --system --deploy

COPY . .

WORKDIR /src/app

CMD ["streamlit", "run", "app.py"]




