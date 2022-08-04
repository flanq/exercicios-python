#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distância da sua viagem em km? '))
curta = distancia * 0.5
longa = distancia * 0.45

if distancia <= 200:
  print('O valor da sua passaem é R${:.2f}' .format(curta))
else:
  print('O valor da sua passaem é R${:.2f}' .format(longa))
