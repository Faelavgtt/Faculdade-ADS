# exercicio 26
# valorcompra = float (input ("Digite o valor do produto: "))
# venda = 0
# if valorcompra < 50.0 :
#     venda = (valorcompra * 0.45) + valorcompra
# else:
#     venda = (valorcompra * 0.3) + valorcompra
# print("O valor de venda é: ", venda)


# exercicio 28
# numint1 = int(input("Digite o primeiro número inteiro: "))
# numint2 = int(input("Digite o segundo número inteiro: "))
# numreal = float(input("Digite o número real: "))
# produto = numint1 * (numint2/2)
# soma = (numint1*3) + numreal
# cubo = numreal ** 3 
# print("O produto do primeiro com a metade do segundo é:", produto)
# print("A soma do triplo do primeiro com o terceiro é:", soma)
# print("O cubo do terceiro número é:", cubo)


# exercicio 29
# altura = float (input ("Digite a altura: "))
# sexo = input ("Digite o sexo sendo M para masculino e F para feminino! > ")
# if sexo == "M":
#     peso_ideal = (72.7 * altura) - 58
#     print ("O Peso ideal é: " , peso_ideal)
# elif sexo == "F":
#     peso_ideal = (62.1 * altura) - 44.7
#     print ("O peso ideal é: ", peso_ideal)
# else:
#     print ("Digite um sexo valido! Ou digite M para masculino ou digite F para feminino!")

# exercicio 30
# peixe=float(input("Digite o Kg do peixe: "))
# while peixe >50:
#     multa=((peixe-50)*4)
#     print("O valor da multa é: ", multa)
#     break
# else:
#     print("pagar somente o valor do peixe")

# exercicio 31
# per=str(input("Qual Turno Você estuda? M-Matutino, V-Vespertino, N-Noturno.\n"))
# if per == "M":
#     print("Bom dia!")
# elif per == "V":
#     print("Boa tarde!")
# elif per =="N":
#     print("Boa noite!")
# else:
#     print("Valor inválido")

# exercicio 32

# saque = int(input("Digite o Valor do Saque (R$ 10 a R$ 600): "))

# if saque < 10 or saque > 600:
#     print("Valor Inválido!")
# else:
#     valorRestante = saque
#     notas100 = valorRestante // 100
#     valorRestante = valorRestante % 100
#     notas50 = valorRestante // 50
#     valorRestante = valorRestante % 50
#     notas10 = valorRestante // 10
#     valorRestante = valorRestante % 10
#     notas5 = valorRestante // 5
#     valorRestante = valorRestante % 5
#     notas1 = valorRestante

#     print(f"Para sacar R$ {saque}, você receberá:")
#     if notas100 > 0:
#         print(f"{notas100} nota(s) de R$ 100")
#     if notas50 > 0:
#         print(f"{notas50} nota(s) de R$ 50")
#     if notas10 > 0:
#         print(f"{notas10} nota(s) de R$ 10")
#     if notas5 > 0:
#         print(f"{notas5} nota(s) de R$ 5")
#     if notas1 > 0:
#         print(f"{notas1} nota(s) de R$ 1")

# exercicio 33
# num1 = float(input("Digite o Primeiro Numero: "))
# num2 = float(input("Digite o Segundo Numero: "))
# print("\nEscolha a Operação:")
# print("1 - Adição (+)")
# print("2 - Subtração (-)")
# print("3 - Multiplicação (*)")
# print("4 - Divisão (/)")

# operacao = int(input("Digite o Numero da Operação Desejada: "))

# if operacao == 1:
#     resultado = num1 + num2
#     simbolo = "+"
# elif operacao == 2:
#     resultado = num1 - num2
#     simbolo = "-"
# elif operacao == 3:
#     resultado = num1 * num2
#     simbolo = "*"
# elif operacao == 4:
#     if num2 != 0:
#         resultado = num1 / num2
#         simbolo = "/"
#     else:
#         print("Erro: Divisão por Zero!")
#         resultado = None
# else:
#     print("Operação Inválida!")
#     resultado = None

# if resultado is not None:
#     print(f"\n{num1} {simbolo} {num2} = {resultado}")
#     if resultado % 2 == 0:
#         parImpar = "Par"
#     else:
#         parImpar = "impar"
#     if resultado > 0:
#         positivoNegativo = "Positivo"
#     elif resultado < 0:
#         positivoNegativo = "Negativo"
#     else:
#         positivoNegativo = "Neutro(Zero)"
#     if resultado == int(resultado):
#         inteiroDecimal = "Inteiro"
#     else:
#         inteiroDecimal = "Decimal"

