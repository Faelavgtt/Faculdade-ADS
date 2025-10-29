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
# lata350ml = int(input("Quantidade de latas (350ml): "))
# garrafa600ml = int(input("Quantidade de garrafas (600ml): "))
# garrafa2l = int(input("Quantidade de garrafas (2L): "))

# totalLitros = (lata350ml * 0.35) + (garrafa600ml * 0.6) + (garrafa2l * 2)

# print(f"Total de litros comprados: {totalLitros:.2f}")

# exercicio 43
# moeda1 = int(input("Quantidade de moedas de 1 centavo: "))
# moeda5 = int(input("Quantidade de moedas de 5 centavos: "))
# moeda10 = int(input("Quantidade de moedas de 10 centavos: "))
# moeda25 = int(input("Quantidade de moedas de 25 centavos: "))
# moeda50 = int(input("Quantidade de moedas de 50 centavos: "))
# moeda1real = int(input("Quantidade de moedas de 1 real: "))

# totalReais = (
#     moeda1 * 0.01 +
#     moeda5 * 0.05 +
#     moeda10 * 0.10 +
#     moeda25 * 0.25 +
#     moeda50 * 0.50 +
#     moeda1real * 1.00
# )

# print(f"Valor total economizado: R$ {totalReais:.2f}")

# exercicio 44
# numero = int(input("Digite um número para ver sua tabuada: "))
# print(f"\nTabuada de {numero}:")
# i = 1
# while i <= 10:
#     print("{} x {} = {}".format(numero, i, numero * i))
#     i += 1


# exercicio 45
# nascimento = int(input("Digite o ano de nascimento: "))
# atual = int(input("Digite o ano atual: "))

# idade_anos = atual - nascimento

# idade_meses = idade_anos * 12
# idade_dias = idade_anos * 365  
# idade_semanas = idade_dias // 7

# print(f"\nIdade em anos: {idade_anos} anos")
# print(f"Idade em meses: {idade_meses} meses")
# print(f"Idade em dias: {idade_dias} dias")
# print(f"Idade em semanas: {idade_semanas} semanas")

# exericio 46
# nome = input("Digite o nome da pessoa: ").strip()
# sexo = input("Digite o sexo (M/F): ").strip().upper()
# estado_civil = input("Digite o estado civil: ").strip().upper()

# if sexo == "F" and estado_civil == "CASADA":
#     anos = int(input("Há quantos anos está casada? "))
#     msg = f"{nome} está casada há {anos} anos."
# else:
#     msg = f"{nome} não se enquadra na condição de mulher casada."

# print(msg)

# exercicio 47
# A = int(input("Digite o valor de A: "))
# B = int(input("Digite o valor de B: "))

# if A == B:
#     C = A + B
# else:
#     C = A * B

# print(f"O valor de C é: {C}")

# exercicio 48
# preco = float(input("Digite o preço do produto: R$ "))

# print("\nEscolha a condição de pagamento:")
# print("1 - À vista em dinheiro ou Pix (10% de desconto)")
# print("2 - À vista no cartão de crédito (5% de desconto)")
# print("3 - Em duas vezes (sem juros)")
# print("4 - Em três vezes (com 10% de juros)")

# codigo = int(input("Digite o código da condição de pagamento: "))

# if codigo == 1:
#     valor_final = preco * 0.90
#     print(f"Valor a pagar com 10% de desconto: R$ {valor_final:.2f}")
# elif codigo == 2:
#     valor_final = preco * 0.95
#     print(f"Valor a pagar com 5% de desconto: R$ {valor_final:.2f}")
# elif codigo == 3:
#     parcela = preco / 2
#     print(f"Pagamento em 2x de R$ {parcela:.2f} (sem juros)")
# elif codigo == 4:
#     valor_final = preco * 1.10
#     parcela = valor_final / 3
#     print(f"Pagamento em 3x de R$ {parcela:.2f} (com juros)")
#     print(f"Valor total com 10% de juros: R$ {valor_final:.2f}")
# else:
#     print("Código inválido. Tente novamente.")

# exercicio 49
# valor_dolar = float(input("Digite o valor em dólar (US$): "))

