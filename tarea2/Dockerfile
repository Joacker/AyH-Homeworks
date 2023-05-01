 FROM python:3.6-alpine

WORKDIR /app

COPY ./app /app

RUN apk add g++ jpeg-dev zlib-dev libjpeg make
RUN pip3 install matplotlib

CMD tail -f /dev/null