

def ShellSort(lista):
    intervalo = int((len(lista)/2))
    while intervalo > 0:
        for i in range(len(lista)):
            j = i
            atual = lista[i]
            while j >= intervalo and lista[j - intervalo] > atual:
                lista[j] = lista[j - intervalo]
                j-=intervalo
            lista[j] = atual
        intervalo = int(intervalo/2)
    return lista

def BubleSort(lista):#Algoritmo de Ordenação
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

def BucketSort(lista):#Algoritmo de Ordenação
    listaBucket = []
    for i in range(0,10):#Inicializando a Lista de Bucket
        listaBucket.append([])
    divisor = ((max(lista)+1)/len(listaBucket))#Max termo de lista/n termos de lista de Buckets
    if not isinstance(divisor,int):#tratamento para pegar o proximo inteiro
        divisor = int(divisor)+1
    for i in lista:#Inserindo Elementos na Lista Bucket
        indice = int(i / divisor)
        listaBucket[indice].append(i)
    for i in listaBucket:#Metodo de Ordenação para ordenar as sublistas da Listas Bucket
        for j in range(1,len(i)):
            if i[j] < i[j-1]:
                aux = i[j]
                i[j] = i[j-1]
                i[j-1] = aux
    indice = 0
    while indice < len(lista):#Devolvendo os elementos em ordem para a lista original
        for i in listaBucket:
            if not i == []:
                for j in i:
                    lista[indice] = j
                    indice+=1
    return lista