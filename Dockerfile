FROM python:3.6
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r ./requirements.txt

COPY data /app/data
COPY saved_data /app/saved_data
COPY src /app/src
COPY deploy.py /app
CMD ["python", "deploy.py"]~
