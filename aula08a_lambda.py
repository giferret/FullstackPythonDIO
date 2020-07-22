# Lambda função anônima

contadorLetras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contadorLetras(lista_animais))

# A função lambda é mais eficiente apenas para funções que conseguimos fazer em apenas uma linha

soma = lambda a, b: a + b

print(soma(5, 32))

# É possível criar uma calculadora inteira com a função soma utilizando dicionários

calculadora = {
    'soma': lambda a, b: a + b,
    'subtração': lambda a, b: a - b,
    'multiplicação': lambda a, b: a * b,
    'divisão': lambda a, b: a / b
}

print(type(calculadora))

soma = calculadora['soma']      # soma = lambda a, b: a + b     é a mesma coisa
multiplicacao = calculadora['multiplicação']
print(soma(5,10))
print(multiplicacao(5,10))