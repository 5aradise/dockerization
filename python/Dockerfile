FROM python:3.13.3-bullseye

WORKDIR /app

COPY . .

RUN python -m venv ./.venv

RUN . ./.venv/bin/activate && \
    pip install -r requirements.txt

EXPOSE 8080

CMD [".venv/bin/uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]