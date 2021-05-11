#-------------------------------------------------------------------------------
# Nom           : IACOB
# Prénom        : Fabian
# Classe        : 1PV
# Groupe        : 1

# TP n°         : 4
#-------------------------------------------------------------------------------
from math import sin, cos, exp, log, acos, atan, pi, tan
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import semilogy

""" MÉTHODES """
def PointFixe(g,x0,epsilon,Nitermax,alpha):
    xold = x0
    xnew = g(xold)
    n = 1
    l_n = [n]
    l_xn = [xnew]
    l_en = [abs(xnew-alpha)]
    while abs(xnew-xold)>epsilon and n<Nitermax:
        xold = xnew
        xnew = g(xold)
        n = n+1
        l_n.append(n)
        l_xn.append(xnew)
        l_en.append(abs(xnew-alpha))
    return l_n,l_xn,l_en

def Newton(f,fder,x0,epsilon,Nitermax,alpha):
    xold = x0
    xnew = xold-f(xold)/fder(xold)
    n = 1
    l_n = [n]
    l_xn = [xnew]
    l_en = [abs(xnew-alpha)]
    while abs(xnew-xold)>epsilon and n<Nitermax:
        xold = xnew
        xnew = xold-f(xold)/fder(xold)
        n = n+1
        l_n.append(n)
        l_xn.append(xnew)
        l_en.append(abs(xnew-alpha))
    return l_n,l_xn,l_en

def Dichotomie(f,a0,b0,epsilon,Nitermax,alpha):
    an=a0
    bn=b0
    n=0
    l_n = []
    l_xn = []
    l_en = []
    while abs(bn-an)>epsilon and n<Nitermax:
        m=(an+bn)/2
        if f(an)*f(m)<0:
            bn=m
        else:
            an=m
        n=n+1
        l_n.append(n)
        l_xn.append(m)
        l_en.append(abs(m-alpha))
    return l_n,l_xn,l_en

def Secante(f,x0,x1,epsilon,Nitermax,alpha):
    xn = x0
    xn1 = x1
    xn2 = (xn*f(xn1)-xn1*f(xn))/(f(xn1)-f(xn))
    n = 1
    l_n = [n]
    l_xn = [xn2]
    l_en = [abs(xn2-alpha)]
    while abs(xn1-xn)>epsilon and n<Nitermax:
        xn = xn1
        xn1 = xn2
        xn2 = (xn*f(xn1)-xn1*f(xn))/(f(xn1)-f(xn))
        n = n+1
        l_n.append(n)
        l_xn.append(xn2)
        l_en.append(abs(xn2-alpha))
    return l_n,l_xn,l_en

""" FONCTIONS """
def f0(x):
    return 2*x-(1+sin(x))
def fder0(x):
    return 2-cos(x)
def g0(x):
    return (1+sin(x))/2


def f1(x):
    return x**4+3*x-9
def fder1(x):
    return 4*x**3+3
def g1_plus(x):
    return (9-3*x)**(1/4)
def g1_moins(x):
    return -(9-3*x)**(1/4)


def f2(x):
    return 3*cos(x)-2-x
def fder2(x):
    return -3*sin(x)-1
def g2_plus(x):
    return acos((x+2)/3)
def g2_moins(x):
    return -acos((x+2)/3)
def g2(x):
    return 3*cos(x)-2

def f3(x):
    return x*exp(x)-7
def fder3(x):
    return (1+x)*exp(x)
def g3(x):
    return log(7/x)


def f4(x):
    return exp(x)-x-10
def fder4(x):
    return exp(x)-1
def g4_1(x):
    return log(x+10)
def g4_2(x):
    return exp(x)-10


def f5(x):
    return 2*tan(x)-x-5
def fder5(x):
    return 2*(tan(x))**2+1
def g5(x):
    return atan((x+5)/2)


def f6(x):
    return exp(x)-x**2-3
def fder6(x):
    return exp(x)-2*x
def g6(x):
    return log(x**2+3)


def f7(x):
    return 3*x+4*log(x)-7
def fder7(x):
    return (3*x+4)/x
def g7(x):
    return (7-4*log(x))/3


def f8(x):
    return x**4-2*x**2+4*x-17
def fder8(x):
    return 4*x**3-4*x+4
def g8_plus(x):
    return (2*x**2-4*x+17)**(1/4)
def g8_moins(x):
    return -(2*x**2-4*x+17)**(1/4)


