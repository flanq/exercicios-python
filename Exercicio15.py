 #Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
fraseunida = frase.replace(" ", "")
inverso = ''
for i in range (len(fraseunida) -1, -1, -1):
  inverso += fraseunida[i]
print()
print(fraseunida, inverso)
print()
if (fraseunida == inverso):
  print('   A FRASE É UM PALINDRO!  ')
else:
  print('  A FRASE NÃO É UM PALINDRO!  ')