#Crie um programa que leia o nome de uma cidade e verifica se ela começa o nome "SANTO" ou não

cidade = str(input('Digite o nome da sua ciadade: ')).strip()
print(cidade[:5].lower() == 'santo')