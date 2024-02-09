FROM python:3.8.16-slim-bullseye


RUN mkdir /app
WORKDIR /app
COPY main.py requirements.txt model_best_9986.pkl ./

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t fastapi-sensor .
# docker run -d -p 8000:8000 --name fastapi-sensor fastapi-sensor