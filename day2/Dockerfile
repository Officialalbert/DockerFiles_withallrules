FROM python:3.14.3-slim

RUN apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/lists/*).

RUN adduser --disabled-password --gecos '' appuser
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER appuser

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost/ || exit 1

CMD ["python", "app.py"]
