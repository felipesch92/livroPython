class Televisao():
    def __init__(self, c):
        self.ligada = False
        self.canal = c
        self.marca = 'SAMSUNG'
        self.tamanho = '43'

    def muda_canal_cima(self):
        if self.canal < 50:
            self.canal += 1
        else:
            self.canal = 1

    def muda_canal_baixo(self):
        if self.canal > 1:
            self.canal -= 1
        else:
            self.canal = 50

tv_quarto = Televisao(48)
print(tv_quarto.canal)
tv_quarto.muda_canal_cima()
tv_quarto.muda_canal_cima()
tv_quarto.muda_canal_cima()
tv_quarto.muda_canal_cima()
tv_quarto.muda_canal_cima()
print(tv_quarto.canal)
tv_quarto.canal = 5
print(tv_quarto.canal)
tv_quarto.muda_canal_baixo()
tv_quarto.muda_canal_baixo()
tv_quarto.muda_canal_baixo()
tv_quarto.muda_canal_baixo()
tv_quarto.muda_canal_baixo()
tv_quarto.muda_canal_baixo()
print(tv_quarto.canal)
