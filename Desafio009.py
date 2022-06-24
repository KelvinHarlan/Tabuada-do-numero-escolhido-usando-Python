numero=  int (input('Escolha um número inteiro para que possamos ver sua tabuada:\n'))
print('')
print('Esta é a tabuada do número escolhido: ')
print('_'*12)
for digito in range(1,11):
    print(f'{numero} x {digito} = {digito*numero}')

print('_'*12)
print('Realizado com sucesso!')
