# Desafio Python - Sistema PDV com descontos
# Este programa simula um caixa de loja com menu de compras,
# relatório de vendas e regras simples de desconto.

# Lista para guardar todas as compras registradas.
compras = []


def validar_valor_produto():
    """Solicita e valida o valor do produto antes de continuar."""
    while True:
        valor = float(input("Digite o valor do produto: "))
        if valor > 0:
            return valor
        print("Valor do produto inválido. Digite um valor maior que zero.")


def validar_idade():
    """Solicita e valida a idade do cliente."""
    while True:
        idade = int(input("Digite a idade do cliente: "))
        if idade >= 0:
            return idade
        print("Idade inválida. Digite uma idade maior ou igual a zero.")


def registrar_compra():
    """Processa uma compra, aplica descontos e salva o registro."""
    # Recebe e valida os dados da compra.
    valor_produto = validar_valor_produto()
    cliente_idade = validar_idade()

    # Regra de desconto: clientes até 65 anos recebem 20% de desconto.
    # Clientes com compra acima de R$ 100 recebem 10% de desconto adicional.
    if cliente_idade <= 65:
        percentual_desconto = 0.20
    elif valor_produto > 100:
        percentual_desconto = 0.10
    else:
        percentual_desconto = 0

    valor_desconto = valor_produto * percentual_desconto
    valor_final = valor_produto - valor_desconto

    # Exibe o resultado da compra para o cliente.
    if percentual_desconto > 0:
        print(
            f"Você recebeu um desconto de {percentual_desconto * 100:.0f}%. "
            f"O valor final é: R$ {valor_final:.2f}"
        )
    else:
        print(f"O valor da sua compra é: R$ {valor_produto:.2f}")

    # Guarda a compra para o relatório final.
    compras.append(
        {
            "valor_bruto": valor_produto,
            "desconto": valor_desconto,
            "valor_final": valor_final,
        }
    )
    print("Compra registrada com sucesso!")


def exibir_relatorio():
    """Mostra o total de compras, descontos e valor final do dia."""
    if not compras:
        print("Nenhuma compra foi registrada até o momento.")
        return

    total_bruto = sum(compra["valor_bruto"] for compra in compras)
    total_descontos = sum(compra["desconto"] for compra in compras)
    total_final = sum(compra["valor_final"] for compra in compras)

    print("\nRelatório de Compras:")
    print(f"Quantidade de compras do dia: {len(compras)}")
    print(f"Total bruto das vendas: R$ {total_bruto:.2f}")
    print(f"Total de descontos concedidos: R$ {total_descontos:.2f}")
    print(f"Total final após descontos: R$ {total_final:.2f}")


# Menu principal do sistema.
print("Bem-vindo ao Sistema PDV com Descontos!")

while True:
    # Exibe as opções disponíveis para o usuário.
    print("\nDigite a opção desejada:")
    print("1 - Compra")
    print("2 - Relatório")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        registrar_compra()
    elif opcao == "2":
        exibir_relatorio()
    elif opcao == "3":
        print("Saindo do Sistema PDV. Até logo!")
        break
    else:
        print("Opção inválida. Digite uma opção válida (1, 2 ou 3).")
