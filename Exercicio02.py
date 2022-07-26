# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = (input('Digite um número de 0 a 9999: '))
var = 4-len(numero)
num = novo = numero.replace(numero, "0"*var+numero)
print('O numéro digitado foi {}' .format(numero))
print('Unidade: {}' .format(num[3]))
print('Dezena: {}' .format(num[2]))
print('Centena: {}' .format(num[1]))
print('Milhar: {}' .format(num[0]))