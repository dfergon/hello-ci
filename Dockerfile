FROM python:3.12-slim

WORKDIR /app

# Dependencias primero (aprovecha caché)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Código
COPY app/ app/

# Comando por defecto
CMD ["python", "-m", "app.saludar"]
