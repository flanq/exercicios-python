#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('          Simulador de financiamento de imóvel          ')
valor_casa = float(input('Qual o valor do imóvel: '))
salario = float(input('Qual o seu salário: '))
anos = int(input('Qual o periodo em anos do financiamento: '))

prestacao_mensal = valor_casa / (anos * 12)


if (prestacao_mensal <= salario * 0.3):
  print('Financiamento aprovado com o valor mensal de R${:.2f}, durante {} anos.' .format(prestacao_mensal, anos) )
else:
  print('FINANCIAMENTO NEGADO!')