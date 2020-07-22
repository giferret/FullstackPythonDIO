class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power (self):
        if self.ligada:   # Equivale a  ====>  if self.ligada == True:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal +=1

    def diminui_canal(self):
        if self.ligada:
            self.canal -=1

print(__name__)
if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    print(televisao.canal)
    televisao.power()
    print(televisao.ligada)
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print(televisao.canal)
    televisao.diminui_canal()
    print(televisao.canal)



# Poderiamos fazer também:
# print('Televisao está ligada: {}'.format(televisao.ligada))
# televisao.power()
# print('Televisao está ligada: {}'.format(televisao.ligada))
# televisao.power()
# print('Televisao está ligada: {}'.format(televisao.ligada))