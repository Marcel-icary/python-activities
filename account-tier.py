nivel = ["basic", "silver", "gold", "platinum"]
porcentagens = {"basic": 30, "silver": 20, "gold": 10, "platinum": 5}

valor_total = float(input("Informe o valor total de faturamento: "))

opcao = -1
while opcao!=5:
    print("1 - nível basic\n2 - nível silver\n3 - nível gold\n4 - nível platinum\n5 - sair")
    opcao = int(input("Informe o nível de assinatura: "))
    if opcao in [1,2,3,4]:
        nivel_escolhido = nivel[opcao-1]
        porcentagem = porcentagens[nivel_escolhido]
        faturamento = valor_total * (porcentagem / 100)
        print(f"O faturamento da nossa empresa no nível {nivel_escolhido} é de R$ {faturamento:.2f}")
    elif opcao == 5:
        print("Encerrando o programa.")
    else:
        print("Opção inválida. Tente novamente.")
