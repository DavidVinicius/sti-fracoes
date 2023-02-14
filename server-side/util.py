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


# retorna maior divisor comum
def mdc(a,b):
    menor = 1    
    if (a<b):
        menor = a
    else:
        menor = b
    for i in range(menor,1,-1):
        if (a%i==0 and b%i==0):
            return i
    return 1

# simplifica a fracao:
# retorna  a fração n/d como [n,d] se já estiver simplificado
# retorna a fração simplificada n'/d' como [n',d'] caso contrário
def simplifica(n,d):
    dividir = mdc(n,d)
    return [int(n/dividir),int(d/dividir)]


#verifica se a lista está simplificada
def is_simplifica(n,d):
    [ns,ds] = simplifica(n,d)
    return [ns,ds] == [n,d]


#calcula mmc entre dois números
def mmc(a,b):
    maior_div = mdc(a,b)
    return a*b/maior_div

#retorna duas fracoes no denominador comum
# f1: [n, d] lista representando fração. n: numerador; d: denominador
# f2: [n, d] lista representando fração. n: numerador; d: denominador
# ex: [1, 3], [3, 4] -> [4,12], [9,12]
def denominador_comum(f1,f2):
    denominador = mmc(f1[-1],f2[-1])
    num1 = f1[0] * (denominador/f1[-1])
    num2 = f2[0] * (denominador/f2[-1])    
    return [[num1,denominador], [num2,denominador]]


        

