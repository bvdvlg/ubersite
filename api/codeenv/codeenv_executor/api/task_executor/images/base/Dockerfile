FROM python:3.9

WORKDIR /code

COPY ./images/base/requirements.txt /code/deployment/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/deployment/requirements.txt

COPY . /code

ENV PYTHONPATH="/code"

CMD ["python3", "main.py"]
