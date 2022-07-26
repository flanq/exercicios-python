 #Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o seu nome completo: ')).split()
print(f'Seu primeiro nome é {nome[0]} e seu útimo nome é {nome[-1]}.')