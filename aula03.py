#Compara três valores e vê informa qual é o maior
a = int(input())
b = int(input())
c=int(input())

if a > b and a > c:
    print('o maior número é {}'.format(a))
elif b > a and b > c:
    print('o maior número é {}'.format(b))
else:
    print('o maior número é {}'.format(c))