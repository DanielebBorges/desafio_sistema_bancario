menu = """

[d] Deposito
[s] Sacar
[e] Extrato
[q] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
Limite_saques = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("insira o valor de deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! o valor informado é invalido.")

    elif opcao == "s":
         valor = float(input("insira o valor deo saque: "))
         excedeu_saldo = valor > saldo
         excedeu_limite = valor > limite
         excedeu_saques = numero_saques >= Limite_saques

         if excedeu_saldo:
             print("Operação falhou! você não tem saldo sufuciente.")
         elif excedeu_limite:
            print("Operação falhou! o valor do saque excede o limite.")
         elif excedeu_saques:
             print("Operação falhou! numero maximo de saues excedido.")
         elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1
         else: 
             print("Operação falhou! o valor informado é invalido.")    
       
    elif opcao == "e":
        print("\n===============EXTRATO===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=======================================")
        
    elif opcao == "q":
        break
    else:
        print("Operação invalida, por favor selecione novamnte a operação desejada")

