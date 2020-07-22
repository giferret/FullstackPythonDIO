#Lista é mutável
#tupla é imutável

lista = [12,15, 3, 5, 7]
lstAnimais = ['cachorro', 'gato', 'elefante', 'arara','lobo']
# print(lstAnimais[2])

# for x in lstAnimais:
#     print(x)

# soma = 0
# for x in lista:
#      print(x)
#      soma += x
# print(soma)

# Outra forma de somar os valores em uma lista

# print(sum(lista))
#
# print(max(lista))
#
# print(min(lstAnimais)) # Letra do alfabeto
#
# print(max(lstAnimais))

# if 'lobo' in lstAnimais:
#     print('Existe valor na lista')
# else:
#     print('não existe valor na lista e será incluido')
#     lstAnimais.append('lobo')
#     print(lstAnimais)

#lstAnimais.pop(indice ou não - sem indice exclui o último da lista)

#Ordenando a lista:
#
# lista.sort()
# lstAnimais.sort()
# print(lista)
# print(lstAnimais)

#Tuplas declaração

# tupla = (1,3,4,7, 9)
# print(tupla[2])
# print(len(tupla))

tupla_animal = tuple(lstAnimais)
print(tupla_animal)
len()