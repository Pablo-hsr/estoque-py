from dados import estoque, salvar

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