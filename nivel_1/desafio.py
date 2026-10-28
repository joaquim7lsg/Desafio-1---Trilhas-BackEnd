# Desafio Python - Sistema PDV com descontos

print("Bem-vindo ao Sistema PDV com Descontos!")
funcao = print("Digite a opção desejada (1 - Compra, 2 - Relatório, 3 - Sair):")
valor_produto = float(input("Digite o valor do produto: "))
cliente_idade = int(input("Digite sua idade: "))

# Compra com Descontos
if funcao == 1:
 while True:
    if valor_produto < 0:
        print("Valor do produto inválido. Por favor, digite um valor positivo.")
        valor_produto = float(input("Digite o valor do produto: "))
    else:
        break
 while True:
    if cliente_idade < 0:
        print("Idade inválida. Por favor, digite um valor positivo.")
        cliente_idade = int(input("Digite sua idade: "))
    else:
        break
    
    
 while True:
    if cliente_idade <= 65:
        valor_desconto = valor_produto * 0.80
        valor_final = valor_desconto + valor_produto
        print("Você tem direito a um desconto de 20%. O valor final do produto é: R$", valor_final)
    elif valor_desconto > 100:
        print("Você tem direito a mais um desconto de 10%. O valor final do produto é: R$", valor_final * 0.10)
    else:
        print("O valor da sua compra é: R$", valor_produto)

 while True:
    if valor_produto = 0:
        print("Compras finalizadas. Obrigado por utilizar nosso Sistema PDV!")


''' compras.append({
        "valor produto": valor_produto,
        "desconto": valor_desconto,
        "valor_final": valor_final,
          print("Compra registrada com sucesso!")
    })'''

  
 # Finalizar a parte do historico e da lista
    
if funcao == 2:

    '''total_bruto = sum(compra["valor_bruto"] for compra in compras)
    total_descontos = sum(compra["desconto"] for compra in compras)
    total_final = sum(compra["valor_final"] for compra in compras)'''
      
    print("Relatório de Compras:")
    print("Quantidade de compras do dia:", len(compras))
    print("Total bruto das vendas: R$", total_bruto )
    print("Total de descontos concedidos:", total_descontos )
    print("Total Final (após descontos): R$", total_final )
elif funcao == 3:
    print("Saindo do Sistema PDV. Até logo!")
else:
    print("Opção inválida. Por favor, digite uma opção válida (1, 2 ou 3).")
