import textwrap

def menu():
    menu = """\n
    ============= MENU ===========        
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [7]\tListar Usuário
    [s]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR$ {valor:.2f}\n'
        print(f'depositado, saldo atual R${saldo}')
    else:
        print("O Deposito não pode ser menor que R$1,00")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saques:
        print('Voce só pode sacar 3 vezes no dia')
            
    elif excedeu_limite:
        print("O valor não pode ser maior que R$500,00")

    elif excedeu_saldo:
        print("Saldo insuficiente para este valor")

    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        print("\n-> Saque realizado com sucesso! <-")
    else:
        print("\n-> O valor informado é invalido <-")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n------------->EXTRATO<--------------")
    print("\nNão existe movimentação." if not extrato else extrato)
    print(f"\n            Saldo ->R${saldo:.2f}")
    print("--------------------------------------")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com este CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("-> Usuário cadastrado com sucesso <-")



def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None




def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n-> Conta criada com sucesso! <-")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, Conta NÃO criada! @@@")



def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            c/c:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def listar_usuario(usuarios):
    for usuario in usuarios:
        linha = f"""\
            Nome:\t{usuario['nome']}
            CPF:\t\t{usuario['cpf']}
            Endereço:\t{usuario['endereco']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    saldo = 0
    numero_saques = 0
    limite = 500
    extrato = ""

    while True:

        opcao = menu()

        if opcao == '1':  #deposito
            valor = float(input("Qual o valor do Deposito ->R$ "))

            saldo, extrato = depositar(saldo, valor, extrato)

            
        elif opcao == '2': #saque
            valor = float(input("Valor do saque ->R$ "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
                    

        elif opcao == '3':  #extrato
            exibir_extrato(saldo, extrato=extrato)


        
        elif opcao == "4": #criar conta
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)


        elif opcao == "5": #listar contas
            listar_contas(contas)



        elif opcao == "6": #criar usuario
            criar_usuario(usuarios)


        elif opcao == "7":
            listar_usuario(usuarios)


        elif opcao == 's': #sair
            break

        else:
            print("Opção Invalida, digite outra opção")


main()