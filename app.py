import os

restaurantes = ['Pizza Hut', 'McDonalds', 'Burger King']

def voltar_menu_principal():
    input("Pressione qualqeur tecla para voltar...")
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
    print('3 - Ativar Restaurante')
    print('4 - Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o programa...')

def opcao_invalida():
    print('Opção inválida!')

    voltar_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(f'{texto}\n')

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de Novo Restaurante')
    nome_do_restaurante = input('Nome do Restaurante de deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'\nRestaurante {nome_do_restaurante} cadastrado com sucesso!')

    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Lista de Restaurantes Cadastrados')
    for restaurante in restaurantes:
        print(f' ~ {restaurante}')

    voltar_menu_principal()



def escolher_opcao():

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar Restaurante')
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
