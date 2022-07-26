#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.

nome = input('Qual é o seu nome completo? ')
print('Seu nome é: {}' .format(nome))
print('Seu nome em maiúsculo: {}' .format(nome.upper()))
print('Seu nome em minúsculo: {}' .format(nome.lower()))
print('Seu nome todo tem {} letras.' .format(len(nome.replace(" ", ""))))
print('Seu primeiro nome tem {} letras.' .format(nome.find(' ')))