from clientes import Clientes
from contas import Conta, ContaEspecial
from bancos import Banco
felipe = Clientes('Felipe Schmaedecke', '49-99199-9899')
tamara = Clientes('Tamara Cardoso Gruetzmann', '51-98175-0510')
c1 = Conta([felipe], 59832, 5500)
c2 = ContaEspecial([felipe, tamara], 12313, 500, 1000)
c1.saque(100)
c2.deposito(300)
c1.saque(190)
c2.deposito(95.15)
c2.saque(1500)
c1.extrato()
c2.extrato()
