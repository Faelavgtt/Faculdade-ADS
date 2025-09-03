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

nome = input("Digite o nome do aluno: ")
disciplina = input("Digite o nome da disciplina: ")
nota1 = float( input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
media = (nota1+nota2+nota3)/3


if media >= 6:
    print("-----------------------------")
    print("Nome:",nome,
      "\n--Notas--\n",
      "prova 1:",nota1,
      "\nprova 2:",nota2,
      "\nprova 3:",nota3,
      "\nMédia", media,
      "\nAprovado"
      )
    
else:
    print("-----------------------------")
    print("Nome:",nome,
      "\n--Notas--\n",
      "prova 1:",nota1,
      "\nprova 2:",nota2,
      "\nprova 3:",nota3,
      "\nMédia", media,
      "\nReprovado"
      )

