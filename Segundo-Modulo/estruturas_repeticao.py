#Estrutura de repetição do for com o range
# for numeros in range(21):
#     print(numeros)


#Usando o while
opcao = -1

while opcao != 0:

    opcao = int(input('[1]- Pix [2]- Cartão de Débito [3]- Cartão de Crédito: '))

    if opcao == 1:
        print('Recebendo pix...')

    elif opcao == 2:
        print('Recebendo no débito...')

    else:
        print('Recebendo no crédito...')


# contador = 1

# while contador <= 100:
#     print(contador)

#     contador += 1 

