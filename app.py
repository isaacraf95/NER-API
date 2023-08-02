from flask import Flask, request, jsonify
import spacy

# Carga el modelo en español para el reconocimiento de entidades nombradas
nlp = spacy.load("es_core_news_sm")

# Crea una instancia de Flask
app = Flask(__name__)


# Define una ruta para la API que acepta peticiones POST a traves de un JSON.
@app.route("/ner", methods=["POST"])
def get_entities():
    # Se obtiene el JSON enviado en la peticion
    data = request.get_json()
    # Extrae la lista de oraciones a pasar por el modelo NER
    sentences = data["oraciones"]
    # Creación de objeto para almacenar el resultado
    result = {"resultado": []}

    # Iteracion en cada una de las oraciones
    for sentence in sentences:
        # Procesa la oracion con el modelo para la identificacion de entidades
        doc = nlp(sentence)
        entities = {}
        # Iteracion en cada una de las entidades identificadas
        for ent in doc.ents:
            entities[ent.text] = ent.label_
        # Se añade la oracion y entidades identificadas a la respuesta
        result["resultado"].append({
            "oracion": sentence,
            "entidades": entities
        })
    # Se devuelve el resultado como un JSON
    return jsonify(result)

# Inicio de aplicación si se ejecuta directamente
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
