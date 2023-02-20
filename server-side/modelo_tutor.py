from enum import Enum
import random 
from util import *
from modelo_aluno import ModeloAluno
import util
from flask import Request, Response, jsonify

class PassosProblema(str,Enum):
    INICIO="INICIO"                 #Exercicio está na primeira etapa
    TODAS_ETAPAS="TODAS_ETAPAS"     #Errou conta direta, fazendo processo longo
    SIMPLIFICA="SIMPLIFICA"         #Faltou simplificar


niveis = ['facil','medio','dificil']


NIVEL_MAX = 2; #0,1,2 facil, medio, dificil, preparados
numAcertosParaPassar=2


# modelo tutor para gerar exercicios
def geraExercicio(requisicao : Request):
    modeloAluno = ModeloAluno()
    modeloAluno.atualizaModeloDeCookie(requisicao)

    response : Response    
    if (modeloAluno.nivelAtual==0):
        response = jsonify(geraFacil())
    elif (modeloAluno.nivelAtual==1):
        response = jsonify(geraMedio())
    elif (modeloAluno.nivelAtual==2):
        response = jsonify(gerarDificil())
    #elif (modeloAluno.nivelAtual==3):
    #    response = jsonify(geraPreparados())
    
    modeloAluno.gravaModeloEmCookie(response)
    
    return response

# dificil
# 
def geraFacil():
    x = [ (1,6,1,3),
        (1, 2, 1, 3),
            (1, 2, 2, 3),
            (1, 3, 1, 1),
            (1, 2, 1, 1) ,           
            (2, 3, 1, 2) ,           
            (1, 4, 1, 2),
            (1, 2, 1, 6)
        ]
    
    i = random.randint(0,len(x)-1)

    return { 'n1' : x[i][0],
            'd1' : x[i][1],
            'n2' : x[i][2],
            'd2' : x[i][3],
            'tipo': 'facil'
            }



def geraMedio():
    x = [ (2, 6, 1, 3),
            (1, 3, 1, 9),
            (2, 3, 2, 9),
            (3, 4, 1, 2) ,           
            (1, 20, 1, 5)
                        
        ]
    
    i = random.randint(0,len(x)-1)

    return { 'n1' : x[i][0],
            'd1' : x[i][1],
            'n2' : x[i][2],
            'd2' : x[i][3],
            'tipo': 'medio'
            }


# def gerarDificil():
#     d1 = random.randint(7,10)
#     n1 = random.randint(1,d1)
    
#     d2 = random.randint(7,d1-1)
#     n2 = random.randint(1,d2)
    
#     if(d1==d2):
#         d2+=1

#     while not is_simplifica(n1,d1):
#         d1 = random.randint(8,11)
#         n1 = random.randint(1,d1)
#     while not is_simplifica(n2,d2):
#         d2 = random.randint(7,d1-1)
#         if(d1==d2):
#             d2+=1
#         n2 = random.randint(1,d2)
    
#     return { 'n1' : n1,
#             'd1' : d1,
#             'n2' : n2,
#             'd2' : d2,
#             'tipo': 'dificil'
#             }

def gerarDificil():
    x = [ (5, 12, 1, 16),
            (8, 15, 1, 10),
            (1, 8, 11, 16),
            (3, 10, 1, 14),
            (7, 16, 1, 14),
            (9, 14, 5, 21),
            (7, 12, 17, 18),
            (1, 14, 7, 12),
            (9, 10, 13, 16),
            (1, 14, 11, 16),
            (2, 9, 7, 12),
            (3, 10, 1, 15),
            (3, 14, 9, 49),
            (4, 36, 6, 24),
            (7, 20, 3, 16),
            (7, 8, 9, 12),
        ]
    
    i = random.randint(0,len(x)-1)
    #return x[i]
    return { 'n1' : x[i][0],
            'd1' : x[i][1],
            'n2' : x[i][2],
            'd2' : x[i][3],
            'tipo': 'preparado'
            }


def intervencaoTutorialResposta(n1,d1,n2,d2,#pergunta
                                rn,rd,#resposta
                                msg_corretude,#'correto' ou 'errado'
                                simplificado: bool,#True False
                                passo:str, #PassosProblema,
                                modeloAluno: ModeloAluno
                                )-> str: # retorna  mensagem de intervencao
    corretude = msg_corretude == 'correto'


    if not corretude:        
        modeloAluno.acertoSequenciais=0
    if not corretude and passo == PassosProblema.INICIO:
        return "Tente primeiro encontrar o MMC"


    
    if simplificado and corretude:# acertou
        modeloAluno.contadorAcertos+=1
        modeloAluno.acertoSequenciais+=1
        modeloAluno.contadorPulos=0 
        if modeloAluno.contadorAcertos>=numAcertosParaPassar:
            modeloAluno.nivelAtual= (modeloAluno.nivelAtual+1) if modeloAluno.nivelAtual < NIVEL_MAX else modeloAluno.nivelAtual
            modeloAluno.contadorAcertos = 0
        return "Parabéns, Você está indo bem"
    
    if corretude and not simplificado:
        return "Está correto, mas você ainda precisa simplificar"
    if (int(n1)+int(n2)==int(rn) and int(d1)+int(d2)==int(rd)):
        return "Para somar uma fração, use o MMC"

    if (util.mmc(d1,d2)*2 == rd):
        return "Para somar uma fração, some os valores do numerador e mantenha o valor do denominador."        

    if not corretude:        
        return "Você errou"



def intervencaoTutorialPassoIntermediario(n1,d1,n2,d2,#pergunta
                                        rn1,rd1,rn2,rd2,#resposta
                                        msg_corretude: str,#'correto' ou 'errado'
                                        modeloAluno:ModeloAluno
                                        ) -> str: # retorna  mensagem de intervencao
    corretude = msg_corretude == 'correto'
    if not corretude:
        modeloAluno.acertoSequenciais=0    
        modeloAluno.errosSeguidosMMC+=1
    else:
        modeloAluno.acertoSequenciais+=1
        modeloAluno.errosSeguidosMMC=0
    

    if modeloAluno.errosSeguidosMMC == 3:
        mmc = util.mmc(d1,d2)
        return f"O MMC entre {d1} e {d2} é {int(mmc)}"

    if modeloAluno.errosSeguidosMMC == 3:
        mmc = util.mmc(d1,d2)
        return f"O MMC entre {d1} e {d2} é {int(mmc)}"

    if not corretude:
        return "Você não acertou esse passo"
    
    
    #return "Mensagem tutorial"
    
def inhtervencaoPularExercicio(modeloAluno:ModeloAluno
                                    ) -> str: # retorna  mensagem de intervencao
    modeloAluno.contadorPulos+=1
    modeloAluno.acertoSequenciais=0
    if(modeloAluno.contadorPulos>=2 and modeloAluno.nivelAtual>0):
        modeloAluno.nivelAtual-=1
        modeloAluno.contadorPulos=0

    return "OK"