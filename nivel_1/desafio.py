# Desafio Python - Sistema PDV com descontos

print("Bem-vindo ao Sistema PDV com Descontos!")
funcao = print("Digite a opção desejada (1 - Compra, 2 - Relatório, 3 - Sair):")
valor_produto = float(input("Digite o valor do produto: "))
cliente_idade = int(input("Digite sua idade: "))

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
        print("Você tem direito a um desconto de 20%. O valor final do produto é: R$", valor_desconto)
    elif valor_desconto > 100:
        print("Você tem direito a mais um desconto de 10%. O valor final do produto é: R$", valor_desconto * 0.10)
    else:
        print("O valor da sua compra é: R$", valor_produto)

 while True:
    if valor_produto = 0:
        print("Compras finalizadas. Obrigado por utilizar nosso Sistema PDV!")
    

