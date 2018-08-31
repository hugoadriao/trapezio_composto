def func(x):
    from math import exp, sqrt, sin
    #f = 1/x
    #f = pow(x,4)
    #f = 1/(x+1)
    #f = sqrt(1+pow(x,2))
    #f = sin(x)
    f = exp(x)
    return f
def trapezio(a, b, n):
    h = (b-a)/n
    x = []
    pm1 = a+h
    x.append(pm1)
    soma_x = func(pm1)
    for i in range(1, n-1, 1):
        x.append(x[i-1]+h)
        soma_x += func(x[i])
    result = (h/2)*(func(a)+(2*(soma_x))+func(b))
    #print('lista =', x)
    print('resultado =', result)
trapezio(0, 2, 1000)