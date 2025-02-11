# 1. Basis-Image auswählen (Python 3.11 als Beispiel)
FROM python:latest

# 2. Arbeitsverzeichnis im Container setzen
WORKDIR /app

COPY . /app

# Aktualisiert pip vor der Installation der Pakete
RUN python -m pip install --upgrade pip

# 3. Abhängigkeiten kopieren und installieren (falls vorhanden)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get install tk -y

# 4. Skripte in den Container kopieren
COPY . .

# 5. Standardbefehl zum Starten des Skripts
CMD ["python", "main_app.py"]
