def calcular_desconto(preco, desconto):
    valor_do_desconto = preco * (desconto / 100)
    return preco - valor_do_desconto

p1 = calcular_desconto(100, 10)
p2 = calcular_desconto(50, 20)
p3 = calcular_desconto(80, 15)

print("Produto 1 com desconto:", p1)
print("Produto 2 com desconto:", p2)
print("Produto 3 com desconto:", p3)
