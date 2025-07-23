FROM python:3.12-alpine

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR CLS_server/

COPY .. .

CMD ["python", "classifier_route.py"]
