class Calibration(Robot):
    def __init__(self):
        Robot.__init__(self)

    def white():
        with open("white_esq.txt", "w") as white_esq:
            esq_lida1 = se.raw
            esq_lida1 = str(esq_lida1)
            white_esq.write(esq_lida1);
            print(esq_lida1)


    def black():
        with open("black_esq.txt", "w") as black_esq:
            esq_lida2 = se.raw
            esq_lida2 = str(esq_lida2)
            black_esq.write(esq_lida2);
            print(esq_lida2)

calibra = Calibration()

sleep(2000)
calibra.white()
sleep(5000)
calibra.black()
sleep(5000)





    '''def abrirAprendizado():
    ## try: tenta abrir um arquivo de aprendizado
    try:
        with open("aprendizado.txt", "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            robot.aprendizado = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            robot.aprendizado.pop()
            for x in robot.aprendizado:
                print("x", x, "int(x)", int(x))
            robot.aprendizado = [int(x) for x in robot.aprendizado]     # tornamos as strings em inteiros
    except:
        robot.aprendizado = [47, 47, 47]                         # caso nao haja arquivo, criamos a lista
    return robot.aprendizado                                  # Retorna a lista "aprendizado"
'''
