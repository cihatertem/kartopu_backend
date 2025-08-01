FROM python:3.13-slim

LABEL maintainer="Cihat Ertem <cihatertem@gmail.com>"

ENV PYTHONUNBUFFERED=1

RUN groupadd -g 1000 -r app && useradd -u 1000 --no-log-init -r -g app app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt clean -y \
    && apt autopurge -y

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R app:app /app

USER app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
