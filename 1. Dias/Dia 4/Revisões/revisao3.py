nome1 = input("Digite o nome da primeira pessoa: ")
idade1 = int(input("Digite a idade da primeira pessoa: "))
nome2 = input("Digite o nome da segunda pessoa: ")
idade2 = int(input("Digite a idade da segunda pessoa: "))
if idade1 > idade2:
    print(f"{nome1} é mais velho(a) que {nome2}")
elif idade1 < idade2:
    print(f"{nome2} é mais velho(a) que {nome1}")
else:
    print(f"{nome1} e {nome2} têm a mesma idade.")
