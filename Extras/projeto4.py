# Calculadora (mais bonita)

print("Bem-vindo(a) a calculadora! Por favor siga as instruções a seguir.")
n1 = float(input("Digite o primeiro número: "))
op = input("Digite a operação desejada (+, -, *, /, %, **, //): ")
n2 = float(input("Digite o segundo número: "))
resultado = None
if op == "+":
    resultado = n1 + n2
elif op == "-":
    resultado = n1 - n2
elif op == "*":
    resultado = n1 * n2
elif op == "/":
    if n2 == 0:
        print("Divisão por zero não é permitida.")
    else:
        resultado = n1 / n2 
elif op == "%":
    if n2 == 0:
        print("Divisão por zero não é permitida.")
    else:
        resultado = n1 % n2
elif op == "**":
    resultado = n1 ** n2
elif op == "//":
    if n2 == 0:
        print("Divisão por zero não é permitida.")
    else:
        resultado = n1 // n2
else:
    print("Operação inválida (ou ainda não aprendi a adicionar).")
if resultado is not None:
    print(f"Resultado: {resultado}")
else:
    print("Resultado não disponível devido a erro na operação.")