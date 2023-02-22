from modulo_especialista import verifica_resposta,denominador_comum
from flask import Flask, request, jsonify

from flask_cors import CORS
from modulo_tutor import geraExercicio,PassosProblema, inhtervencaoPularExercicio, intervencaoTutorialPassoIntermediario, intervencaoTutorialResposta
from modelo_aluno import ModeloAluno


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
    message, resultado = verifica_resposta(param) #verifica_resposta no util (modelo dominio)
    
    passo = content['passo']
    simplificado = [rn,rd]==resultado

    #Carrega modelo do aluno do cookie
    modeloAluno = ModeloAluno()
    modeloAluno.atualizaModeloDeCookie(request)

    #realiza intervencao
    msgIterv = intervencaoTutorialResposta(n1,d1,n2,d2,rn,rd,message,simplificado,passo,modeloAluno)
    

    r = {"message": message, "resultado": resultado, "msgTutoria": msgIterv}
    response = jsonify(r)

    #regrava modelo do aluno em cookie
    modeloAluno.gravaModeloEmCookie(response)
    
        
    return response

# verifica se passo intermediario (fracoes com mesmo mmc) está certo
@app.route("/pularExercicio", methods=["POST","GET"])
def pularExercicio():
    # content = request.get_json()
     #Carrega modelo do aluno do cookie
    modeloAluno = ModeloAluno()
    modeloAluno.atualizaModeloDeCookie(request)

    #realiza intervencao
    msgIterv = inhtervencaoPularExercicio(modeloAluno)

    r = {"msgTutoria": msgIterv}
    response = jsonify(r)    
    #regrava modelo do aluno em cookie
    modeloAluno.gravaModeloEmCookie(response)

    return response

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
    
    if ((rn1,rd1,rn2,rd2) == (c_n1, c_d1,c_n2,c_d2)):
        message = "correto"
    else:
        message = "errado"

    #Carrega modelo do aluno do cookie
    modeloAluno = ModeloAluno()
    modeloAluno.atualizaModeloDeCookie(request)

    #realiza intervencao
    msgIterv = intervencaoTutorialPassoIntermediario(n1,d1,n2,d2,rn1,rd1,rn2,rd2,message,modeloAluno)
  

        
    r = {"message": message, "msgTutoria": msgIterv}
    response = jsonify(r)    
    #regrava modelo do aluno em cookie
    modeloAluno.gravaModeloEmCookie(response)

    return response




@app.route("/exercicio", methods=['GET','POST'])
def exercicio():
    resp =   geraExercicio(request)
    return resp

# metodo de gerar exercicio inicial, excluir depois de validado o novo
# SERVIÇO PARA GERAR OS EXERCÍCIOS
# POR ENQUANTO SÓ GERA 1/6 + 1/12
def geraExercicioDummy():
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

#app.run(host="0.0.0.0", port="5004")
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_SECURE'] = True
app.run(host="localhost", port="5004")