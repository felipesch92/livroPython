class televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.marca = 'SAMSUNG'
        self.tamanho = '43'

    def muda_canal_cima(self):
        if self.canal < 50:
            self.canal += 1

    def muda_canal_baixo(self):
        if self.canal > 1:
            self.canal -= 1


tv = televisao()
print(tv.canal)
tv.muda_canal_cima()
tv.muda_canal_cima()
print(tv.canal)
tv.muda_canal_baixo()
print(tv.canal)
tv_sala = televisao()
tv_sala.ligada = True
tv_sala.canal = 10
print(tv_sala.ligada)
print(tv_sala.canal)
tv_sala.marca = 'TCL'
print(tv_sala.marca)
tv_sala.muda_canal_baixo()
tv_sala.muda_canal_baixo()
print(tv_sala.canal)
