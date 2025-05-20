n = int(input("Digite um número inteiro: "))
while n > 0:             
    if n % 2 == 0:        
        print(f"{n} é par.")
    else:                 
        print(f"{n} é ímpar.")
    n -= 1                
if n == 0:
    print(n)