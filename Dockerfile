FROM python:3-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt
RUN python setup.py install

COPY . /usr/src/app

CMD ["python3", "-m", "swagger_server.server"]
