while True: # Repetição infinita.
    num1 = float(input("Digite o primeiro número: "))
    op = input("Digite a operação (+, -, *, /, **, //, %, ou 'sair' para encerrar): ")

    if op == "sair":
        print("Encerrando a calculadora...")
        break # Encerra o loop quando o usuário digita "sair".

    num2 = float(input("Digite o segundo número: "))

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        if num2 == 0:
            print("Divisão por 0 é inválida.")
        else:
            print(num1 / num2)
    elif op == "**":
        print(num1 ** num2)
    elif op == "//":
        if num2 == 0:
            print("Divisão por 0 é inválida.")
        else:
            print(num1 // num2)
    elif op == "%":
        if num2 == 0:
            print("Divisão por 0 é inválida.")
        else:
            print(num1 % num2)
    else:
        print("Operação inválida.")