# cotacao = float(input("Digite a cotação do dólar (R$): "))

# valor_real = valor_dolar * cotacao

# print(f"Valor convertido em reais: R$ {valor_real:.2f}")

# exercicio 50
# numero = int(input("Digite um número inteiro: "))

# antecessor = numero - 1
# sucessor = numero + 1

# print(f"O antecessor de {numero} é {antecessor}")
# print(f"O sucessor de {numero} é {sucessor}")

# exercico 51
# soma = 0

# print("Digite os números (digite -999 para encerrar):")

# while True:
#     numero = int(input("Número: "))
#     if numero == -999:
#         break
#     soma += numero

# print(f"\nA soma dos números digitados é: {soma}")

# exercicio 52
# quantidade = 0

# print("Digite os números (digite -1 para encerrar):")

# while True:
#     numero = int(input("Número: "))
#     if numero == -1:
#         break
#     quantidade += 1

# print(f"\nQuantidade de números digitados: {quantidade}")

# exercicio 53
# quantidade_impares = 0

# print("Digite os números (digite 999 para encerrar):")

# while True:
#     numero = int(input("Número: "))
#     if numero == 999:
#         break
#     if numero % 2 != 0:
#         quantidade_impares += 1

# print(f"\nQuantidade de números ímpares digitados: {quantidade_impares}")

# exercicio 54
# contador_50 = 0

# print("Digite os números inteiros (digite 0 para encerrar):")

# while True:
#     numero = int(input("Número: "))
#     if numero == 0:
#         break
#     if numero == 50:
#         contador_50 += 1

# print(f"\nO número 50 foi digitado {contador_50} vezes.")

# exercicio 55
# numeros = []

# print("Digite 20 números:")

# for i in range(1, 21):
#     numero = int(input(f"Numero {i}: "))
#     numeros.append(numero)

# menor = min(numeros)
# maior = max(numeros)

# print(f"\nMenor número informado: {menor}")
# print(f"Maior número informado: {maior}")

# exercicio 56
# livros = int(input("Digite a quantidade de livros comprados no bimestre: "))

# if livros == 0:
#     pontos = 0
# elif livros == 1:
#     pontos = 5
# elif livros == 2:
#     pontos = 15
# elif livros == 3:
#     pontos = 30
# else:
#     pontos = 60

# print(f"\nPontos acumulados: {pontos}")

# if 20 <= pontos <= 30:
#     print("Brinde disponível: Uma Eco Bag OU Caneta personalizada")
# elif 35 <= pontos <= 60:
#     print("Brinde disponível: Um livro (até R$30,00) OU Luminária de cabeceira")
# elif pontos > 65:
#     print("Brinde disponível: 2 livros (até R$100,00) OU Power bank")
# else:
#     print("Nenhum brinde disponível neste bimestre.")

# exercicio 57
# cardapio = {
#     1: ("Bife acebolado", 15.00),
#     2: ("Lasanha", 25.00),
#     3: ("Frango grelhado", 18.50),
#     4: ("Peixe ao molho", 22.00),
#     5: ("Salada completa", 12.00),
#     6: ("Macarronada", 20.00)
# }

# print("===== CARDÁPIO =====")
# for codigo, (prato, preco) in cardapio.items():
#     print(f"{codigo} - {prato} - R$ {preco:.2f}")

# escolha = int(input("\nDigite o número do prato desejado: "))

# if escolha in cardapio:
#     prato_escolhido, preco = cardapio[escolha]
#     print(f"\nVocê escolheu: {prato_escolhido} - R$ {preco:.2f}")
    
#     gorjeta = input("Aceita pagar a gorjeta do garçom (10%)? (S/N): ").strip().upper()
    
#     if gorjeta == "S":
#         total = preco * 1.10
#         print(f"Valor final com gorjeta: R$ {total:.2f}")
#     else:
#         print(f"Valor final sem gorjeta: R$ {preco:.2f}")
# else:
#     print("Opção inválida. Por favor, escolha um prato do cardápio.")

