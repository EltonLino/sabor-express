'''
1 - Crie uma lista para cada informação a seguir:

Lista de números de 1 a 10;
Lista com quatro nomes;
Lista com o ano que você nasceu e o ano atual.
2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
'''

#Exercicio 01
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_nomes = ['Elton', 'Dayane', 'Cacau', 'Toddy']
lista_anos = [1992, 2025]
print(lista_numeros)
print(lista_nomes)
print(lista_anos)

#Exercicio 02
lista_times = ['São Paulo', 'Palmeiras', 'Corinthians', 'Santos']
for time in lista_times:
    print(time)

#Exercicio 03
impar = 0
soma = 0
for numero in lista_numeros:
    if numero % 2 != 0:
        impar = numero
        soma += impar

print(f'A soma dos números ímpares de 1 a 10 é: {soma}')

#Exercicio 04
for numero in range (10,0,-1):
    print(numero)

#Exercicio 05
num = int(input('Digite um número para ver a tabuada: '))
for i in range (1,11):
    print(f'{num} x {i} = {num*i}')

