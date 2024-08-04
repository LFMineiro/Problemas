import math
import matplotlib.pyplot as plt

def calcular_erro(iteracoes):
    serie=0
    erros = [] 
    for n in range(iteracoes):
        an = ((-1) ** n)/(2*n+1)
        serie += an
        pi_aproximado = 4*serie
        erro = (math.pi - pi_aproximado)
        erros.append(erro)
    return erros
def main():
    n = int(input("Digite o número de iterações: "))
    erros = calcular_erro(n)
    plt.plot(range(n), erros)
    plt.show()

if __name__ == "__main__":
    main()
    

