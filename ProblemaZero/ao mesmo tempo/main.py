import matplotlib.pyplot as plt
import math

def calcular_arctg(x, iteracoes):
    serie = 0
    arctgs = []
    for n in range(iteracoes):
        an = ((-1) ** n) / (2 * n + 1) * x ** (2 * n + 1)
        serie += an
        arctgs.append(serie)
    return arctgs

def calcular_erro(pi_aprox):
    erros = []
    for pi_term in pi_aprox:
        erro_i = abs(math.pi - pi_term)
        erros.append(erro_i)
    return erros

def gregory(iteracoes):
    serie = 0
    pi_aprox = []
    for n in range(iteracoes):
        an = ((-1) ** n) / (2 * n + 1)
        serie += an
        pi_aprox.append(4 * serie)
    return pi_aprox

def machin(iteracoes):
    teta1 = calcular_arctg(1/5, iteracoes)
    teta2 = calcular_arctg(1/239, iteracoes)
    pi_aprox = []
    for i in range(iteracoes):
        pi_aprox_i = 4 * (4 * teta1[i] - teta2[i])
        pi_aprox.append(pi_aprox_i)
    return pi_aprox

def hutton(iteracoes):
    teta1 = calcular_arctg(1/2, iteracoes)
    teta2 = calcular_arctg(1/3, iteracoes)
    pi_aprox = []
    for i in range(iteracoes):
        pi_aprox_i = 4 * (teta1[i] + teta2[i])
        pi_aprox.append(pi_aprox_i)
    return pi_aprox

def clausen(iteracoes):
    teta1 = calcular_arctg(1/3, iteracoes)
    teta2 = calcular_arctg(1/7, iteracoes)
    pi_aprox = []
    for i in range(iteracoes):
        pi_aprox_i = 4 * (2 * teta1[i] + teta2[i])
        pi_aprox.append(pi_aprox_i)
    return pi_aprox

def dase(iteracoes):
    teta1 = calcular_arctg(1/2, iteracoes)
    teta2 = calcular_arctg(1/5, iteracoes)
    teta3 = calcular_arctg(1/8, iteracoes)
    pi_aprox = []
    for i in range(iteracoes):
        pi_aprox_i = 4 * (teta1[i] + teta2[i] + teta3[i])
        pi_aprox.append(pi_aprox_i)
    return pi_aprox

def main():
    n = int(input("Número de iterações: "))

    pi_gregory = gregory(n)
    pi_machin = machin(n)
    pi_hutton = hutton(n)
    pi_clausen = clausen(n)
    pi_dase = dase(n)

    erros_gregory = calcular_erro(pi_gregory)
    erros_machin = calcular_erro(pi_machin)
    erros_hutton = calcular_erro(pi_hutton)
    erros_clausen = calcular_erro(pi_clausen)
    erros_dase = calcular_erro(pi_dase)

    plt.plot(range(n), erros_gregory, label="Gregory", marker='o')
    plt.plot(range(n), erros_machin, label="Machin", marker='x')
    plt.plot(range(n), erros_hutton, label="Hutton", marker='s')
    plt.plot(range(n), erros_clausen, label="Clausen", marker='d')
    plt.plot(range(n), erros_dase, label="Dase", marker='*')
    plt.xlabel('Número de Iterações')
    plt.ylabel('Erro')
    plt.title('Erro na Aproximação de π usando Diferentes Fórmulas')
    plt.legend()
    plt.grid(True, which="both", linestyle='--', linewidth=0.5)
    plt.show()

if __name__ == "__main__":
    main()
