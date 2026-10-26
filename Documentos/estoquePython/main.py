from menus import menu
from menus import menu_estoque
import menu_funções

menu()

func = int(input('Qual função deseja usar: '))

while func != 0:

    if func == 9:
        menu()
        func = int(input('Qual função deseja usar: '))

    if func == 1:
        menu_funções.cadastro()
        enter = input('[Aperte enter para voltar ao menu:] ')

        if enter == '':
            func = 9

    elif func == 2:
        menu_funções.remover()
        enter = input('[Aperte enter para voltar ao menu:] ')
        
        if enter == '':
            func = 9

    elif func == 3:
        menu_funções.lista()
        menuEstoque = input('[Deseja acessar o menu de estoque? [s/n]: ').strip().upper()

        if menuEstoque == 'N':
            enter = input('[Aperte enter para voltar ao menu:] ')
            
            if enter == '':
                func = 9
                
    
        while menuEstoque == 'S':
            menu_estoque()
            funcEstoque = int(input('Qual função deseja usar: '))


            if funcEstoque == 1:
                print(f'{'='*39}')
                menu_funções.somaEstoque()
                enter = (input('[Aperte enter para voltar ao menu do estoque]'))
                if enter == '':
                    menuEstoque = 'S'
            elif funcEstoque == 2:
                print(f'{'='*39}')
                menu_funções.separarPreco()
                enter = (input('[Aperte enter para voltar ao menu do estoque]'))
                if enter == '':
                    menuEstoque = 'S'
            elif funcEstoque == 3:
                print(f'{'='*39}')
                menu_funções.separarQuantidade()
                enter = (input('[Aperte enter para voltar ao menu do estoque]'))
                if enter == '':
                    menuEstoque = 'S'
            elif funcEstoque == 0:
                func = 9
                menuEstoque = 'N'

    elif func == 0:
        break