def f9(x):
    return exp(x)-2*sin(x)-7
def fder9(x):
    return exp(x)-2*cos(x)
def g9(x):
    return log(7+2*sin(x))


def f10(x):
    return log(x**2+4)*exp(x)-10
def fder10(x):
    return (2*x*exp(x))/(x**2+4)+log(x**2+4)*exp(x)
def g10(x):
    return log(10/log(x**2+4))


""" AFFICHAGE SOLUTIONS """
def graphe(f,fder,g,x0,x1,epsilon,Nitermax,alpha):
    l_n,l_xn,l_en = PointFixe(g,x0,epsilon,Nitermax,alpha)
    l_n2,l_xn2,l_en2 = Newton(f,fder,x0,epsilon,Nitermax,alpha)
    if x0<x1:
        l_n3,l_xn3,l_en3 = Dichotomie(f,x0,x1,epsilon,Nitermax,alpha)
        l_n4,l_xn4,l_en4 = Secante(f,x0,x1,epsilon,Nitermax,alpha)
    else:
        l_n3,l_xn3,l_en3 = Dichotomie(f,x1,x0,epsilon,Nitermax,alpha)
        l_n4,l_xn4,l_en4 = Secante(f,x1,x0,epsilon,Nitermax,alpha)

    print('Point Fixe :'.ljust(13),'α =',repr(l_xn[-1]).ljust(19),'n =',repr(l_n[-1]).ljust(4))
    print('Newton :'.ljust(13),'α =',repr(l_xn2[-1]).ljust(19),'n =',repr(l_n2[-1]).ljust(4))
    print('Dichotomie :'.ljust(13),'α =',repr(l_xn3[-1]).ljust(19),'n =',repr(l_n3[-1]).ljust(4))
    print('Sécante :'.ljust(13),'α =',repr(l_xn4[-1]).ljust(19),'n =',repr(l_n4[-1]).ljust(4))
    print('••••••••••••••••••••••••••••••••••••••••••••')

    fig, ax = plt.subplots()
    if l_n[-1]<5000:
        ax.semilogy(l_n, l_en, "r", linewidth=1, label='Point Fixe')
    ax.semilogy(l_n2, l_en2, "g", linewidth=1, label='Newton')
    ax.semilogy(l_n3, l_en3, "y", linewidth=1, label='Dichotomie')
    ax.semilogy(l_n4, l_en4,  linewidth=1, label='Sécante')

    ax.set(xlabel='itérations', ylabel='en',title='Erreur en fonction des itérations')
    ax.grid()

    plt.legend()
    plt.show()


#graphe(f0,fder0,g0,0,1,1e-10,5e4,0.8878622115)                 #Solution


#graphe(f1,fder1,g1_plus,3/2,1,1e-10,5e4,1.4649177089)          #Solution positive
#graphe(f1,fder1,g1_moins,-2,-1,1e-10,5e4,-1.9644857395)        #Solution négative

#graphe(f2,fder2,g2_plus,0.4,1,1e-10,5e4,0.5529448215)          #Solution positive
#graphe(f2,fder2,g2_moins,-1.5,-0.5,1e-10,5e4,-1.3536404317)    #Solution négative 1
#graphe(f2,fder2,g2,-3.5,-4.5,1e-10,5e4,-3.9880104453)          #Solution négative 2

#graphe(f3,fder3,g3,1.5,2,1e-10,5e4,1.5243452049)               #Solution

#graphe(f4,fder4,g4_1,2,3,1e-10,5e4,2.5279632019)               #Solution 1
#graphe(f4,fder4,g4_2,-10.5,-9.5,1e-10,5e4,-9.9999545980)       #Solution 2

#graphe(f5,fder5,g5,1.2,1.5,1e-10,5e4,1.2616327441)             #Solution

#graphe(f6,fder6,g6,1.2,2,1e-10,5e4,1.8731225477)               #Solution

#graphe(f7,fder7,g7,1.5,2,1e-10,5e4,1.6586562691)               #Solution

#graphe(f8,fder8,g8_plus,1.5,2.5,1e-10,5e4,2.0347532635)        #Solution positive
#graphe(f8,fder8,g8_moins,-2.8,-2.5,1e-10,5e4,-2.5089616851)    #Solution négative

#graphe(f9,fder9,g9,pi/2,3,1e-10,5e4,2.1591439313)              #Solution

#graphe(f10,fder10,g10,1.5,2,1e-10,5e4,1.6562517244)        #Solution

