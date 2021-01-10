from cidades import Cidade
from estados import Estado
c1 = Cidade('Erechim', 37498)
c2 = Cidade('Canoas', 350000)
c3 = Cidade('Porto Alegre', 439321)
e1 = Estado('Rio Grande Do Sul', 'RS', [c1, c2, c3])
c4 = Cidade('São Miguel Do Oeste', 41983)
c5 = Cidade('Chapecó', 225321)
e2 = Estado('Santa Catarina', 'SC', [c4, c5])
e1.resumo()
e2.resumo()
