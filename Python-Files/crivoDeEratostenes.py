from time import time

def readInt():
    while True:
        try:
            return int(input())
        except:
            print('ERRO! Digite um número inteiro!')

# Retorna a raíz quadrada de um número inteiro arredondada para baixo
def sqrtToInt(num):
    try:
        return int(num ** 0.5)
    except:
        print(f'ERRO! Não foi possível calcular a raíz de {num}. Retornando 0!')
        return 0

# Retorna uma lista de números primos
def primosDe(deX, ateY):
    listaPrimos = list()
    try:
        for i in range(deX, ateY + 1):
            listaAUX = list()
            for j in range(1, i + 1):
                if i % j == 0:
                    listaAUX.append(j)
            if len(listaAUX) == 2:
                listaPrimos.append(i)
        return listaPrimos
    except:
        print(f'ERRO! Não foi possível descobrir os números primos de {deX} até {ateY}. Retornando uma lista vazia!')
        return list()

def crivoDeEratostenes(inicio, limite):
    if inicio < 2:
        inicio = 2
    if limite < inicio:
        limite = inicio

    listaPrimos = list(range(inicio, limite + 1))
    listaAUX = primosDe(2, sqrtToInt(limite))
    aux = 0

    for numPrimo in listaAUX:
        for numLista in listaPrimos:
            if numLista % numPrimo == 0:
                try:
                    listaPrimos.remove(numLista)
                except:
                    pass
        if numPrimo >= inicio:
            listaPrimos.insert(aux, numPrimo)
            aux += 1
    return listaPrimos

def main():
    print('Qual o número de inicio que você quer saber os primos?', end=' ')
    tamanhoInicial = readInt()
    while tamanhoInicial < 2:
        print('Digite um número maior ou igual a 2', end=' ')
        tamanhoInicial = readInt()

    print('Até qual número você quer saber os primos?', end=' ')
    tamanhoFinal = readInt()
    while tamanhoFinal < tamanhoInicial:
        print(f'Digite um número maior que {tamanhoInicial}.')
        tamanhoFinal = readInt()
    
    # Salva o tempo atual em segundos desde uma época em uma variável.
    timeStart = time()
    print('Temporizador iniciado!')

    # Calcula e retorna uma lista com os números primos
    print(crivoDeEratostenes(tamanhoInicial, tamanhoFinal))

    # Salva o tempo atual em segundos desde uma época em uma variável.
    timeEnd = time()
    print('Temporizador finalizado!')

    # Calcula o tempo que o programa demorou pra executar da variável timeStart até a variável timeEnd.
    timeUsed = timeEnd - timeStart
    print(f'\n O programa levou {timeUsed:.3f} segundos para calcular.')

if __name__ == '__main__':
    main()
