# Exercicio 1
# nome = input("digite o nome: ")
# idade = int(input("digite a idade: "))
# sexo = input("digite o sexo: ")
# endereco = input("digite o endereço: ")
# telefone = int(input("digite a telefone: "))

# print("nome:",nome,
#       "\nidade:",idade,
#       "\nsexo:",sexo,
#       "\nendereço:",endereco,
#       "\ntelefone:",telefone
#       )

# Exercicio 2

# nome = input("Digite o nome do aluno: ")
# nota1 = float( input("Digite a nota do 1 bimestre: "))
# nota2 = float(input("Digite a nota do 2 bimestre: "))
# nota3 = float(input("Digite a nota do 3 bimestre: "))
# nota4 = float(input("Digite a nota do 4 bimestre: "))

# print("-----------------------------")
# print("Nome:",nome,
#       "\n--Notas--\n",
#       "Bimestre 1:",nota1,
#       "\nBimestre 2:",nota2,
#       "\nBimestre 3:",nota3,
#       "\nBimestre 4:",nota4,
#       )

# # Exercicio 3
# nome = input("Digite o nome: ")
# titulo = int(input("Digite o titulo: "))
# candidato = int(input("Digite o numero do candidato: "))

# print(
#     "nome: ",nome,
#     "\ntitulo: ",titulo,
#     "\ncandidato: ",candidato,
#       )

# Exercicio 4

# nome = input("Digite o nome: ")
# placa = int(input("Digite a placa: "))
# modelo = input("Digite a placa do carro: ")
# cor = input("Digite a cor do carro: ")

# print(
#     "nome: ",nome,
#     "\nplaca: ",placa,
#     "\nmodelo: ",modelo,
#     "\ncor: ",cor,
#       )

# Exercicio 5
# nome = input("Digite o nome do aluno: ")
# disciplina = input("Digite o nome da disciplina: ")
# nota1 = float( input("Digite a nota 1: "))
# nota2 = float(input("Digite a nota 2: "))
# nota3 = float(input("Digite a nota 3: "))

# print("-----------------------------")
# print("Nome:",nome,
#       "\n--Notas--\n",
#       "prova 1:",nota1,
#       "\nprova 2:",nota2,
#       "\nprova 3:",nota3,
#       "Média",(nota1+nota2+nota3)/3
#       )

# exercicio 6

# base = float(input("Digite a base: "))
# altura = float(input("Digite a altura: "))

# print("o resultado é:", base*altura)

# # exercicio 7
# base = float(input("Digite a base: "))
# altura = float(input("Digite a altura: "))

# print("o resultado é:", (base*altura)/2)

# # exercicio 8
# distacia = float(input("Digite a distancia em Km: "))
# consumo = float(input("Digite o consumo por km do veiculo: "))
# combustivel = float(input("Digite o valor do combustivel: "))

# calculo = (distacia/consumo)*combustivel

# print("O custo total da viagem é: ", calculo)

# exercicio 9

# nome = input("Digite o nome do aluno: ")
# disciplina = input("Digite o nome da disciplina: ")
# nota1 = float( input("Digite a nota 1: "))
# nota2 = float(input("Digite a nota 2: "))
# nota3 = float(input("Digite a nota 3: "))
# media = (nota1+nota2+nota3)/3


# if media >= 6:
#     print("-----------------------------")
#     print("Nome:",nome,
#       "\n--Notas--\n",
#       "prova 1:",nota1,
#       "\nprova 2:",nota2,
#       "\nprova 3:",nota3,
#       "\nMédia", media,
#       "\nAprovado"
#       )
    
# else:
#     print("-----------------------------")
#     print("Nome:",nome,
#       "\n--Notas--\n",
#       "prova 1:",nota1,
#       "\nprova 2:",nota2,
#       "\nprova 3:",nota3,
#       "\nMédia", media,
#       "\nReprovado"
#       )

# exercicio 10
# try:
#     num = int(input("digite um número: "))
#     if num <10:
#         print("numero menor que 10")
#     elif num >10:
#         print("numero maior que 10")
#     elif num == 10:
#         print("numero igual a 10")
#     else:
#         print("digite um numero.")
# except ValueError:
#     print("Digite um numero inteiro!")

# exercicio 11
# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))

# if idade >= 0 and idade <= 12: 
# 	print(nome,"Criança")
# elif idade >=13 and idade <= 17:
# 	print(nome,"Adolescente")
# elif idade >=18 and idade <= 59:
# 	print(nome,"Adulto")
# elif idade >= 60:
# 	print(nome,"Velho")

# exercicio 12
# numero = float(input("Digite seu numero: "))
# if numero > 0:
#   print("O numero e positivo.")
# elif numero < 0:
#   print("O numero e negativo.")
# else:
#    print("O numero e zero.")

# exercicio 13
# numero = int(input("Digite um numero: "))

