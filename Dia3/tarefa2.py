a = int(input("Olá! Digite um número: "))   # Pede ao usuário um número e converte para inteiro

# Contagem crescente usando for
for i in range(a + 1):                      # Conta de 0 até o número digitado (por isso o +1)
    print(f"Contando: {i}")                 # Mostra o valor de i a cada volta

# Contagem regressiva usando while
while a >= 0:                               # Enquanto 'a' for maior ou igual a 0
    print(f"Regredindo: {a}")               # Mostra o valor atual de 'a'
    a -= 1                                  # Diminui 1 do valor de
