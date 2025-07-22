FROM python:3.12-alpine

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR Naive_Bayes/

COPY . .

CMD ["python", "main.py"]
