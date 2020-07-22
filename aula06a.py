conj1 = {1, 2, 3, 4, 5}
conj2 = {5, 6, 7, 8, 9}
conjA = {2, 3, 4}
conjB = {1, 2, 3, 4, 5, 6}
conjUniao = conj1.union(conj2) # Não Faz diferença a ordem dos fatores
conjIntersecao = conj1.intersection(conj2) # Não Faz diferença a ordem dos fatores
conjDiferenca = conj2.difference(conj1) # Faz diferença a ordem dos fatores
conjDiffSimetrico = conj1.symmetric_difference(conj2) # Não Faz diferença a ordem dos fatores
conjSubset = conjA.issubset(conjB) # Verifica se um conjunto é subconjunto do outro
conjSuperset = conjA.issuperset(conjB) # Verifica se um conjunto é um superconjunto de outro

lista = ['cachorro', 'cachorro', 'gato', 'gato']
removerDuplicidade = set(lista)
print(removerDuplicidade)
voltaLista = list(removerDuplicidade)
print(voltaLista)

# print(conjUniao)
# print(conjIntersecao)
# print(conjDiferenca)
# print(conjDiffSimetrico)

lista = ['cachorro', 'cachorro', 'gato', 'gato']
removerDuplicidade = set(lista)

print(conjSubset)
print(conjSuperset)


# conjunto = {1, 2, 3, 4, 5, 4, 2}
# conjunto.add(6)
# conjunto.discard(2)
# print(conjunto)