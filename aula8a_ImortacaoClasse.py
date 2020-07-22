from aula07a_Televisao import Televisao
from aula07a_Calculadora1 import Calculadora
from aula08a_ContadorLetras import contadorLetras

if __name__ == '__main__':

    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(5, 10)
    print(calculadora.soma())

    lista = ['cachorro', 'gato', 'elefante']
    print(contadorLetras(lista))

    # Outra forma de mostrar

    total_letras = contadorLetras(lista)
    print('O total de letras por palavras da da lista: {}'.format(total_letras))


