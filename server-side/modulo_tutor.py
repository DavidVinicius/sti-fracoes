from enum import Enum
from modulo_especialista import *
from modelo_aluno import ModeloAluno
import modulo_especialista as esp
from flask import Request, Response, jsonify

class PassosProblema(str,Enum):
    INICIO="INICIO"                 #Exercicio está na primeira etapa
    TODAS_ETAPAS="TODAS_ETAPAS"     #Errou conta direta, fazendo processo longo
    SIMPLIFICA="SIMPLIFICA"         #Faltou simplificar


#niveis = ['facil','medio','dificil']


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

    if (esp.mmc(d1,d2)*2 == rd):
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
        mmc = esp.mmc(d1,d2)
        return f"O MMC entre {d1} e {d2} é {int(mmc)}"

    if modeloAluno.errosSeguidosMMC == 3:
        mmc = esp.mmc(d1,d2)
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