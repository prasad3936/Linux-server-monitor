M python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir Flask psutil

EXPOSE 5000

CMD ["python", "app.py"]


