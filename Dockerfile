FROM python:3.7

WORKDIR /src

RUN mkdir app

COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

WORKDIR /src/app

CMD streamlit run --server.port $PORT app.py




