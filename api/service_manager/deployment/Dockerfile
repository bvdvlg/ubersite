FROM python:3.9

WORKDIR /code

COPY deployment/requirements.txt /code/deployment/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/deployment/requirements.txt

COPY ./ /code/

ENV PYTHONPATH="/code"

CMD ["python3", "deployment/main.py", "--host", "0.0.0.0", "--port", "80"]
