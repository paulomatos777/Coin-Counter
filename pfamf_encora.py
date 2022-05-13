def quartes(n):
    cont = 0
    while n >= 25:
        n = n - 25
        cont = cont + 1
    return [cont, n]

def dimes(n):
    cont = 0
    while n >= 10:
        n = n - 10
        cont = cont + 1
    return [cont, n]

def nickels(n):
    cont = 0
    while n >= 5:
        n = n - 5
        cont = cont + 1
    return [cont, n]
def pennies(n):
    cont = 0
    while n >= 1:
        n = n - 1
        cont = cont + 1
    return [cont, n]

def func_0(n):
    w = pennies(n)
    return [0,0,0,w[0]]

def func_1(n):
    z = nickels(n)
    w = pennies(z[1])
    return [0,0,z[0],w[0]]

def func_2(n):
    y = dimes(n)
    z = nickels(y[1])
    w = pennies(z[1])
    return [0,y[0],z[0],w[0]]

def func_3(n):
    x = quartes(n)
    y = dimes(x[1])
    z = nickels(y[1])
    w = pennies(z[1])
    return [x[0],y[0],z[0],w[0]]

def makeChange(n):
    x = func_0(n)
    y = func_1(n)
    z = func_2(n)
    w = func_3(n)
    return [x,y,z,w]

n = int(input("Digite um número: "))
print(makeChange(n))