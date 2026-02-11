# Imagen base de Python
FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la app
COPY . .

# Puerto que Cloud Run espera
EXPOSE 8080

# Comando para ejecutar la app
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
