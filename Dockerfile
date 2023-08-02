# Usar una imagen base con Python 3.8
FROM python:3.8-slim
# Establecer un directorio de trabajo
WORKDIR /app
# Copiar el archivo de requerimientos y el código fuente
COPY requirements.txt ./
COPY app.py ./
# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt
# Descargar el modelo español de SpaCy
RUN python -m spacy download es_core_news_sm
# Exponer el puerto donde se ejecutará la aplicación
EXPOSE 5000
# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
