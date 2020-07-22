#Conta a quantidade de letras em uma lista com várias palavras
def contadorLetras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

if __name__ == '__main__':
    lista = ['cachorro', 'gato']
    print(contadorLetras(lista))