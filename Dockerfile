  # Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requisitos al contenedor
COPY requirements.txt requirements.txt

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt


# Copiar todo el contenido del proyecto al contenedor
COPY . .

# Reinstalar numpy para asegurar su instalación correcta
RUN pip install --no-cache-dir --force-reinstall numpy

# Exponer el puerto 5000 para acceder a la API
EXPOSE 5000

# Definir el comando por defecto para ejecutar la aplicación
CMD ["python", "app.py"]
