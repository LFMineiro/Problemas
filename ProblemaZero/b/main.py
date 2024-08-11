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
        pi_aprox_i= 4*(4*teta1[i] - teta2[i])
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
    teta1 = calcular_arctg(1/5, n)
    teta2 = calcular_arctg(1/239, n)
    pi_aproximado=calcular_piaprox(teta1, teta2)
    erros = calcular_erro(n, pi_aproximado)

    for i in range(n):
        print(f"Iteração {i + 1}: pi aproximado = {pi_aproximado[i]}, erro = {erros[i]}")

    plt.plot(range(n), erros, marker='o')
    plt.grid(True, which="both", linestyle='--', linewidth=0.5)
    plt.show()

if __name__ == "__main__":
    main()
    print(math.pi)
    


