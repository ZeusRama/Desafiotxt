def ordenar_numeros(arquivo):
    try:
        with open(arquivo, 'r') as f:
            numeros = [int(linha.strip()) for linha in f.readlines()]

        for i in range(len(numeros)):
            for j in range(0, len(numeros) - i - 1):
                if numeros[j] > numeros[j + 1]:
                    # Troca os números de posição
                    numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

    
        print("Números ordenados:", numeros)

    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except ValueError:
        print("Erro: O arquivo deve conter apenas números inteiros.")

ordenar_numeros('extra.txt')
