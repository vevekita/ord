def leia_campo(entrada):
    campo = ''
    c = str(entrada.read(1))
    while c != '' and c != '|':
        campo += c
        c = str(entrada.read(1))

    return campo

def main():
    nome_arq = input("Digite o nome do arquivo a ser lido: ")
    entrada = open(nome_arq, 'r')
    campo = leia_campo(entrada)
    while campo != '':
        print(campo)
        campo = leia_campo(entrada)
    entrada.close()

main()