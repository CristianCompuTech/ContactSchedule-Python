#Checa pela existência do arquivo
def arquivo_existencia(nome):
    try:
        contatos = open(nome, "r")
        contatos.close()
    except (FileNotFoundError):
        return False
    else:
        return True

    
#Cria o arquivo (caso não exista)
def criar_arquivo(nome):
    try:
        contatos = open(nome, "w")
        contatos.close()
    except:
        print("\033[0;31mHouve um ERRO na criação do arquivo...\033[m \n")
    else:
        print("\033[32mArquivo criado!\033[m")


#Checa se um número inteiro é válido
def leiaInt(inteiro):
    while True:
        try:
            inteiro = int(input(inteiro))
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Digite apenas números inteiros!\033[m")
            continue
        else:
            return inteiro
            break


#Mostra os contatos salvos
def lista_contatos(nome):
    try:
        contatos = open(nome, "r")
    except:
        print("\033[0;31mHouve um ERRO ao abrir o arquivo...\033[m")
    else:
        for linha in contatos:
            linha = linha.replace("\n", "")
            print(f"\033[1m{linha}\033[m")


#Adiciona um novo contato
def novo_contato(nome):
    nome_pessoa = str(input("\033[34;1mNome: \033[m"))
    numero_pessoa = leiaInt("\033[34;1mNúmero: \033[m")

    try:
        contatos = open(nome, "a")
        contatos.writelines(f"Nome: {nome_pessoa:<22} Núm: {numero_pessoa:>3}\n")
    except:
        print("\033[0;31mHouve um ERRO ao escrever no arquivo...\033[m")
    else:
        print(f"\n\033[32;1mCadastro de {nome_pessoa} adicionado!\033[m")
