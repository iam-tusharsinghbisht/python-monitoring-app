FROM python:3.11.3-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1

EXPOSE 5000

# CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
CMD ["python", "app.py"]