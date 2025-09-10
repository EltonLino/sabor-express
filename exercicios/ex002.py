'''Exercícios
1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

Criança: 0 a 12 anos;
Adolescente: 13 a 18 anos;
Adulto: acima de 18 anos.
3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
Terceiro Quadrante: os valores de x e y devem ser menores que zero;
Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
Caso contrário: o ponto está localizado no eixo ou origem.
'''

# Exercicio 01
num = int(input('Digite um número: '))
if (num % 2 == 0):
    print(f'O número {num} é PAR')
else:
    print(f'O número {num} é IMPAR')

#Exercicio 02
idade = int(input('Digite sua idade: '))
if (idade <= 12):
    print(f'Com {idade} anos, você é uma Criança!')
elif (12 < idade <= 18):
    print(f'Com {idade} anos, você é um Adolescente!')
else:
    print(f'Com {idade} anos, você é um Adulto!')

#Exercício 03
usuario = 'Elton'
senha = int(123456)

resp_usuario = input('Digite o nome de Usuário: ')
resp_senha = int(input('Digite sua senha: '))

if (usuario == resp_usuario and senha == resp_senha):
    print('Login feito com sucesso!')
else:
    print('Usuário ou senha não correspondem, tente novamente!')

#Exercicio 04
x = int(input('Digite sua coordenada "X": '))
y = int(input('Digite sua coordenada "Y": '))

if (x > 0 and y > 0):
    print('Primeiro Quadrante')
elif (x < 0 and y > 0):
    print('Segundo Quadrante')
elif (x > 0 and y < 0):
    print('Terceiro Quadrante')
elif(x < 0 and y < 0):
    print('Quarto Quadrante')
else:
    print('Ponto localizado na Origem')
