

from enum import Enum
from flask import Request, Response

# class syntax
class CookieAluno(str,Enum):
    NIVEL_ATUAL= 'nivel_atual'
    ACERTO_SEQUENCIAIS= 'acerto_sequenciais'
    CONTADOR_ACERTOS= 'contador_acertos'
    CONTADOR_PULOS= 'contador_pulos',
    ERROS_SEGUIDOS_MMC =  'erros_mmc_seguidos'

class ModeloAluno:
    def __init__(self):
        self.nivelAtual = 0
        self.acertoSequenciais = 0
        self.contadorAcertos = 0
        self.contadorPulos = 0
        self.errosSeguidosMMC = 0

    def gravaModeloEmCookie(self,resp: Response):        
        resp.set_cookie(CookieAluno.NIVEL_ATUAL, str(self.nivelAtual))
        resp.set_cookie(CookieAluno.ACERTO_SEQUENCIAIS, str(self.acertoSequenciais))
        resp.set_cookie(CookieAluno.CONTADOR_ACERTOS, str(self.contadorAcertos))
        resp.set_cookie(CookieAluno.CONTADOR_PULOS, str(self.contadorPulos))
        resp.set_cookie(CookieAluno.ERROS_SEGUIDOS_MMC, str(self.errosSeguidosMMC))

    def atualizaModeloDeCookie(self, request: Request):
        self.nivelAtual = int(request.cookies.get(CookieAluno.NIVEL_ATUAL)) if request.cookies.get(CookieAluno.NIVEL_ATUAL) is not None else 0
        self.acertoSequenciais = int(request.cookies.get(CookieAluno.ACERTO_SEQUENCIAIS)) if request.cookies.get(CookieAluno.ACERTO_SEQUENCIAIS) is not None else 0
        self.contadorAcertos = int(request.cookies.get(CookieAluno.CONTADOR_ACERTOS)) if request.cookies.get(CookieAluno.CONTADOR_ACERTOS) is not None else 0
        self.contadorPulos = int(request.cookies.get(CookieAluno.CONTADOR_PULOS)) if request.cookies.get(CookieAluno.CONTADOR_PULOS) is not None else 0
        self.errosSeguidosMMC = int(request.cookies.get(CookieAluno.ERROS_SEGUIDOS_MMC)) if request.cookies.get(CookieAluno.ERROS_SEGUIDOS_MMC) is not None else 0
        
        