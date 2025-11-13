from coneccao import Session

from bd import Vendedor

with Session() as session:
    
    vendedor = Vendedor(nome = 'joana',loja_id=1)
    
    session.add(vendedor)
    session.commit()
    print('deu certo')