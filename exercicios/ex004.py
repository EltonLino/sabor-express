'''
Exercícios
1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

2 - Utilizando o dicionário criado no item 1:

Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário.
3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.

4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
'''
# Exercício 1
dados_usuario = [{'nome': 'Elton', 'idade': 32, 'cidade': 'São José dos Campos'}]
for dado in dados_usuario:
    print(f'Nome: {dado['nome']}\nIdade: {dado['idade']}\nCidade: {dado['cidade']}\n')

# Exercício 2
for dado in dados_usuario:
    # Modificando a idade
    dado['idade'] = 30
    print(f'Idade atualizada: {dado['idade']}')

    # Adicionando profissão
    dado['profissão'] = 'Desenvolvedor'
    print(f'Profissão adicionada: {dado['profissão']}')
    dado['RG'] = '123456789-0'
    print(f'RG adicionado: {dado['RG']}\n')

    # Removendo cidade
    del dado['cidade']
    print(f'Dados após remoção da cidade:\n')
    for key, value in dado.items():
        print(f'{key}: {value}')

# Exercício 3
quadrados = {num: num**2 for num in range(1, 6)}
for num, quadrado in quadrados.items():
    print(f'O quadrado de {num} é {quadrado}')

# Exercício 4
pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

# Exercício 5
frase = "A vida é bela e a vida é cheia de surpresas"
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)