#     print(f"O resultado é: {parImpar}, {positivoNegativo} e {inteiroDecimal}")

# exercicio 34
# litros = float(input("Digite a Quantidade de Litros: "))
# tipoCombustivel = input("Digite o Tipo de Combustível (A-Álcool, G-Gasolina): ").upper()

# precoAlcool = 1.90
# precoGasolina = 2.50

# if tipoCombustivel == "A":
#     # Álcool
#     precoTotal = litros * precoAlcool
#     if litros <= 20:
#         desconto = 3  
#     else:
#         desconto = 5  
#     combustivel_nome = "Álcool"
#     precoLitro = precoAlcool

# elif tipoCombustivel == "G":
#     # Gasolina
#     precoTotal = litros * precoGasolina
#     if litros <= 20:
#         desconto = 4  
#     else:
#         desconto = 6  
#     combustivel_nome = "Gasolina"
#     precoLitro = precoGasolina

# else:
#     print("Tipo de Combustível Invalido!")
#     precoTotal = 0
#     desconto = 0

# if tipoCombustivel in ["A", "G"]:
#     valorDesconto = precoTotal * (desconto / 100)
#     valorFinal = precoTotal - valorDesconto

#     print(f"Combustível: {combustivel_nome}")
#     print(f"Quantidade: {litros} litros")
#     print(f"Preço por Litro: R$ {precoLitro:.2f}")
#     print(f"Valor Sem Desconto: R$ {precoTotal:.2f}")
#     print(f"Desconto ({desconto}%): R$ {valorDesconto:.2f}")
#     print(f"Valor a Pagar: R$ {valorFinal:.2f}")

# exercicio 35
# print("Tipos de Carne Disponíveis:")
# print("1 - File Duplo")
# print("2 - Alcatra")
# print("3 - Picanha")

# tipoCarne = int(input("Digite o Numero do Tipo de Carne: "))
# quantidade = float(input("Digite a Quantidade em Kg: "))
# pagamento = input("Pagamento com Cartão? (S/N): ").upper()

# if tipoCarne == 1:
#     nomeCarne = "File Duplo"
#     if quantidade <= 5:
#         precoKg = 34.90
#     else:
#         precoKg = 35.80
# elif tipoCarne == 2:
#     nomeCarne = "Alcatra"
#     if quantidade <= 5:
#         precoKg = 44.90
#     else:
#         precoKg = 46.80
# elif tipoCarne == 3:
#     nomeCarne = "Picanha"
#     if quantidade <= 5:
#         precoKg = 66.90
#     else:
#         precoKg = 67.80
# else:
#     print("Tipo de Carne Inválido!")
#     nomeCarne = ""
#     precoKg = 0


# if nomeCarne != "":
#     precoTotal = quantidade * precoKg

    
#     if pagamento == "S":
#         desconto = precoTotal * 0.05  # 5% de desconto
#         tipoPagamento = "Cartão"
#     else:
#         desconto = 0
#         tipoPagamento = "Outros"

#     valorFinal = precoTotal - desconto

   
#     print("\n" + "="*40)
#     print("HIPERMERCADO")
#     print("CUPOM FISCAL")
#     print("="*40)
#     print(f"Tipo de Carne: {nomeCarne}")
#     print(f"Quantidade: {quantidade} kg")
#     print(f"Preço por Kg: R$ {precoKg:.2f}")
#     print(f"Preço Total: R$ {precoTotal:.2f}")
#     print(f"Tipo de Pagamento: {tipoPagamento}")
#     if desconto > 0:
#         print(f"Desconto (5%): R$ {desconto:.2f}")
#     else:
#         print("Desconto: R$ 0,00")
#     print(f"Valor a Pagar: R$ {valorFinal:.2f}")
#     print("="*40)

# exercicio 36
# codigoSanduiche = int(input("Digite o Codigo do Sanduiche: "))
# codigoBebida = int(input("Digite o Codigo da Bebida: "))

