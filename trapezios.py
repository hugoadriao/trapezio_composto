#Criacao da funcao que funciona como f(x)
def func(x):
    from math import exp, sqrt, sin
    #f = 1/x
    #f = pow(x,4)
    #f = 1/(x+1)
    #f = sqrt(1+pow(x,2))
    #f = sin(x)
    f = exp(x)
    return f
#Criacao do algoritmo
def trapezio(a, b, n):
    h = (b-a)/n
    x = []
    #Definicao do primeiro ponto depois de a
    pm1 = a+h
    #Insere o primeiro ponto na lista geral
    x.append(pm1)
    #Insere o primeiro valor no somatorio
    soma_x = func(pm1)
    #Insere os valores na lista e calcula o somatorio dos valores na funcao
    for i in range(1, n-1, 1):
        x.append(x[i-1]+h)
        soma_x += func(x[i])
    #Formula
    result = (h/2)*(func(a)+(2*(soma_x))+func(b))
    #print('lista =', x)
    print('resultado =', result)
trapezio(0, 2, 1000)