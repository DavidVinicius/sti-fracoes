from util import verifica_resposta,denominador_comum
from flask import Flask, request, jsonify

from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)


@app.route("/resposta", methods=["POST"])
def resposta():
    if not request.method == "POST":
        return

    content = request.get_json()
    message, resultado = verifica_resposta(content['data'])
    r = {"message": message, "resultado": resultado}

    return jsonify(r)


# usar para os casos simples, soma de duas frações
# verifica se n1/d1 + n2/d2 = n1/d1

@app.route("/resposta_simples", methods=["POST"])
def resposta_simples():
    if not request.method == "POST":
        return
    content = request.get_json()
    
    n1,d1,n2,d2= content['n1'],content['d1'],content['n2'],content['d2']
    rn,rd = content['rn'],content['rd']
    param = [[n1,d1],[n2,d2],[rn,rd]]    
    message, resultado = verifica_resposta(param)
    r = {"message": message, "resultado": resultado}

    return jsonify(r)

# verifica se passo intermediario (fracoes com mesmo mmc) está certo
@app.route("/passo_intermediario", methods=["POST"])
def passo_intermediario():
    if not request.method == "POST":
        return
    content = request.get_json()
    
    n1,d1,n2,d2= content['n1'],content['d1'],content['n2'],content['d2']
    rn1,rd1,rn2,rd2= content['rn1'],content['rd1'],content['rn2'],content['rd2']
    
    [[c_n1, c_d1], [c_n2,c_d2]] =  denominador_comum([n1,d1],[n2,d2])

    message : str
    #inserir regras do passo intemediario aqui
    if ((rn1,rd1,rn2,rd2) == (c_n1, c_d1,c_n2,c_d2)):
        message = "correto"
    else:
        message = "errado"

    # TODO: pensar em uma forma de entregar a resposta do resultado (igual o /resposta)
    #resultado = ()

    # message, resultado = verifica_resposta(param)
    r = {"message": message}

    return jsonify(r)    


# SERVIÇO PARA GERAR OS EXERCÍCIOS
# POR ENQUANTO SÓ GERA 1/6 + 1/12

@app.route("/exercicio", methods=['GET','POST'])
def exercicio():
    r ={ 'n1' : 1,
         'd1' : 6,
         'n2' : 1,
         'd2' : 12
    }
    return jsonify(r)




@app.after_request
def creds(response):
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response


@app.route("/test", methods=["POST",'GET'])
def test():
    r = {"message": 1}

    resp = jsonify(r)

    return resp

app.run(host="0.0.0.0", port="5004")