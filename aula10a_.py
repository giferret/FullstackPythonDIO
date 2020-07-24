from datetime import date, time, datetime, timedelta


def trabalhandoComTimeDelta():
    dataString = '01/01/2000'
    dataConvertida = datetime.strptime(dataString, '%d/%m/%Y')
    print(dataConvertida)
    novaData = dataConvertida - timedelta(days=365)
    novaData = dataConvertida + timedelta(days=365)
    novaData = dataConvertida - timedelta(days=365, hours=2, minutes=15)
    print(novaData)


def trabalhandoComDatetime():
    dataAtual = datetime.now()
    print(dataAtual)
    print(dataAtual.strftime('%d/%m/%y %H:%M:%S'))
    print(dataAtual.strftime('%c'))
    print(dataAtual.year)
    print(dataAtual.month)
    print(dataAtual.day)
    print(dataAtual.weekday()+1) # mais 1 apenas para contarmos a partir de segunda como sendo 1 e não zero como é no Python
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[dataAtual.weekday()])
    dataCriada = datetime(2016, 5, 13, 15,30,6)
    print(dataCriada)
    print(dataCriada.strftime('%c'))
    dataString = '01/01/2000'
    dataConvertida = datetime.strptime(dataString, '%d/%m/%Y')
    print(dataConvertida)
    print(type(dataConvertida))





def trabalhandoComDate():

    dataAtual = date.today()
    dataAtualSTR = dataAtual.strftime('%A %B %Y')

    print(dataAtual)
    print(dataAtual.strftime('%d/%m/%y'))
    print(dataAtual.strftime('%d/%m/%Y'))
    print(dataAtual.strftime('%d-%m-%Y'))
    print(dataAtual.strftime('%A %B %Y'))

    print(type(dataAtual))
    print(type(dataAtualSTR))

def trabalhandoComTime():
    horario = time(hour=15, minute=30, second= 50)
    print(horario)
    print(type(horario))
    horarioSTR = horario.strftime('%H:%M:%S')
    print(horario.strftime('%H:%M:%S'))
    print(type(horarioSTR))

if __name__ == '__main__':
    #trabalhandoComDate()
    #trabalhandoComTime()
    #trabalhandoComDatetime()
    trabalhandoComTimeDelta()