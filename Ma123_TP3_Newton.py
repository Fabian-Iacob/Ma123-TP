#--*-- coding:utf8 --*--
#-------------------------------------------------------------------------------
# Nom           : IACOB
# Prénom        : Fabian
# Classe        : 1PV
# Groupe        : V1

# TP n°         : 3
#-------------------------------------------------------------------------------

from math import sin, cos, exp, log, pi, tan

def Newton(f,fder,x0,epsilon,Nitermax):
    xold = x0
    xnew = xold-f(xold)/fder(xold)
    n = 1
    while abs(xnew-xold)>epsilon and n<Nitermax:
        xold = xnew
        xnew = xold-f(xold)/fder(xold)
        n = n+1
    return xnew,n


def f1(x):
    return x**4+3*x-9

def fder1(x):
    return 4*x**3+3

print('f1, sol 1 : (alpha, itérations) ->',Newton(f1,fder1,3/2,1e-10,5e4))      #Solution positive
print('f1, sol 2 : (alpha, itérations) ->',Newton(f1,fder1,-2,1e-10,5e4))       #Solution négatie

def f2(x):
    return 3*cos(x)-2-x

def fder2(x):
    return -3*sin(x)-1

print('f2, sol 1 : (alpha, itérations) ->',Newton(f2,fder2,0.4,1e-10,5e4))      #Solution positive
print('f2, sol 2 : (alpha, itérations) ->',Newton(f2,fder2,-3/2,1e-10,5e4))     #Solution négatie 1
print('f2, sol 3 : (alpha, itérations) ->',Newton(f2,fder2,-3.5,1e-10,5e4))     #Solution négatie 2

def f3(x):
    return x*exp(x)-7

def fder3(x):
    return (1+x)*exp(x)

print('f3, unique sol : (alpha, itérations) ->',Newton(f3,fder3,3/2,1e-10,5e4))     #Solution

def f4(x):
    return exp(x)-x-10

def fder4(x):
    return exp(x)-1

print('f4, sol 1 : (alpha, itérations) ->',Newton(f4,fder4,2,1e-10,5e4))            #Solution 1
print('f4, sol 2 : (alpha, itérations) ->',Newton(f4,fder4,-10.5,1e-10,5e4))        #Solution 2

def f5(x):
    return 2*tan(x)-x-5

def fder5(x):
    return 2*(tan(x))**2+1

print('f5, unique sol : (alpha, itérations) ->',Newton(f5,fder5,1.2,1e-10,5e4))     #Solution

def f6(x):
    return exp(x)-x**2-3

def fder6(x):
    return exp(x)-2*x

print('f6, unique sol : (alpha, itérations) ->',Newton(f6,fder6,1.2,1e-10,5e4))     #Solution

def f7(x):
    return 3*x+4*log(x)-7

def fder7(x):
    return (3*x+4)/x

print('f7, unique sol : (alpha, itérations) ->',Newton(f7,fder7,3/2,1e-10,5e4))     #Solution

def f8(x):
    return x**4-2*x**2+4*x-17

def fder8(x):
    return 4*x**3-4*x+4

print('f8, sol 1 : (alpha, itérations) ->',Newton(f8,fder8,3/2,1e-10,5e4))          #Solution positive
print('f8, sol 2 : (alpha, itérations) ->',Newton(f8,fder8,-2.8,1e-10,5e4))         #Solution négative

def f9(x):
    return exp(x)-2*sin(x)-7

def fder9(x):
    return exp(x)-2*cos(x)

print('f9, unique sol : (alpha, itérations) ->',Newton(f9,fder9,pi/2,1e-10,5e4))    #Solution

def f10(x):
    return log(x**2+4)*exp(x)-10

def fder10(x):
    return (2*x*exp(x))/(x**2+4)+log(x**2+4)*exp(x)

print('f10, unique sol : (alpha, itérations) ->',Newton(f10,fder10,3/2,1e-10,5e4))  #Solution
