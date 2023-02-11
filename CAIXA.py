from designer_caixa import aparencia
from menus_caixa import interface

a = aparencia()
i = interface()
a.iniciar()
i.entrada()                          # senha 
a.carregar()
while True:  
    a.logotipo()                    # banco
    i.saldoConta()                  # saldo na tela
    a.linha()
    i.menuPrincipal()               # menu Principal
    a.linha()
    try:
        if i.saindo() == 'fim':
            break
    except:
        a.logotipo()
        i.saldoConta()              # saldo na tela
        a.linha()
        i.menuPrincipal()           # menu Principal
        a.linha()
   