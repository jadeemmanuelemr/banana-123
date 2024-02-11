sizeStr = 'Escolha o tamanho: \n P - 300ml \n M - 500ml\n'

beverage = int(input('Digite o número da sua bebida: \n 1 - Coca\n 2 - Guaraná\n 3 - Suco de Uva\n 4 - Suco de Laranja\n'))
while (beverage < 1) or (beverage > 4):
    beverage = int(input('Please choose one of the given options: \n 1 - Coca\n 2 - Guaraná\n 3 - Suco de Uva\n 4 - Suco de Laranja\n')) 

if (beverage == 1) or (beverage == 2):
    size = input(f'{sizeStr} G - 700ml\n')
    while (size.lower() != 'p') and (size.lower() != 'm') and (size.lower() != 'g'):
        size = input(f'Please choose a cup size\n{sizeStr} G - 700ml\n')
else:
    size = input(f'{sizeStr}')
    while (size.lower() != 'p') and (size.lower() != 'm'):
        size = input(f'Please choose a cup size\n{sizeStr}')


noIce = input('Deseja tirar o gelo: S/N\n')
while (noIce != 's') and (noIce != 'n'):
    noIce = input('Please choose Y/N')

localRef = int(input('1 - Take Out\n2 - Eat In\n'))
while (localRef < 1) or (localRef > 2):
    localRef = int(input('Please choose one of the available options\n1 - Take Out\n2 - Eat In\n1'))


match beverage:
    case 1:
        flavor = 'coca'
        flavorStr = 'Coca-Cola'
        type = 'refrigerante'
        ice = 6
        cup = 'papel'
    case 2:
        flavor = 'guarana'
        flavorStr = 'Guaraná'
        type = 'refrigerante'
        ice = 6
        cup = 'papel'
    case 3:
        flavor = 'uva'
        flavorStr = 'Suco de Uva'
        type = 'suco'
        ice = 12
        cup = 'plastico'
    case 4: 
        flavor = 'laranja'
        flavorStr = 'Suco de Laranja'
        type = 'suco'
        ice = 12
        cup = 'plastico'

if (noIce.lower() == 's'):
    ice = 0

if (localRef == 1):
    lid = 'solid'
else:
    lid = 'straw'

if (size == 'p'):
    sizeOrder = 'P - 300ml'
elif (size == 'm'):
    sizeOrder = 'M - 500ml'
else:
    sizeOrder = 'G - 700ml'

if (localRef == 1):
    localStr = 'Para Levar'
else:
    localStr = 'Comer no Local'


if (noIce == 's'):
    print(f'Confira seu pedido\nBebida: {flavorStr}\nTamanho: {sizeOrder}\n{localStr}\n*Obs: Sem Gelo')
else:
    print(f'Confira seu pedido\nBebida: {flavorStr}\nTamanho: {sizeOrder}\n{localStr}')