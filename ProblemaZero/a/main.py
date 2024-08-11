import math
import matplotlib.pyplot as plt

def calcular_erro(iteracoes):
    serie=0
    erros = [] 
    for n in range(iteracoes):
        an = ((-1) ** n)/(2*n+1)* (math.sqrt(3)/3) ** (2 * n + 1)
        serie += an
        pi_aproximado = 6*serie
        erro = abs(math.pi - pi_aproximado)
        erros.append(erro)
    return erros
def main():
    n = int(input("Digite o número de iterações: "))
    erros = calcular_erro(n)

    for i in range(n):
        print(f"Iteração {i + 1}: pi aproximado = {pi_aproximado[i]}, erro = {erros[i]}")

    plt.plot(range(n), erros)
    plt.grid(True, which='both')
    plt.show()
    

if __name__ == "__main__":
    main()
    

