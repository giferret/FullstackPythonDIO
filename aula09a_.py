# arquivo = open('teste.txt', 'w') # Escrever pela primeira vez
# arquivo.write('Primeira escrita')
# arquivo = open('teste.txt', 'a') #Atualiza o arquivos com novas informações
# arquivo.write('\nSegunda Linha')
# arquivo.close()


def escreverArquivo(texto):
    diretorio = ('C:/Users/Gisele/PycharmProjects/teste.txt')
    #OU arquivo = open('C:/Users/Gisele/PycharmProjects/teste.txt', 'w')
    arquivo = open(diretorio, 'w')
    #arquivo = open ('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizarArquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def lerArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
    alunoNota = arquivo.read()
    alunoNota = alunoNota.split('\n')
    print(alunoNota)
    for x in alunoNota:
        listaNota = x.split(',')
        print(listaNota)

if __name__ == '__main__':
    escreverArquivo('Primeira linha \n')
    #atualizarArquivo('Segunda linha \n')
    #lerArquivo('teste.txt')