# if numero % 2 == 0: 
#     print("Par")
# else: 
#     print("Impar")

# exercicio 14
# conta = input("Número da conta: ")
# saldo = float(input("Saldo: "))
# debito = float(input("Débito: "))
# credito = float(input("Crédito: "))

# saldo_atual = saldo - debito + credito

# print(f"Saldo atual: R$ {saldo_atual:.2f}")

# if saldo_atual >= 0:
#     print("Saldo Positivo")
# else:
#     print("Saldo Negativo")

# exercicio 15
# letra = input("Digite 'F' para feminino ou 'M' para masculino: ").upper()

# if letra == "F":
#     print("Feminino")
# elif letra == "M":
#     print("Masculino")
# else:
#     print("Sexo Inválido")

# exercicio 16
# n1 = float(input("Digite o primeiro número: "))
# n2 = float(input("Digite o segundo número: "))
# n3 = float(input("Digite o terceiro número: "))

# maior = max(n1, n2, n3)
# menor = min(n1, n2, n3)

# print(f"Maior número: {maior}")
# print(f"Menor número: {menor}")

# exercicio 17
# salario = float(input("Digite o salário atual: "))

# if salario <= 280:
#     aumento = 0.20
# elif salario <= 700:
#     aumento = 0.15
# elif salario <= 1500:
#     aumento = 0.10
# else:
#     aumento = 0.05

# valor_aumento = salario * aumento
# novo_salario = salario + valor_aumento

# print(f"Salário antes do reajuste: R$ {salario:.2f}")
# print(f"Percentual de aumento: {aumento * 100}%")
# print(f"Valor do aumento: R$ {valor_aumento:.2f}")
# print(f"Novo salário: R$ {novo_salario:.2f}")

# exercicio 18
# valor_hora = float(input("Valor da hora: "))
# horas_trabalhadas = float(input("Horas trabalhadas no mês: "))

# salario_bruto = valor_hora * horas_trabalhadas

# # IR
# if salario_bruto <= 900:
#     ir = 0
# elif salario_bruto <= 1500:
#     ir = salario_bruto * 0.05
# elif salario_bruto <= 2500:
#     ir = salario_bruto * 0.10
# else:
#     ir = salario_bruto * 0.20

# inss = salario_bruto * 0.10
# fgts = salario_bruto * 0.11
# total_descontos = ir + inss
# salario_liquido = salario_bruto - total_descontos

# print(f"Salário Bruto: R$ {salario_bruto:.2f}")
# print(f"(-) IR: R$ {ir:.2f}")
# print(f"(-) INSS: R$ {inss:.2f}")
# print(f"FGTS: R$ {fgts:.2f}")
# print(f"Total de Descontos: R$ {total_descontos:.2f}")
# print(f"Salário Líquido: R$ {salario_liquido:.2f}")

# exercicio 19
# a = float(input("Lado A: "))
# b = float(input("Lado B: "))
# c = float(input("Lado C: "))

# if a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print("Triângulo Equilátero")
#     elif a == b or a == c or b == c:
#         print("Triângulo Isósceles")
#     else:
#         print("Triângulo Escaleno")
# else:
#     print("Os lados não formam um triângulo.")

# exercicio 20
# ano = int(input("Digite o ano: "))

# if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#     print("Ano bissexto")
# else:
#     print("Ano não bissexto")

# exercicio 21
# salario_fixo = float(input("Salário fixo: "))
# vendas = float(input("Valor total das vendas: "))

# comissao = vendas * 0.04
# salario_final = salario_fixo + comissao

# print(f"Comissão: R$ {comissao:.2f}")
# print(f"Salário final: R$ {salario_final:.2f}")

# exercicio 22
# preco = float(input("Preço do produto: "))
# novo_preco = preco * 0.90

# print(f"Novo preço com desconto: R$ {novo_preco:.2f}")

# exercicio 23
# qtd_frangos = int(input("Quantidade de frangos: "))
# custo_chip = 4.00
# custo_anel = 3.50

# total = qtd_frangos * (custo_chip + 2 * custo_anel)
# print(f"Gasto total da granja: R$ {total:.2f}")

# exercicio 24
# qtd_sanduiches = int(input("Quantidade de sanduíches: "))

# queijo = (2 * 50 * qtd_sanduiches) / 1000  # em kg
# presunto = (50 * qtd_sanduiches) / 1000
# carne = (100 * qtd_sanduiches) / 1000

# print(f"Queijo: {queijo:.2f} kg")
# print(f"Presunto: {presunto:.2f} kg")
# print(f"Carne: {carne:.2f} kg")

# exercicio 25
# pequenas = int(input("Quantidade de camisetas pequenas: "))
# medias = int(input("Quantidade de camisetas médias: "))
# grandes = int(input("Quantidade de camisetas grandes: "))

# total = (pequenas * 10) + (medias * 12) + (grandes * 15)
# print(f"Valor total da compra: R$ {total:.2f}")