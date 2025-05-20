import math

def area_circulo(raio):
    area = math.pi * (raio ** 2)
    return area

area_raios = []

for i in range(3):
    raio = float(input(f"Digite o {i+1}° raio: "))
    raios = {
        'raio': raio
    }
    area_raios.append(raios)

for raios in area_raios:
    area = area_circulo(raios['raio'])
    print(f"Área do círculo com raio {raios['raio']}: {area:.2f}")