from enum import Enum

class States(Enum):
    '''P = preto
    N = not(preto)'''
    NPP = 1
    PPN = 2
    NPN = 3
    PPP = 4
    NNP = 5
    PNN = 6
    NNN = 7
    PNP = 8

def verificaCor():
    # 1 preto e 0 branco
    global esquerdo
    global direito
    global meio
    
    esquerdo, meio, direito = input().split()
    esquerdo = int(esquerdo)
    meio = int(meio)
    direito = int(direito)

def verificaEstado():
    global esquerdo
    global direito
    global meio
    global estado

    if(esquerdo != 1 and meio == 1 and direito == 1): #NPP
        estado = States(1)
    if(esquerdo == 1 and meio == 1 and direito != 1): #PPN
        estado = States(2)
    if(esquerdo != 1 and meio == 1 and direito != 1): #NPN
        estado = States(3)
    if(esquerdo == 1 and meio == 1 and direito == 1): #PPP
        estado = States(4)
    if(esquerdo != 1 and meio != 1 and direito == 1): #NNP
        estado = States(5)
    if(esquerdo == 1 and meio != 1 and direito != 1): #PNN
        estado = States(6)
    if(esquerdo != 1 and meio != 1 and direito != 1): #NNN
        estado = States(7)
    if(esquerdo == 1 and meio != 1 and direito == 1): #PNP
        estado = States(8)
    print(estado, '\n')
def verificaVerde():
        global e_verde
        global d_verde
        global verde
        global verde_direito

        if esquerdo==2:
            e_verde= True
        elif esquerdo == 0:
            e_verde = False
        if direito==2:
            d_verde = True
        elif direito == 0:
            d_verde = False
        print(e_verde, '\n', d_verde)

    
    

e_verde = False
d_verde = False
esquerdo = 0
direito = 0
meio = 0
estado = 0
while(1):
    verificaCor()
    verificaEstado()
    verificaVerde()