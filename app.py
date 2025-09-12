import os

restaurantes = [{'nome':'Burguer King', 'categoria':'Fast Food', 'ativo':True},
                {'nome':'Mc Donalds', 'categoria':'Fast Food', 'ativo':True},
                {'nome':'Subway', 'categoria':'Fast Food', 'ativo':False},
                {'nome':'Giraffas', 'categoria':'Fast Food', 'ativo':True},
                {'nome':'Pizza Hut', 'categoria':'Italiana', 'ativo':True}]

def voltar_menu_principal():
    input("Pressione qualquer tecla para voltar...")
    main()

def exibir_nome_do_programa():
    print('''
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n''')

def exibir_opcoes():
    print('1 - Cadastrar Restaurante')
    print('2 - Listar Restaurante')
    print('3 - Alterar Status do Restaurante')
    print('4 - Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o programa...')

def opcao_invalida():
    print('Opção inválida!')

    voltar_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '=' * len(texto)
    print(f'{linha}\n{texto}\n{linha}\n')

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de Novo Restaurante')
    nome_do_restaurante = input('Nome do Restaurante de deseja cadastrar: ')
    categoria = input(f'Categoria do Restaurante {nome_do_restaurante}: ')
    novo_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(novo_restaurante)
    print(f'\nRestaurante {nome_do_restaurante} cadastrado com sucesso!')

    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Lista de Restaurantes Cadastrados')

    print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        restaurante_ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'{nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {restaurante_ativo}')

    voltar_menu_principal()

def ativar_restaurante():
    exibir_subtitulo('Aletrar status do restaurante')
    nome_do_restaurante = input('Nome do Restaurante que deseja ativar ou desativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'].lower() == nome_do_restaurante.lower():
            restaurante['ativo'] = not restaurante['ativo']
            restaurante_encontrado = True
            mensagem = (f'\nRestaurante {nome_do_restaurante} ativado com sucesso!' if restaurante['ativo'] else f'\nRestaurante {nome_do_restaurante} foi desativado com sucesso!')
            print(mensagem)
        
    if not restaurante_encontrado:
        print(f'\nRestaurante {nome_do_restaurante} não encontrado!')

    voltar_menu_principal()



def escolher_opcao():

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            ativar_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
