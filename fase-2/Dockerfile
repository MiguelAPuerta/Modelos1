FROM python:3.10-slim

# Instalar compiladores y dependencias de sistema necesarias
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar scripts de entrenamiento y predicción
COPY train.py predict.py cleaning.py train.csv test.csv ./

# Instalar bibliotecas Python sin caché para reducir tamaño
RUN pip install --no-cache-dir numpy pandas scikit-learn loguru tqdm

# Nota: No se define CMD para permitir que el usuario ejecute manualmente
# el script deseado al correr el contenedor, por ejemplo:
#  docker run mi_imagen python train.py
