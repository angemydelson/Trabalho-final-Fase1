# Esses dois variáveis são as variáveis global. Nprodutos é uma lista. Produto é um dicionário 
Nprodutos = []
produto = dict()

# Essa função é pra fazer uma tabela e deixar tudo bem arrumadinho. Cadastro, Atualizações etc. 
def tabela(prod,Nprod):
    
    print('-'*80)
    print('Numeracão     ', end='')
    for i in prod.keys():
        print(f'{i:<15}', end='')
    print()
    for k, v in enumerate(Nprod):
        print(f'{k:>4}          ' , end='')
        for d in v.values():
            print(f'{str(d):<15}', end='')
        print()
    print('-'*80)


# Parte 1. Eu fiz essa função é para cadastrar os produtos. Lá no final eu chamei a função tabela para deixar tudo arrumadinho.
def cadastrar_produto():
    print('Bem vindo à nossa caixa.\nAqui voçê pode fazer o cadastro dos produtos.')
    while True:
        produto = {}
        produto['Nome'] = str(input('Digite o nome do produto: '))
        produto['Codigo'] = int(input('Digite o código do produto: '))
        produto['Preco'] = float(input('Digite o preço do produto: '))
        produto['QuantidadeEMestoque'] = int(input('Digite a quantidade em estoque do produto: '))
        Nprodutos.append(produto)   
        while True:
            pergunta = str(input('Quer fazer mais um cadastro? [S/N] ')).upper()[0]
            if pergunta in 'SN':
                break
            print("Erro! Responda apenas S ou N")
        if pergunta == 'N':
                break
    print('-=' * 40)
    print('-=' * 40)

    # Aqui eu chamei a função tabela
    tabela(produto,Nprodutos)


# Parte 2. Essa função é para atualizar produtos. Nessa função é permitido fazer várias atualizações.
def atualizar_produto():
    if not Nprodutos :
        print('Nao tem produtos cadastrados')
    else:

        while True:
            print('Aqui voçê pode fazer a atualização dos produtos.\nSó segue as etapas.\nDica: Só digitar "s" se quiser continuar e "n" para parar.')
            codigo = int(input('Digite o código do produto: '))
            Found = False 
            for prod in Nprodutos:
                if prod['Codigo'] == codigo:
                    preco = float(input('Informe o novo preço: '))
                    quantidade = int(input('Informe a nova quantidade: '))
                    prod['Preco'] = preco 
                    prod['QuantidadeEMestoque'] = quantidade 
                    Found = True
            if not Found:
                print('Produto não foi encontrado. Por favor, digite o codigo córreto do produto.')
            while True:
                pergunta = str(input('Quer fazer mais uma atualização? [S/N] ')).upper()[0]
                if pergunta in 'SN':
                    break
                print("Erro! Responda apenas S ou N")
            if pergunta == 'N':
                    break

        print('=-'*40)


        # Aqui eu chamei a função tabela
        tabela(produto,Nprodutos)


