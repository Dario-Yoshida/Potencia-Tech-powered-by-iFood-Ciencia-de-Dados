'''3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha
 saldo em conta, o sistema deve exibir uma mensagem informando que não será possível 
 sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma 
 variável e exibidos na operação de extrato.'''

#depósito, saque e extrato

deposito = []
saque = []
saldo = 0
numero_saque = 1
limite = 500
extrato = ""

menu = """          MENU         
        1 - Deposito
        2 - Saque
        3 - Extrato
        s - Sair
        """

while True:

    opcao = input(menu)

    if opcao == '1':  #deposito
        valor_deposito = int(input("Qual o valor do Deposito ->R$ "))
        if valor_deposito < 1:
            print("O Deposito não pode ser menor que R$1,00")
        else:
            deposito.append(valor_deposito)
            saldo += valor_deposito
            extrato += f'Deposito R${valor_deposito:.2f}\n'
            print(f'depositado, saldo atual R${saldo}')

    elif opcao == '2': #saque
        print(f'saque {numero_saque}')
        if numero_saque > 3:
            print('Voce só pode sacar 3 vezes no dia')
        else:
            valor_saque = int(input("Valor do saque ->R$ "))
            if valor_saque > limite:
                print("O valor não pode ser maior que R$500,00")
            elif saldo - valor_saque < 0:
                print("Saldo insuficiente para este valor")
            else:
                saque.append(valor_saque)
                saldo -= valor_saque
                numero_saque += 1
                extrato += f'Saque    R${valor_saque:.2f}\n'
                

    elif opcao == '3':  #extrato
        print("\n------------->EXTRATO<--------------")
        print("\nNão existe movimentação." if not extrato else extrato)
        print(f"\n            Saldo ->R${saldo:.2f}")
        print("--------------------------------------")

    elif opcao == 's':
        break

    else:
        print("Opção Invalida, digite outra opção")