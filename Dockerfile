# Imagen base con Python
FROM python:3.10-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos del proyecto
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar y preparar el script de arranque
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Variables de entorno para Flask
ENV FLASK_APP=app:create_app
ENV FLASK_RUN_PORT=5000

# Exponer el puerto
EXPOSE 5000

# Comando de arranque
CMD ["/entrypoint.sh"]

