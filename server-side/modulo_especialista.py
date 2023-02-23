from fractions import Fraction
import random 
# modelo do dominio

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
