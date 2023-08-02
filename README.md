# Reconocimiento de Entidades Nombradas en Español (NER-API)
NER-API es una API en Flask que identifica y clasifica entidades nombradas dentro de oraciones en español. Utiliza la tecnología de procesamiento de lenguaje natural (PLN) a través de la biblioteca SpaCy y se puede ejecutar fácilmente en un contenedor Docker.
## Características :star2:
- **Identificación de Entidades**: Detecta y clasifica entidades en oraciones en español.
- **Microservicio Flask**: Desplegado como un microservicio fácilmente escalable.
- **Contenedor Docker**: Empaquetado para ejecución sencilla con Docker.
## Instrucciones de Uso :rocket:
### Sin Docker :desktop_computer:
Si prefieres no usar Docker, puedes instalar las dependencias en un entorno virtual y ejecutar la aplicación localmente. Se utilizó python 3.8 para su creación, adicional consultar el archivo `requirements.txt` para las dependencias requeridas.
1. Instalar las Dependencias:
```bash
pip install -r requirements.txt
```
Ejecutar la Aplicación:
```bash
python app.py
```
La aplicación estará disponible en http://localhost:5000/ner. Puedes utilizar un cliente HTTP como curl o Postman para enviar peticiones POST.

### Usando Docker :whale:
1. **Construir la Imagen Docker**:
   ```bash
   docker build -t ner-api .
   ```
2. **Ejecutar la Imagen**:
   ```bash
   docker run -p 5000:5000 ner-api
   ```
La API estará disponible en `http://localhost:5000/ner`. Puedes utilizar un cliente HTTP como `curl` o Postman para enviar peticiones POST.
## Ejemplo de Petición :mailbox_with_mail:
Puedes probar la API con la siguiente petición:
```json
{
  "oraciones": [
    "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
    "San Francisco considera prohibir los robots de entrega en la acera."
  ]
}
```
## Contribuir :handshake:
Si tienes ideas para mejorar la API o encuentras algún error, no dudes en abrir un Issue o hacer un Pull Request.
