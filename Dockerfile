FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 3000

CMD [ "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "3000"]