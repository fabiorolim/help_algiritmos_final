from funcoes import *
from menu import menu

while True:
    menu()
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        matricula = int(input('Informe a matricula: '))
        nome = input('Informe o nome: ')
        cadastrar(matricula, nome)
    elif opcao == 2:
        mostrar_todos()
    elif opcao == 3:
        exit()

fechar_conexao()