# if codigoSanduiche == 100:
#     precoSanduiche = 11.20
#     nomeSanduiche = "Cachorro Quente"
# elif codigoSanduiche == 101:
#     precoSanduiche = 8.30
#     nomeSanduiche = "Ovo Simples"
# elif codigoSanduiche == 102:
#     precoSanduiche = 11.50
#     nomeSanduiche = "Bauru com Ovo"
# elif codigoSanduiche == 103:
#     precoSanduiche = 16.20
#     nomeSanduiche = "Hambúrguer"


# if codigoBebida == 201:
#     precoBebida = 6.00
#     nomeBebida = "Refrigerante"
# elif codigoBebida == 202:
#     precoBebida = 7.50
#     nomeBebida = "Suco"
# elif codigoBebida == 203:
#     precoBebida = 4.70
#     nomeBebida = "Água Mineral"

# valorTotal = precoSanduiche + precoBebida

# print(f"Sanduíche: {nomeSanduiche} - R$ {precoSanduiche:.2f}")
# print(f"Bebida: {nomeBebida} - R$ {precoBebida:.2f}")
# print(f"Valor Total a Pagar: R$ {valorTotal:.2f}")

# exercicio 37
# qtidPaes = int(input("Digite a Quantidade de Pães Vendidos: "))
# qtidBroas = int(input("Digite a Quantidade de Broas Vendidas: "))


# precoPao = 1.00
# precoBroa = 3.50

# valorPaes = qtidPaes * precoPao
# valorBroas = qtidBroas * precoBroa
# totalArrecadado = valorPaes + valorBroas


# valorPoupanca = totalArrecadado * 0.10

# # Exibindo os Resultados
# print(f"\nRelatório de Vendas - Padaria Super Pão")
# print(f"Pães Franceses: {qtidPaes} x R$ {precoPao:.2f} = R$ {valorPaes:.2f}")
# print(f"Broas: {qtidBroas} x R$ {precoBroa:.2f} = R$ {valorBroas:.2f}")
# print(f"Total Arrecadado: R$ {totalArrecadado:.2f}")
# print(f"Valor para Poupança (10%): R$ {valorPoupanca:.2f}")

# exercicio 38
# refeicao = float(input("Digite o Peso da Refeição: "))

# preco = 59.00

# valor = refeicao * preco

# print(f"Peso da Refeição: {refeicao:.3f} kg")
# print(f"Preço por Kg: R$ {preco:.2f}")
# print(f"Valor a Pagar: R$ {valor:.2f}")

# exercicio 39
# dia = int(input("Digite o Dia: "))
# mes = int(input("Digite o Mês: "))

# diasCorridos = (mes - 1) * 30 + dia


# print(f"Data: {dia:02d}/{mes:02d}")
# print(f"Dias Decorridos desde o Início do Ano: {diasCorridos} dias")

# exercicio 40
# salario = 1200
# conta1 = 200
# conta2 = 120
# multaPercentual = 2  

# multaConta1 = conta1 * (multaPercentual / 100)
# multaConta2 = conta2 * (multaPercentual / 100)

# valorTotalConta1 = conta1 + multaConta1
# valorTotalConta2 = conta2 + multaConta2

# gastos = valorTotalConta1 + valorTotalConta2

# salarioFinal = salario - gastos

# # Exibindo os Resultados
# print(f"Salário de João: {salario:.2f}")
# print(f"Conta 1: {conta1:.2f} + Multa de 2% = {multaConta1:.2f} = {valorTotalConta1:.2f}")
# print(f"Conta 2: {conta2:.2f} + Multa de 2% = {multaConta2:.2f} = {valorTotalConta2:.2f}")
# print(f"Total de Gastos: {gastos:.2f}")
# print(f"Restará do Salário: {salarioFinal:.2f}")

# exercicio 41
# valorTotal = float(input("Digite o valor total da conta: "))

# maria = int(valorTotal // 3)
# gabriel = maria
# willian = round(valorTotal -(maria+gabriel), 2)

# print(f"Maria deve pagar: R${maria:.2f}\n Gabriel deve pagar: R$ {gabriel:.2f}\n willian deve pagar: R$ {willian:.2f}")

# exercicio 42
lata350ml = int(input("Quantidade de latas (350ml): "))
garrafa600ml = int(input("Quantidade de garrafas (600ml): "))
garrafa2l = int(input("Quantidade de garrafas (2L): "))

totalLitros = (lata350ml * 0.35) + (garrafa600ml * 0.6) + (garrafa2l * 2)

print(f"Total de litros comprados: {totalLitros:.2f}")