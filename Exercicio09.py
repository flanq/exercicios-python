# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite um número: '))

print('O número digitado foi {}' .format(numero))
print('O número é PAR!' if numero%2 == 0 else 'O número é IMPAR!')