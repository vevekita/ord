import sys

def main():
    NOME_ARQ = input("Digite o nome do arquivo: ")
    SAIDA = open(NOME_ARQ, 'w')
    SOBRENOME = input("Digite o sobrenome: ")
    while SOBRENOME != '':
        NOME = input("Digite o nome: ")
        ENDERECO = input("Digite o endereço: ")
        CIDADE = input("Digite a cidade: ")
        ESTADO = input("Digite o Estado: ")
        CEP = input("Digite o CEP: ")

        TODAS_INFO = str(SOBRENOME) + '|' + str(NOME) + '|' + str(ENDERECO) + '|' + str(CIDADE) + '|' + str(ESTADO) + '|' + str(CEP) + '|'
        SAIDA.write(TODAS_INFO)

        SOBRENOME = input("Digite o sobrenome: ")
        
    SAIDA.close()

main()