# exercicio 59
# num1 = int(input("Digite o primeiro número inteiro: "))
# num2 = int(input("Digite o segundo número inteiro: "))

# inicio = min(num1, num2) + 1
# fim = max(num1, num2)

# if inicio >= fim:
#     print("Não há números inteiros entre os valores informados.")
# else:
#     print(f"Números inteiros entre {num1} e {num2}:")
#     for i in range(inicio, fim):
#         print(i)

# exercicio 60
# numero = int(input("Digite um número entre 1 e 10 para ver sua tabuada: "))

# if 1 <= numero <= 10:
#     print(f"\nTabuada de {numero}:")
#     for i in range(1, 11):
#         print(f"{numero} X {i} = {numero * i}")
# else:
#     print("Número inválido. Por favor, digite um número entre 1 e 10.")


# exercicio 61
# pares = 0
# impares = 0

# print("Digite 10 números inteiros:")

# for i in range(1, 11):
#     numero = int(input(f"Número {i}: "))
#     if numero % 2 == 0:
#         pares += 1
#     else:
#         impares += 1

# print(f"\nQuantidade de números pares: {pares}")
# print(f"Quantidade de números ímpares: {impares}")

# exercicio 62
# numero = int(input("Digite um número inteiro para calcular o fatorial: "))

# fatorial = 1

# for i in range(numero, 0, -1):
#     fatorial *= i

# print(f"\n{numero}! = ", end="")
# for i in range(numero, 0, -1):
#     print(f"{i}", end="." if i > 1 else f" = {fatorial}")

# exercicio 63
# qnt_n = int(input("Quantos números você deseja informar? "))

# numeros = []

# for i in range(qnt_n):
#     numero = float(input(f"Digite o {i+1}º número: "))
#     numeros.append(numero)

# menor = min(numeros)
# maior = max(numeros)
# soma = sum(numeros)

# print(f"\nMenor valor: {menor}")
# print(f"Maior valor: {maior}")
# print(f"Soma dos valores: {soma}")

# exercicio 64
# codigos = []
# veiculos = []
# acidentes = []

# for i in range(5):
#     print(f"\nCidade {i+1}:")
#     codigo = input("Código da cidade: ")
#     num_veiculos = int(input("Número de veículos de passeio (1999): "))
#     num_acidentes = int(input("Número de acidentes com vítimas (1999): "))
    
#     codigos.append(codigo)
#     veiculos.append(num_veiculos)
#     acidentes.append(num_acidentes)

# media_veiculos = sum(veiculos) / 5

# maior_acidente = max(acidentes)
# menor_acidente = min(acidentes)
# cidade_maior = codigos[acidentes.index(maior_acidente)]
# cidade_menor = codigos[acidentes.index(menor_acidente)]

# acidentes_menor_2000 = [
#     acidentes[i] for i in range(5) if veiculos[i] < 2000
# ]

# if acidentes_menor_2000:
#     media_acidentes_menor_2000 = sum(acidentes_menor_2000) / len(acidentes_menor_2000)
# else:
#     media_acidentes_menor_2000 = 0

# print("\n===== RESULTADOS =====")
# print(f"Média de veículos nas 5 cidades: {media_veiculos:.2f}")
# print(f"Maior índice de acidentes: {maior_acidente} (Cidade: {cidade_maior})")
# print(f"Menor índice de acidentes: {menor_acidente} (Cidade: {cidade_menor})")
# print(f"Média de acidentes nas cidades com menos de 2000 veículos: {media_acidentes_menor_2000:.2f}")

# exercicio 65
# valor_divida = float(input("Digite o valor da dívida: R$ "))

# tabela_juros = {
#     1: 0,
#     3: 10,
#     6: 15,
#     9: 20,
#     12: 25
# }

# print("\n{:<20} {:<20} {:<25} {:<20}".format("Valor da Dívida", "Valor dos Juros", "Quantidade de Parcelas", "Valor da Parcela"))
# print("-" * 85)

# for parcelas, juros in tabela_juros.items():
#     valor_juros = valor_divida * (juros / 100)
#     valor_total = valor_divida + valor_juros
#     valor_parcela = valor_total / parcelas
#     print("R$ {:<17.2f} R$ {:<17.2f} {:<25} R$ {:<17.2f}".format(valor_total, valor_juros, parcelas, valor_parcela))

