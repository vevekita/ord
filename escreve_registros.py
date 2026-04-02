def main():
    nome_arq = input('Digite o nome do arquivo: ')
    saida = open(nome_arq, 'wb')
    campo = input('Escreva o sobrenome: ')
    while campo != '':
        buffer = ''
        buffer += campo + '|'
        campos = ['Escreva nome: ', 'Escreva endereço: ', 'Escreva cidade: ', 'Escreva estado: ', 'Escreva CEP: ']
        for c in campos:
            campo = input(c)
            buffer += campo + '|'
        buffer_b = buffer.encode('utf-8')
        tam = len(buffer_b)
        tam_b = tam.to_bytes(2, byteorder='little')
        saida.write(tam_b)
        saida.write(buffer_b)
        campo = input('Escreva o sobrenome: ')
    saida.close()

main()