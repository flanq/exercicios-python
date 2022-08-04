# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('Digite 3 números e vamos verificar qual é o maior e o menor.')
primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
terceiro = int(input('Digite o segundo número: '))
numeros = [primeiro, segundo, terceiro]

print('O número maior é o {}' .format(max(numeros)))
print('O número menor é o {}' .format(min(numeros)))