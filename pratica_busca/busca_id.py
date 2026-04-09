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
    chave = input('Digite o ID a ser buscado: ')
    achou = False
    reg = leia_reg(entrada)
    while reg != '' and not achou:
        id = reg.split(sep='|')[0]
        if id == chave:
            achou = True
        else:
            reg = leia_reg(entrada)
    if achou:
        #campo = ''
        for c in reg.split(sep='|'): #as partes comentadas é pra quando lê apenas reg, ambas fazem a mesma coisa
            # if c != '|':
            #    campo += c
            # else:
            #     print(campo)
            #     campo = ''
            print(c)
    else:
        print('O registro de ID não foi encontrado')
    entrada.close()

main()