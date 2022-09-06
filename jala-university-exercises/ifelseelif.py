# Autor: Hugo Edson de Souza
# Data: 06/09/2022 09:17
# Curso de Admissão - Turma 01

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def getData():
        nome = str(input("Nome: "))
        idade = int(input("Idade: "))
        peso = float(input("Peso: "))
        altura = float(input("Altura: "))
        return [nome, idade, peso, altura]
    
quantPessoas = int(input("Type the quantity of people you want to register: "))
pessoas = []

# Tentei aplicar todos os conceitos que já vimos até agora novamente para praticar.

for i in range(0, quantPessoas):
  pessoas.append(0)
  
for pessoa in pessoas:
    listData = Pessoa.getData()
    pessoas[pessoa] = Pessoa(listData[0], listData[1], listData[2], listData[3])

# Aqui eu aplico o conceito da aula, mais abaixo irei aprofundar utilizando elif.
for pessoa in pessoas:
    if pessoa.idade < 18:
        print(f"A pessoa: {pessoa.nome} é menor de idade !!!")
    elif pessoa.idade > 65:
        print(f"A pessoa: {pessoa.nome} é idosa !!!")
    elif pessoa.idade < 14:
        print(f"A pessoa: {pessoa.nome} é uma criança !!!")
    else:
        print(f"A pessoa: {pessoa.nome} é menor de idade ou adolescente !!!")
