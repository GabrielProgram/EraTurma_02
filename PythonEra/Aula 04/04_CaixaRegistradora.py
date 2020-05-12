# Curso de Python
# 2020/05/08

"""
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e
agora possui uma loja de conveniências. Faça um programa que implemente
uma caixa registradora rudimentar. O programa deverá receber um número
desconhecido de valores referentes aos preços das mercadorias. Um valor zero
deve ser informado pelo operador para indicar o final da compra. O programa
deve então mostrar o total da compra e perguntar o valor em dinheiro que o
cliente forneceu, para então calcular e mostrar o valor do troco. Após esta
operação, o programa deverá voltar ao ponto inicial, para registrar a próxima
compra.
"""

while True:
    print('\nType the prices of the products\n')

    N = 0
    Produto = 1
    Soma = 0

    Pagamento = 0
    Troco = 0

    while Produto != 0:
        N = N + 1

        while True:
            try:
                Produto = float(input("Produto: {}\n".format(N)))  # Ask teacher, how to add only up to 2 decimal numbers.
            except ValueError:
                print('Please insert a valid real number and try again.')
                continue
            else:
                break

        Soma = Produto + Soma

    print('The sum total: {:0.2f}'.format(Soma))

    while True: #Desnecessário.
        while True:
            try:
                Pagamento = float(input('What is the amount given by the client?\n'))
            except ValueError:
                print('Please insert a valid real number and try again.')
                continue
            else:
                break
        Troco = Pagamento - Soma
        if Troco < 0:
            print('The value given is smaller than the total value of the purchase, please ask for more money!\n')
            continue
        else:
            print('Amount of change for the client, RS: {:0.2f}'.format(Troco))
            break
