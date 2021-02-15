from interface import * #Importa funções do arquivo "interface.py"
from funcoes import * #Importa funções do arquivo "funcoes.py"
from time import sleep #Importa função "sleep" da biblioteca "time"
cabecalho("AGENDA DE CONTATOS")

#Checa pela existência do arquivo
arquivo = "contatos.txt"
if not arquivo_existencia(arquivo):
    criar_arquivo(arquivo)

while True:
    #Menu pricipal
    cabecalho("MENU PRICIPAL")
    
    menu_principal = menu(["Novo contato", "Contatos cadastrados", "Sair da agenda"])
    escolha = leiaInt("\033[34;1mEscolha: \033[m")
    sleep(0.5)

    #Adicionar novo contato
    if escolha == 1:
        cabecalho("NOVO CONTATO")
        novo_contato(arquivo)
        sleep(1)

    #Ver contatos salvos
    elif escolha == 2:
        cabecalho("CONTATOS")
        lista_contatos(arquivo)
        sleep(2)

    #Sair do sistema
    elif escolha == 3:
        cabecalho("SAINDO...")
        break

    #Opção inválida
    else:
        print("\033[31mOpção inválida.\033[m")
        sleep(0.5)
        continue
