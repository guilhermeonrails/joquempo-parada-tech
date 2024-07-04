# Parada Tech - Pedra, papel e tesoura

Este projeto foi feito durante a parada tech. Este é um simples jogo de Pedra, Papel e Tesoura implementado em Python. O jogo permite que o jogador escolha entre Pedra, Papel e Tesoura e então compara a escolha do jogador com a escolha da máquina para determinar o vencedor.

### Como jogar

Execute o script.
Escolha a sua opção (Pedra, Papel ou Tesoura) digitando o número correspondente.
O jogo irá exibir o resultado (vitória, derrota ou empate).\


### Regras do jogo

Pedra vence Tesoura.
Tesoura vence Papel.
Papel vence Pedra.

# Sobre o código

import random  # Importa o módulo random para gerar escolhas aleatórias para a máquina

print('*** Pedra, papel e tesoura ***')
# Define uma lista com as opções do jogo: Pedra, Papel e Tesoura
#                       0.   1.    2.
pedra_papel_tesoura = ['🗿', '📄', '✁']
maquina = random.choice(pedra_papel_tesoura)  # Escolhe aleatoriamente uma opção para a máquina
# print(maquina)  # Linha de debug para mostrar a escolha da máquina

print('\nEscolha a sua opção')
print('1. Pedra  🗿')
print('2. Papel  📄')
print('3. Tesoura ✁')

player = int(input('\nDigite a sua opção: '))  # Solicita ao jogador para escolher uma opção e converte a entrada para inteiro
player = pedra_papel_tesoura[player - 1]  # Ajusta a escolha do jogador para corresponder ao índice da lista
# print(player)  # Linha de debug para mostrar a escolha do jogador

# Dicionário que define as regras de vitória: cada chave vence o valor correspondente
vitoria = {
    '🗿':'✁',
    '✁':'📄',
    '📄': '🗿'
}

# Verifica o resultado do jogo comparando as escolhas do jogador e da máquina
if player == maquina:
    print('Empate')  # Se as escolhas forem iguais, é um empate
elif vitoria[player] == maquina:
    print('Você venceu')  # Se a escolha do jogador vencer a escolha da máquina, o jogador vence
else:
    print('Você perdeu')  # Caso contrário, o jogador perde

print(f'{player} vs {maquina}')  # Exibe as escolhas do jogador e da máquina

### vitoria.get (explicação)

Sempre que usamos o `vitoria.get('🗿')`, o ícone perdedor será exibido. Por exemplo:

```python
vitoria.get('🗿')
# saida será: ✁
```

Logo, se sabemos qual ícone ira perder, podemos comparar com a opção da máquina:

```python
vitoria[player] == maquina:
    print('Você venceu')
```

> Nesse caso, nós vencemos!
