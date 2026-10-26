from dados import estoque, salvar

'''==============================================================================
=============================FUNÇÕES DO MENU=====================================
=============================================================================='''

def cadastro():
    produto = input('Digite o nome do produto a ser cadastrado: ')
    preco = float(input('Digite o preço do produto: '))
    quantidade = int(input('Qual a quantidade: '))

    for itens in estoque:
        if itens['Produto'] == produto:
            itens['Quantidade'] = quantidade
            itens['Preço'] = preco
            print('Produto Atualizado.')
            break

    else:
        estoque.append({
                        'Produto': produto,
                        'Preço': preco, 
                        'Quantidade': quantidade
                        })

        print('Produto Cadastrado.')

    salvar()


def remover():
    produto = input('Digite o produto que deseja remover: ')

    for item in estoque:
        if item['Produto'] == produto:
            estoque.remove(item)
            print('Produto Removido.')
            salvar()
            break
    else:
        print('Produto Não Encontrado.')


def lista():
    print('='*37)
    print(f'{'|Produto':.<19.19}|{'Qtd':.>8.8}|{'Preço|':.>8.8}')
    print('='*37)
    for item in estoque:
        print(f"|{item['Produto']:.<18.18}|{item['Quantidade']:.>8}|{item['Preço']:.>7.2f}|")
    print('='*37)


'''==============================================================================
=========================FUNÇÕES DO MENU DE TABELA===============================
=============================================================================='''

def somaEstoque():

    soma = 0

    for i in range(len(estoque)):
        preço = estoque[i]['Preço']
        quantidade = estoque[i]['Quantidade']

        acumulador = preço * quantidade
        soma += acumulador

    print(f'O valor do estoque é de: [{soma:.2f}]')



def separarPreco():

    valorMinimo = float(input('Digite o valor minimo: '))
    valorMaximo = float(input('Digite o valor maximo: '))

    separados = []

    for i in range(len(estoque)):
        itens = estoque[i]['Preço']

        if itens >= valorMinimo and itens <= valorMaximo:
            separados.append({
                            'Produto': estoque[i]['Produto'],
                            'Quantidade': estoque[i]['Quantidade'],
                            'Preço': estoque[i]['Preço']
            })

    listaSeparada = sorted(separados, key=lambda item: item['Preço'])

    print('='*37)
    print(f'{'|Produto':.<19.19}|{'Qtd':.>8.8}|{'Preço|':.>8.8}')
    print('='*37)
    for item in listaSeparada:
        print(f"|{item['Produto']:.<18.18}|{item['Quantidade']:.>8}|{item['Preço']:.>7.2f}|")
    print('='*37)

    listaSeparada.clear()
    separados.clear()

def separarQuantidade():

    listaOrdenada = sorted(estoque, key=lambda item: item['Quantidade'])

    print('='*37)
    print(f'{'|Produto':.<19.19}|{'Qtd':.>8.8}|{'Preço|':.>8.8}')
    print('='*37)
    for item in listaOrdenada:
        print(f"|{item['Produto']:.<18.18}|{item['Quantidade']:.>8}|{item['Preço']:.>7.2f}|")
    print('='*37)

    listaOrdenada.clear()
