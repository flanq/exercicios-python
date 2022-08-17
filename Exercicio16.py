#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridadehomem = 0
homemmaisvelho = ''
mulhermenos20 = 0

for i in range (1,5):
  print('   CADASTRO {}º PESSOA   ' .format(i))
  nome = str(input('Nome: ')).strip()
  sexo = str(input('Sexo [M/F]: ')).strip()
  idade = int(input('Idade: '))
  somaidade += idade
  if i == 1 and sexo in 'Mm':
    maioridadehomem = idade
    homemmaisvelho = nome
  if sexo in 'Mm' and idade > maioridadehomem:
    maioridadehomem = idade
    homemmaisvelho = nome
  if sexo in 'Ff' and idade < 20:
    mulhermenos20 += 1

mediaidade = (somaidade / 4)

print('A média de idade do grupo cadastrado é {:.2f} anos.' .format(mediaidade))
print('O homem mais velho se chama {} e tem {} anos.' .format(homemmaisvelho, maioridadehomem))
print('Estão cadastradas {} mulheres com menos de 20 anos.' .format(mulhermenos20))


