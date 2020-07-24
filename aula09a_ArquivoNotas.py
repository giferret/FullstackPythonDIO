#     import shutil

def escreverArquivo(NomeArquivo, texto):

    arquivo = open('notas.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizarArquivo(NomeArquivo, texto):
    arquivo = open(NomeArquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def lerArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
    texto = arquivo.read()
    print(texto)

def mediaNotas(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
    alunoNota = arquivo.read()
    alunoNota = alunoNota.split('\n')
    print(alunoNota)
    for x in alunoNota:
        listaMedia = []
        listaNota = x.split(',')
        aluno = listaNota[0]
        listaNota.pop(0)
        print(aluno)
        print(listaNota)
        media = lambda notas: sum([int(i) for i in notas]) /4
        print(media(listaNota))
        listaMedia.append({aluno: media(listaNota)})
    return listaMedia


# def copiaArquivo(nomeArquivo):

#     shutil.copy(nomeArquivo, 'diretorio')

def moveArquivo(nomeArquivo):
    shutil.move(nomeArquivo, 'diretorio para o qual se pretende alterar')

if __name__ == '__main__':
    listaMedia = mediaNotas('notas.txt')
    print(listaMedia)
    #escreverArquivo('notas.txt', 'Rafael, 10, 3, 9, 8\n')
    #aluno =  'Fernando, 7, 8, 5, 5\n'
    #atualizarArquivo('notas.txt', aluno)
    #lerArquivo('teste.txt')