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
    entrada = open('pessoasGOT.dat', 'rb')
    chave = input('Digite o sobrenome a ser buscado: ')
    reg = leia_reg(entrada)

    for i in reg.split(sep='|'):    
        if i == chave:
            print(i)
        else:
            reg = leia_reg(entrada)

    entrada.close()

main()