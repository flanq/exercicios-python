#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.


from random import randint

computer = randint(0,5)

print('Vou pensar em um número entre 0 e 5 tente adivinhar!')
print('-' * 20)
numero = int(input('Digite o número que eu pensei: '))

if numero == computer:
  print('Você acertou! Eu realmente pensei no número {}!' .format(computer))
else:
  print('Você errou! O número que eu pensei foi {} e não {}!' .format(computer, numero))
