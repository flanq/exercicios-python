# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual é a velociodade atual do carro: '))
print('Sua velocidade atual é {}km/h!' .format(velocidade))

multa = (velocidade - 80) * 7

if velocidade <= 80:
  print('Você está na velocidade recomendada. Boa Viagem.')
else: 
  multa = (velocidade - 80) * 7
  print ('Você ultrapassou a velocidade recomendada e será multado em R${:.2f}' .format(multa))