import random

vetor_randomizado = []
#Gera vetor ordenada
def gerar_vetor():
    lista_numeros = []
    for num in range(1, 50001):
        lista_numeros.append(num)
        #print(num)
    return lista_numeros


#Função para randomizar vetor
def randomizar_vetor(vetor):
    indices_aleatorios = list(range(len(vetor)))
    random.shuffle(indices_aleatorios)

    vetor_randomizado = [vetor[i] for i in indices_aleatorios]

    return vetor_randomizado
