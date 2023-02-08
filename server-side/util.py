from fractions import Fraction

def verifica_resposta(dados):
    #recebe ultimo item da lista como resposta do usuario
    resposta = Fraction(dados[-1][0], dados[-1][1])

    #inicia com o primeiro termo da soma
    total = Fraction(dados[0][0], dados[0][1])

    #soma demais termos
    for frac in dados[1:-1]:
        total += Fraction(frac[0], frac[1])

    #retorna mensagem se resposta do usuario esta correta
    #retorna soma realizada pelo algoritmo, simplificada
    if resposta == total:
        return 'correto', [total._numerator, total._denominator]
    else:
        return 'errado', [total._numerator, total._denominator]
