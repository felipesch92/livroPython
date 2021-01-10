from clientes import Clientes
from contas import Conta
from bancos import Banco
felipe = Clientes('Felipe Schmaedecke', '49-99199-9899')
tamara = Clientes('Tamara Cardoso Gruetzmann', '51-98175-0510')
joao = Clientes('João da Silva', '51-93821-3912')
jose = Clientes('José Ricardo Tiesca', '51-99483-3192')
c1 = Conta([felipe], '55982', 5500)
c2 = Conta([felipe, tamara], '69832', 1000)
c3 = Conta([joao, jose], '39821', 500)
tatu = Banco('Tatú')
tatu.abre_conta(c1)
tatu.abre_conta(c2)
tatu.abre_conta(c3)
tatu.lista_contas()
