idade_CNH = 18
excessao = 17

idade = int(input('Digite a sua idade: '))

if idade >= idade_CNH:
    print('Acesso Autorizado!')

if idade == excessao:
    print('Liberado somente aulas teóricas!')

#Ex.1
elif idade < idade_CNH:
    print('Acesso Negado')
#Ex.2
# else:
#     print('Acesso Negado!')
