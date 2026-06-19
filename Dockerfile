# Basis-Image mit schlankem Python-Interpreter.
FROM python:3.12-slim

# Arbeitsverzeichnis im Container.
WORKDIR /app

# Benoetigte Data-Science-Libraries plus pytest installieren.
RUN pip install --no-cache-dir \
        numpy \
        pandas \
        matplotlib \
        seaborn \
        pytest

# Projektdateien ins Image kopieren.
COPY . /app

# Standardbefehl: alle Tests ausfuehren.
CMD ["pytest", "-v"]