#Cria uma linha
def linha():
    print("\033[1m=\033[m" * 43)


#Cria um cabeçalho
def cabecalho(msg = "<vazio>"):
    linha()
    print(f"\033[1m{msg:^43}\033[m")
    linha()


#Cria um menu personalizado
def menu(lista):
    for posicao, opcao in enumerate(lista):
        print(f"\033[34;1m{posicao + 1}\033[m - \033[1m{opcao}\033[m")
