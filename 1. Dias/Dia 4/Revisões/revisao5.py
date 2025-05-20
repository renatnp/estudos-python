num = int(input("Digite um número: "))
for i in range(num + 1):  # Conta de 0 até o número digitado.
    if i % 3 == 0:        # Verifica se o número é múltiplo de 3.
        print(i)          # Se for, mostra na tela.