# exercicio 66
# populacao_a = 80000
# populacao_b = 200000

# taxa_a = 0.03  # 3%
# taxa_b = 0.015  # 1.5%

# anos = 0

# while populacao_a <= populacao_b:
#     populacao_a += populacao_a * taxa_a
#     populacao_b += populacao_b * taxa_b
#     anos += 1

# print(f"Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a do país B.")
# print(f"População final de A: {int(populacao_a)} habitantes")
# print(f"População final de B: {int(populacao_b)} habitantes")

# exercicio 67
# while True:
#     usuario = input("Digite o nome de usuário: ")
#     senha = input("Digite a senha: ")

#     if senha == usuario:
#         print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.\n")
#     else:
#         print("Cadastro realizado com sucesso!")
#         break

# exercicio 68
# print("Números de 1 a 20 (um abaixo do outro):")
# for i in range(1, 21):
#     print(i)
# print("\nNúmeros de 1 a 20 (um ao lado do outro):")
# for i in range(1, 21):
#     print(i, end=" ")

# exercicio 69
# numeros = []
# soma = 0

# print("Digite 5 números:")

# for i in range(1, 6):
#     numero = float(input(f"Número {i}: "))
#     numeros.append(numero)
#     soma += numero

# media = soma / 5

# print(f"\nSoma dos números: {soma}")
# print(f"Média dos números: {media}")

# exercicio 70
# while True:
#     nome = input("\nDigite o nome do atleta (ou pressione Enter para encerrar): ")
#     if nome == "":
#         break

#     saltos = []
#     for i in range(1, 6):
#         distancia = float(input(f"{i}º salto: "))
#         saltos.append(distancia)

#     print(f"\nAtleta: {nome}")
#     print(f"Primeiro Salto: {saltos[0]} m")
#     print(f"Segundo Salto: {saltos[1]} m")
#     print(f"Terceiro Salto: {saltos[2]} m")
#     print(f"Quarto Salto: {saltos[3]} m")
#     print(f"Quinto Salto: {saltos[4]} m")

#     melhor = max(saltos)
#     pior = min(saltos)

#     saltos.remove(melhor)
#     saltos.remove(pior)

#     media = sum(saltos) / len(saltos)

#     print(f"\nMelhor salto: {melhor} m")
#     print(f"Pior salto: {pior} m")
#     print(f"Média dos demais saltos: {media:.1f} m")

# exercicio 71
# numero = input("Digite um número inteiro positivo: ")

# if numero.isdigit():
#     invertido = numero[::-1]
#     print(f"Número invertido: {invertido}")
# # else:
#     print("Entrada inválida. Por favor, digite apenas números inteiros positivos.")

# exercicio 72
# while True:
#     nome = input("\nDigite o nome do ginasta (ou pressione Enter para encerrar): ")
#     if nome == "":
#         break

#     notas = []
#     for i in range(1, 8):
#         nota = float(input(f"Nota {i}: "))
#         notas.append(nota)

#     print(f"\nAtleta: {nome}")
#     for i, nota in enumerate(notas, start=1):
#         print(f"Nota: {nota}")

#     melhor = max(notas)
#     pior = min(notas)

#     notas.remove(melhor)
#     notas.remove(pior)

#     media = sum(notas) / len(notas)

#     print("\nResultado final:")
#     print(f"Atleta: {nome}")
#     print(f"Melhor nota: {melhor}")
#     print(f"Pior nota: {pior}")
#     print(f"Média: {media:.2f}")

# exercicio 73
# candidatos = {
#     1: "Bruno",
#     2: "João",
#     3: "Rafaela",
#     4: "Ahmed"     
# }

# votos = {1: 0, 2: 0, 3: 0, 4: 0}
# nulos = 0
# brancos = 0
# total_votos = 0

# print("Digite os votos (1 a 4 para candidatos, 5 para nulo, 6 para branco, 0 para encerrar):")