# Parte 3. Eu fiz essa função para registrar as compras. No final vai aparecer na tela o cupom das compras com o valor total a pagar.
#  E é permitido fazer várias compras.
def registrar_compra():
    if not Nprodutos :
        print('Nao tem produtos cadastrados')
    else:

        print('Aqui é para fazer comprar.\nPode ficar á vontade.')
        vetorprecoTotal = []    # Esse vetor vai receber o preço total de cada compra.
        vetorprodutocomprado=[]  # Esse vetor vai receber um dicionário de cada produto comprado.
        dicprodutocomprado = dict() # Esse dicionário vai receber as informações e a quantidade de um produto comprado.
        while True:
            precoTotal=0 # Essa variáviel vai receber o preço total de um produto.
            codigocompra = int(input('Digite o código do produto ou "-1" para passar essa etapa: '))
            Found = False
            if codigocompra == -1:
                break
            for prod in Nprodutos:
                if prod['Codigo'] == codigocompra:
                    quantidadeparacomprar = int(input('Quanto que deseja comprar? :'))
                    if quantidadeparacomprar <= prod['QuantidadeEMestoque']:
                        prod['QuantidadeEMestoque'] -= quantidadeparacomprar
                        precoTotal += prod['Preco'] * quantidadeparacomprar
                        vetorprecoTotal.append(precoTotal)
                        print('A sua compra foi realizada')
                        dicprodutocomprado = {}
                        dicprodutocomprado['Nome'] = prod['Nome']
                        dicprodutocomprado['Codigo'] = prod['Codigo']
                        dicprodutocomprado['Preco'] = prod['Preco']
                        dicprodutocomprado['Quantidade'] = quantidadeparacomprar
                        vetorprodutocomprado.append(dicprodutocomprado)
                        Found = True
                    else:
                        print('Infelizmente, a sua compra não foi realizada. Nos não temos essa quantidade, só tem ',prod['QuantidadeEMestoque'] ,'no estoque.')
                        break
            if not Found:
                print('Produto não foi encontrado. Por favor, digite um codigo correto do produto.')
            
        totalcompra = 0   # Essa variável é para somar o valor total de cada compra.
        #print(vetorprecoTotal)
        for i in vetorprecoTotal:
            totalcompra += i
        print('O cupom da sua compra.')
        # Aqui eu só chamei a função.
        tabela(dicprodutocomprado,vetorprodutocomprado)
        print('Total:',totalcompra)
        print('=-'*40)


# Parte 4. Eu fiz essa função para fazer a consulta de um produto ou várias produtos no estoque.
def consultar_produto():
    if not Nprodutos :
        print('Nao tem produtos cadastrados')
    else:
        print('-=' * 40)
        while True:
            print('Aqui é para fazer a busca de um produto.\nFique a vontade.')
            verificador = False
            buscarcodigo = int(input('Digite o código do produto que voçê deseja buscar: '))
            for prod in Nprodutos:
                if buscarcodigo == prod['Codigo']:
                    # Esse for é para dar um print bem arrumadinho
                    print('-'*80)
                    for k , w in prod.items():
                        print(f'{k} = {w}; ', end = '')
                verificador = True
            if not verificador :
                print('Infelizmente! Codigo nao foi cadastrado.')
            while True:
                pergunta = str(input('Quer fazer mais uma consulta? [S/N] ')).upper()[0]
                if pergunta in 'SN':
                    break
                print("Erro! Responda apenas S ou N")
            if pergunta == 'N':
                    break

        print('-=' * 40)



#Parte 5. Essa parte do código é o relatório final de produtos. Eu só chamei a função tabela
def relatorio_produto():
    if not Nprodutos : 
        print('Nao tem produtos cadastrados')
    else:
        print('Relatório de produtos')
        tabela(produto,Nprodutos)

        
# Essa parte do código é o Menu. Ela permite ou acesso das diferentes partes do código.
# Eu faço a chamada de uma função depende da escolha do usuário.
def main():
    print('-='*40)
    print()
    print('------ Bem vindo á nossa platatorma! ------')
    print()
    print('---------------SUPERDEL TECH---------------')
    print()
    while True:
        print()
        print('1- Cadastrar novos produtos')
        print()
        print('2- Atualizar produto')
        print()
        print('3- Registrar compras')
        print()
        print('4- Consultar produto')
        print()
        print('5- Relatório de produto')
        print()
        print('0- Para sair')
        print()
        entrada = int(input('Por favor! Escolha uma opção: '))
        print()
        if entrada == 1:
            cadastrar_produto()
        elif entrada == 2:
            atualizar_produto()
        elif entrada == 3:
            registrar_compra()
        elif entrada == 4:
            consultar_produto()
        elif entrada == 5:
            relatorio_produto()
        elif entrada == 0:
            print('Obrigado! Volte sempre.')
            break
        else:
            print('Não tem essa opção. Por favor digite uma das opções abaixo')
            print()
    print('-='*40)

main()





    





