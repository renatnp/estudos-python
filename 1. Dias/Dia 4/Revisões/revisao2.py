num1 = float(input("Digite seu primeiro número: "))
num2 = float(input("Digite seu segundo número: "))
op = input("Escolha sua operação (+ - * / // % **): ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 == 0:
        print("Divisão por zero não é permitida.")
    else:
        print(num1 / num2)
elif op == "//":
    if num2 == 0:
        print("Divisão por zero não é permitida.")
    else:
        print(num1 // num2)
elif op == "%":
    if num2 == 0:
        print("Divisão por zero não é permitida.")
    else:
        print(num1 % num2)
elif op == "**":
    print(num1 ** num2)
else:
    print("Operação inválida")