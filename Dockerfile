FROM python:3.10

ENV FLASK_APP=<lb>

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY . /opt

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $1736