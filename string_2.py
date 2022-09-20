nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"


print("Nome: %s Idade: %d" %(nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(nome, idade))
print("Nome: {nome} Idade: {idade}".format(nome = nome, idade = idade))
print(f"Nome: {nome} Idade: {idade}")