MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Digite a sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Idade insuficiente para tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Idade insuficiente para tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode realizar aulas teóricas.")
else:
    print("Idade insuficiente para tirar a CNH.")