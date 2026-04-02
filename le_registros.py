def leia_reg(entrada):
    tam = entrada.read(2)
    tam_b = int.from_bytes(tam, 'little')
    if tam_b > 0:
        buffer_b = entrada.read(tam_b)
        buffer = buffer_b.decode()
        return buffer
    else:
        return ''
    
def main():
    nome_arq = input('Escreva o nome do arquivo a ser lido: ')
    entrada = open(nome_arq, 'rb')
    buffer = leia_reg(entrada)
    while buffer != '':
        campos = []
        campos += buffer.split(sep='|')
        for c in campos:
            print(c)
        buffer = leia_reg(entrada)
    entrada.close()
    
main()