# while True:
#     voto = int(input("Código do voto: "))
#     if voto == 0:
#         break
#     elif voto in votos:
#         votos[voto] += 1
#     elif voto == 5:
#         nulos += 1
#     elif voto == 6:
#         brancos += 1
#     else:
#         print("Código inválido. Tente novamente.")
#         continue
#     total_votos += 1

# print("\n===== RESULTADOS DA ELEIÇÃO =====")
# for codigo, nome in candidatos.items():
#     print(f"{nome}: {votos[codigo]} voto(s)")

# print(f"\nVotos nulos: {nulos}")
# print(f"Votos em branco: {brancos}")

# if total_votos > 0:
#     perc_nulos = (nulos / total_votos) * 100
#     perc_brancos = (brancos / total_votos) * 100
#     print(f"\nPercentual de votos nulos: {perc_nulos:.2f}%")
#     print(f"Percentual de votos em branco: {perc_brancos:.2f}%")
# else:
#     print("\nNenhum voto foi registrado.")


# exercicio 74
# numeros = []

# print("Digite 5 números inteiros:")
# for i in range(1, 6):
#     numero = int(input(f"Número {i}: "))
#     numeros.append(numero)

# print("\nNúmeros informados:")
# for num in numeros:
#     print(num)

# exercicio 75
# numeros = []

# print("Digite 10 números reais:")
# for i in range(1, 11):
#     numero = float(input(f"Número {i}: "))
#     numeros.append(numero)

# print("\nNúmeros na ordem inversa:")
# for num in reversed(numeros):
#     print(num)

# exercicio 76
# notas = []

# print("Digite 4 notas:")
# for i in range(1, 5):
#     nota = float(input(f"Nota {i}: "))
#     notas.append(nota)

# media = sum(notas) / len(notas)

# print("\nNotas informadas:")
# for i, nota in enumerate(notas, start=1):
#     print(f"Nota {i}: {nota}")

# print(f"\nMédia das notas: {media:.2f}")

# exercicio 77
# caracteres = []
# consoantes = []

# vogais = ['a', 'e', 'i', 'o', 'u']

# print("Digite 10 caracteres (letras):")
# for i in range(1, 11):
#     letra = input(f"Caractere {i}: ").lower()
#     caracteres.append(letra)
#     if letra.isalpha() and letra not in vogais:
#         consoantes.append(letra)

# print(f"\nQuantidade de consoantes lidas: {len(consoantes)}")
# print("Consoantes digitadas:")
# for c in consoantes:
    # print(c)

# exercico 78
# todos = []
# pares = []
# impares = []

# print("Digite 20 números inteiros:")

# for i in range(1, 21):
#     numero = int(input(f"Número {i}: "))
#     todos.append(numero)
#     if numero % 2 == 0:
#         pares.append(numero)
#     else:
#         impares.append(numero)

# print("\nVetor com todos os números:")
# print(todos)

# print("\nVetor com números pares:")
# print(pares)

# print("\nVetor com números ímpares:")
# print(impares)

# exercicio 79
# medias = []
# aprovados = 0

# for i in range(1, 11):
#     print(f"\nAluno {i}:")
#     soma = 0
#     for j in range(1, 5):
#         nota = float(input(f"Nota {j}: "))
#         soma += nota
#     media = soma / 4
#     medias.append(media)
#     if media >= 7.0:
#         aprovados += 1

# print("\nMédias dos alunos:")
# for i, media in enumerate(medias, start=1):
#     print(f"Aluno {i}: Média = {media:.2f}")

# print(f"\nNúmero de alunos com média maior ou igual a 7.0: {aprovados}")

# exercicio 80
# idades = []
# alturas = []

# print("Digite a idade e a altura de 5 pessoas:")
# for i in range(1, 6):
#     idade = int(input(f"Idade da pessoa {i}: "))
#     altura = float(input(f"Altura da pessoa {i} (em metros): "))
#     idades.append(idade)
#     alturas.append(altura)

# print("\nDados na ordem inversa:")
# for i in range(4, -1, -1):
#     print(f"Pessoa {5 - i}: Idade = {idades[i]}, Altura = {alturas[i]:.2f} m")