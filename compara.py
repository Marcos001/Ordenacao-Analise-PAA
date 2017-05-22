
from algoritmos_sort import ShellSort, BubleSort, BucketSort
import os, timeit, time
import matplotlib.pyplot as plt



def get_lista():
    lista_int = []
    file = open(os.getcwd()+'/a_numeros.txt', 'r')
    lista = file.read()
    file.close()

    #print('lista do arquivo file = ', lista, 'tamanho = ', len(lista))

    tmp = ''

    for i in lista:
        if i != '\n':
            tmp += str(i)
        else:
            lista_int.append(int(tmp))
            tmp = ''

    #print('lista_int = ', lista_int)
    return lista_int

def get_melhor_pior_caso(lista_int):
    print('processando lista melhor e pior caso > ')

    lista_m = sorted(lista_int)
    lista_p = []
    for i in range(len(lista_m)):
        pos = len(lista_m) - i
        #print('ind = ', len(lista_m), ' - ', i, 'valor = ', pos)
        lista_p.append(lista_m[pos - 1])
    return lista_m, lista_p,

def vendo_listas(lista_int,lista_m, lista_p):
    print('lista aleatoria = ', lista_int, ' tam = ', len(lista_int))
    print('lista no melhor caso = ', lista_m, ' tam = ', len(lista_m))
    print('lista no pior caso = ', lista_p, ' tam = ', len(lista_p))

def calcular_tempo_timeit(lista, tipo):
    '''calcular tempo de execucao'''

    operacao = 'w'

    name_file = os.getcwd()+'/'+tipo + '.txt'
    arquivo = open(name_file, operacao)

    #calculando o ShellSort()
    print('calculando shell em caso ', tipo)
    tempo_ShellSort = timeit.timeit("ShellSort({})".format(lista), setup="from __main__ import ShellSort", number=1)
    arquivo.write(str(float(tempo_ShellSort))+'\n')
    print('shell done.')

    print('calculando buble em caso ', tipo)
    # calculando o BubleSort()
    tempo_BubleSort = timeit.timeit("BubleSort({})".format(lista), setup="from __main__ import BubleSort", number=1)
    arquivo.write(str(float(tempo_BubleSort))+'\n')
    print('buble done.')

    # calculando o BucketSort
    print('calculando bucket em caso ', tipo)
    tempo_BucketSort = timeit.timeit("BubleSort({})".format(lista), setup="from __main__ import BubleSort", number=1)
    arquivo.write(str(float(tempo_BucketSort))+'\n')
    print('bucket done.')

def calcular_tempo_fim_menos_inicio(lista, tipo):
    '''calcular tempo de execucao'''

    operacao = 'w'

    name_file = os.getcwd()+'/'+tipo + '.txt'
    arquivo = open(name_file, operacao)

    #calculando o ShellSort()
    inicio = time.time()
    ShellSort(lista)
    fim = time.time()
    tempo_ShellSort = fim-inicio
    arquivo.write(str(float(tempo_ShellSort))+'\n')

    # calculando o BubleSort()
    inicio = time.time()
    BubleSort(lista)
    fim = time.time()
    tempo_BubleSort = fim - inicio
    arquivo.write(str(float(tempo_BubleSort))+'\n')

    # calculando o BucketSort()
    inicio = time.time()
    BucketSort(lista)
    fim = time.time()
    tempo_BucketSort = fim - inicio
    arquivo.write(str(float(tempo_BucketSort))+'\n')

def gerar_grafico(shell, buble, bucket, tipo):
    ''''''
    y_axis = [shell, buble, bucket]
    x_axis = range(len(y_axis))
    width_n = 0.4
    bar_color = 'green'
    algortirmos = ['shell', 'buble', 'bucket']

    plt.bar(x_axis, y_axis, width=width_n, color=bar_color, align='center')
    plt.ylabel('Tempo')
    plt.xlabel('Algoritmos')
    plt.xticks(x_axis, algortirmos, rotation='vertical')
    plt.title('Caso '+str(tipo))
    plt.tight_layout()
    plt.grid(True)
    plt.savefig(os.getcwd()+'/_plot/'+str(tipo)+'.png')
    print('figura ', tipo, '.png salva!')
    plt.show()

def get_valores_pro_grafico(tipo):
    ''''''
    arquivo = open(os.getcwd()+'/'+str(tipo)+'.txt', 'r')
    valores = arquivo.read()
    print(valores)
    arquivo.close()
    shell = 0
    buble = 0
    bucket = 0
    tmp = ''
    v1 = True
    v2 = False
    v3 = False
    for i in range(len(valores)):

        if valores[i] == '\n':
            if shell == 0 and v1:
                shell = tmp
                tmp = ''
                v1 = False
                v2 = True
            elif buble == 0 and v2:
                buble = tmp
                tmp = ''
                v2 = False
                v3 = True
            elif bucket == 0 and v3:
                bucket = tmp
                tmp = ''
        else:
            tmp += valores[i]

        print(valores[i])
    print('s = ', shell, ' b1 = ', buble, ' b2 = ', bucket)

    a = float(shell[:10])
    b = float(buble[:10])
    c = float(bucket[:10])
    gerar_grafico(a,b,c,tipo=tipo)



if __name__ == '__main__':

    var_pior = 'pior'
    var_melhor = 'melhor'
    var_random = 'random'

    from gerar_numeros import gerar_numeros


    print('gerando numeros >')
    gerar_numeros(quantidade=100000, maximo=1000000)

    print('obtendo as listas de valores > ')
    lista_int = get_lista() #obtendo lista noarquivo a_numeros.txt gerada aleatoriamente

    lista_m, lista_p = get_melhor_pior_caso(lista_int) #lista do melhor e pior caso

    vendo_listas(lista_int, lista_m,lista_p) #

    print('tamanhos', len(lista_int),' : ', len(lista_m),' : ', len(lista_p))


    #"""
    print('Calculando tempo de execução com timeit')  #
    calcular_tempo_timeit(lista_int,var_random)       #
    calcular_tempo_timeit(lista_m, var_melhor)        #
    calcular_tempo_timeit(lista_p, var_pior)          #
    print('done timeit().')
    #"""


    """
    print('Calculando tempo de execução com ini_fim() > ')
    calcular_tempo_fim_menos_inicio(lista_int, var_random)
    calcular_tempo_fim_menos_inicio(lista_m, var_melhor)
    calcular_tempo_fim_menos_inicio(lista_p, var_pior)
    print('done ini_fim().')
    """


    print('gerando os graficos > ')
    #gera os gráficos dos tempos
    get_valores_pro_grafico(var_random)
    get_valores_pro_grafico(var_pior)
    get_valores_pro_grafico(var_melhor)
    #"""


