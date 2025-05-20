def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

temperaturas = []
for i in range(3):
    temperatura = float(input(f"Digite a {i+1}° temperatura: "))
    transformar = {
        'temperatura': temperatura
    }
    print(" ")
    temperaturas.append(transformar)
print("Conversões:")
for temperatura in temperaturas:
    fahrenheit = celsius_para_fahrenheit(temperatura['temperatura'])
    print(f"Conversão da temperatura de Celsiu para Fahrenheit: {fahrenheit:.2f}°F")
    print(" ")