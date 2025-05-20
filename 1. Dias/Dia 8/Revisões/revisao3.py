grupo = []
for i in range(3):
    nome = input(f"Digite o {i+1}° nome: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    grupo.append([nome, idade])
for pessoa in grupo:
    print(type(pessoa))    # Vai mostrar <class 'list'>
    for dado in pessoa:
        print(type(dado))  # Vai mostrar <class 'str'> e <class 'int'>