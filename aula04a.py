#Esse trecho de código exibe na tela os números primos até o valor digitado pelo usuário, inclusive

a = int(input('Entre com um valor: '))

for i in range (a+1):
    div = 0
    for x in range(1, i+1):
        if (i % x) == 0:
            div += 1
    if div == 2:
        print(i)

# # Esse trecho de código imprime os números primos de 0 até 100
#
# #Conhecer os números números primos até o 100
#
# for i in range (101):
#     div = 0
#     for x in range(1, i+1):
#         if (i % x) == 0:
#             div += 1
#     if div == 2:
#         print(i)



# #Conhecer os números números primos até o 100
#
# num = int(input())
# div = 0
# for x in range(1, num+1):
#     if (num % x) == 0:
#         div = div +1 #div +=1 poderia ser escrito desta forma
# if div == 2:
#     print('número {} eh primo'.format(num))
# else:
#     print('número {} não eh primo'.format(num))

# for x in range (101):
#     print(x)
