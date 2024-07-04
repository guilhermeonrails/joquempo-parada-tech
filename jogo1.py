import random

print('*** Pedra, papel e tesoura ***')
#                       0.   1.    2.
pedra_papel_tesoura = ['🗿', '📄', '✁']
maquina = random.choice(pedra_papel_tesoura)
# print(maquina)

print('\nEscolha a sua opção')
print('1. Pedra  🗿')
print('2. Papel  📄')
print('3. Tesoura ✁')

player = int(input('\nDigite a sua opção: '))
player = pedra_papel_tesoura[player - 1]
# print(player)

vitoria = {
    '🗿':'✁',
    '✁':'📄',
    '📄': '🗿'
}

if player == maquina:
    print('Empate')
elif vitoria[player] == maquina:
    print('Você venceu')
else:
    print('Você perdeu')

print(f'{player} vs {maquina}')
