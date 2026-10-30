
print("Bem-vindo ao Sistema PDV com Descontos!")

historico_compras = []

while True:
    funcao = input(
        'Digite a opção desejada ("1" - Compra, "2" - Relatório, "3" - Sair): '
    )

    # Compra com descontos
    if funcao == "1":

        valor_produto = float(input("Digite o valor do produto: "))

        if valor_produto < 0:
            print("Valor do produto inválido. Digite um valor positivo.")
            continue

        if valor_produto == 0:
            print("Compras finalizadas.")
            continue

        cliente_idade = int(input("Digite sua idade: "))

        desconto = 0

        # Desconto de 20% para clientes com mais de 65 anos
        if cliente_idade > 65:
            desconto = 0.20

        # Desconto adicional de 10% para produtos acima de R$ 100
        if valor_produto > 100:
            desconto += 0.10

        valor_desconto = valor_produto * desconto
        valor_final = valor_produto - valor_desconto

        print("Valor do produto: R$", valor_produto)
        print("Desconto concedido: R$", valor_desconto)
        print("Valor final: R$", valor_final)

        historico_compras.append({
            "valor produto": valor_produto,
            "desconto": valor_desconto,
            "valor_final": valor_final
        })

    # Relatório de compras
    elif funcao == "2":

        if len(historico_compras) == 0:
            print("Nenhuma compra registrada ainda.")

        else:
            total_bruto = sum(
                compra["valor produto"] for compra in historico_compras
            )

            total_descontos = sum(
                compra["desconto"] for compra in historico_compras
            )

            total_final = sum(
                compra["valor_final"] for compra in historico_compras
            )

            print("\nRelatório de Compras:")
            print("Quantidade de compras:", len(historico_compras))
            print("Total bruto das vendas: R$", total_bruto)
            print("Total de descontos concedidos: R$", total_descontos)
            print("Total final após descontos: R$", total_final)

    # Sair do sistema
    elif funcao == "3":
        print("Saindo do Sistema PDV. Até logo!")
        break

    else:
        print("Opção inválida. Escolha 1, 2 ou 3.")
