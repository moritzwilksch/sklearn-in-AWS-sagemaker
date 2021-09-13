FROM python:slim

RUN apt-get update \
    && apt-get upgrade -y
    #&& apt-get install venv \
    # pip install venv \
    #&& python3 -m venv .env \
    #&& source .env/bin/activate

COPY ./code ./data ./requirements.txt ./

RUN pip install -r requirements.txt