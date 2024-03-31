import random

def numerosParesMultiplicados(lista):
    novaLista = []
    
    for numero in lista:
        if numero % 2 == 0:
            novaLista.append(numero * 2)

    return novaLista


listaOriginal = [random.randint(1, 100) for _ in range(10)]
resultado = numerosParesMultiplicados(listaOriginal)

print("Lista Original:", listaOriginal)
print("Lista Resultante:", resultado)

