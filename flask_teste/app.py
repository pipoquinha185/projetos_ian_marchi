from flask import Flask, request, jsonify
from flask_cors import CORS
from gerador_de_matricua import realizar_processo_matricula

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})


@app.route("/matricular", methods=["POST", "OPTIONS"])
def rota_matricular():
    if request.method == "OPTIONS":
        return jsonify({"status": "ok"}), 200
    dados = request.json

    resultado = realizar_processo_matricula(
        dados['nome'], dados['cpf'], dados['ano'], dados['curso']
        )
    return jsonify(resultado)

if __name__ == "__main__":
    app.run(debug=True, port=5000)