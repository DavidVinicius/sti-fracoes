from util import verifica_resposta
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/resposta", methods=["POST"])
def resposta():
    if not request.method == "POST":
        return

    content = request.get_json()
    message, resultado = verifica_resposta(content['data'])
    r = {"message": message, "resultado": resultado}

    return jsonify(r)
    
app.run(host="0.0.0.0", port="5004")