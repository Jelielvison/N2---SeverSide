#Função do método merge sort para ordenar lista randomizada
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    # Dividir a lista ao meio
    meio = len(lista) // 2
    lista_esquerda = lista[:meio]
    lista_direita = lista[meio:]

    # Chamada recursiva para ordenar as duas metades
    lista_esquerda = merge_sort(lista_esquerda)
    lista_direita = merge_sort(lista_direita)

    # Combinar as duas listas ordenadas
    return merge(lista_esquerda, lista_direita)


def merge(lista_esquerda, lista_direita):
    lista_ordenada = []
    i = 0  # Índice para lista_esquerda
    j = 0  # Índice para lista_direita

    # Mesclar as duas listas ordenadas
    while i < len(lista_esquerda) and j < len(lista_direita):
        if lista_esquerda[i] < lista_direita[j]:
            lista_ordenada.append(lista_esquerda[i])
            i += 1
        else:
            lista_ordenada.append(lista_direita[j])
            j += 1

    # Adicionar os elementos restantes, se houver, de lista_esquerda
    while i < len(lista_esquerda):
        lista_ordenada.append(lista_esquerda[i])
        i += 1

    # Adicionar os elementos restantes, se houver, de lista_direita
    while j < len(lista_direita):
        lista_ordenada.append(lista_direita[j])
        j += 1

    return lista_ordenada
