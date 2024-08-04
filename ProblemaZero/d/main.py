import matplotlib.pyplot as plt
import math

def calcular_arctg(x, iteracoes):
    serie=0
    arctgs = []
    for n in range(iteracoes):
        an = ((-1) ** n)/(2*n+1) * x ** (2*n + 1)
        serie += an
        arctgs.append(serie)
    return arctgs
def calcular_piaprox(teta1, teta2):
    pi_aprox= []
    for  i in range(len(teta1)):
        pi_aprox_i= 4*(2*teta1[i] + teta2[i])
        pi_aprox.append(pi_aprox_i)
    return pi_aprox
def calcular_erro(iteracoes, pi_aprox):
    erros=[]
    for i in range(iteracoes):
        erro_i = math.pi - pi_aprox[i]
        erros.append(erro_i)
    return erros
    
def main(): 
    n = int(input("Número de iterações: "))
    teta1 = calcular_arctg(1/3, n)
    teta2 = calcular_arctg(1/7, n)
    pi_aproximado=calcular_piaprox(teta1, teta2)
    erros = calcular_erro(n, pi_aproximado)
    plt.plot(range(n), erros)
    plt.show()

if __name__ == "__main__":
    main()


