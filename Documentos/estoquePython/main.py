from menus import menu
import menu_funções

menu()

func = int(input('Qual função deseja usar: '))

backmenu = 'N'

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
        enter = input('[Aperte enter para voltar ao menu:] ')
    
        if enter == '':
            func = 9

    elif func == 0:
        break