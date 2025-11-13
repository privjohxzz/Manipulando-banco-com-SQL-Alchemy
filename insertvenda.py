from coneccao import Session

from bd import Venda

with Session() as session:
    vendas = Venda(carro = 'porsche gts 911',valor = 1000000000,comissao = 2000,vendedor_id = 1)

    session.add(vendas)
    session.commit()
    print("vendas registradas com sucesso")