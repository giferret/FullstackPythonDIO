class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b
    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b

calculadora = Calculadora()

print(calculadora.soma(10, 6))
print(calculadora.subtracao(30, 7))
print(calculadora.multiplicacao(50, 8))
print(calculadora.divisao(80, 9))


