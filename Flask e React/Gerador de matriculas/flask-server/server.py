from flask import Flask, request, jsonify

app = Flask(__name__)

cursos_disponiveis = [
    {"nome": "Engenharia da computação", "codigo": 2345, "vagas_max": 40, "vagas_preenchidas": 0},
    {"nome": "Psicologia", "codigo": 8931, "vagas_max": 5, "vagas_preenchidas": 5},
    {"nome": "Medicina", "codigo": 1992, "vagas_max": 16, "vagas_preenchidas": 16},
    {"nome": "Odontologia", "codigo": 6769, "vagas_max": 32, "vagas_preenchidas": 16},
    {"nome": "Desing Grafico", "codigo": 2223, "vagas_max": 15, "vagas_preenchidas": 10},
]

@app.route("/matricular", methods=['POST'])
def matricular():
    dados = request.json

    nome = dados.get('nome')
    cpf = dados.get('cpf')
    ano_nascimento = dados.get('ano')
    curso_nome = dados.get('curso').lower()

    curso_encontrado = next((c for c in cursos_disponiveis if c['nome'].lower() == curso_nome), None)

    informacoes_colocadas = None

    if nome!='' and cpf != '' and ano_nascimento !='' and curso_nome !='':
        informacoes_colocadas = True
    

    if informacoes_colocadas == True:
        if not curso_encontrado:
            return jsonify({"erro": "Curso não encontrado"}), 404
        
        if curso_encontrado['vagas_preenchidas'] < curso_encontrado['vagas_max']:
            curso_encontrado['vagas_preenchidas'] += 1

            matricula = f"{curso_encontrado['codigo']}{ano_nascimento[-2:]}{cpf[-2:]}"

            return jsonify({
                "status": "sucesso",
                "matricula": matricula,
                "nome": nome
            })

        else:
            return jsonify({"erro": "Sem vagas"}), 400
    else:
        return jsonify({"erro": "Coloque as infomações"})

    
if  __name__ == "__main__":
    app.run(debug=True)