FROM python:3.13-slim

WORKDIR /app

# Instalacja zależności systemowych (jeśli potrzebne)
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Kopiowanie i instalacja wymagań Pythona
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiowanie reszty kodu aplikacji
COPY . .

# Uruchomienie aplikacji na porcie dostarczonym przez Render
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]