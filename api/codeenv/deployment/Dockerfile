FROM ubuntu:23.04

WORKDIR /code

COPY ./deployment/requirements.txt /code/deployment/requirements.txt

RUN apt-get update && apt-get -y install curl 
RUN apt-get -y install python3 systemctl python3-pip && curl -sSL https://get.docker.com/ | sh && pip3 install --break-system-packages --no-cache-dir --upgrade -r /code/deployment/requirements.txt

COPY ./api /code/api
COPY ./configuration /code/configuration
COPY ./deployment/main.py /code/deployment/main.py

ENV PYTHONPATH="/code"

CMD ["python3", "deployment/main.py", "--host", "0.0.0.0", "--port", "80"]
