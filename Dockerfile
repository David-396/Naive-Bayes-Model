FROM python:3.12-alpine

COPY requirements.txt .
RUN pip install --upgrade pip && pip --no-cache-dir install -r requirements.txt

WORKDIR Naive_Bayes
VOLUME /Naive_Bayes/data/

COPY . .

CMD ["python", "main.py"]
CMD ["FastAPI", "dev", "server_side/run_server.py"]