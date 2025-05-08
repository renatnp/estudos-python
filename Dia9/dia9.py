# 1. Usando "if" com dicionários:
carro = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2020
}
# Pode-se fazer testes com os valores das chaves.
if carro["ano"] >= 2020:
    print("Carro novo.")
else:
    print("Carro mais antigo.")

# 2. Verificando se uma chave existe no dicionário com "in":
if "marca" in carro:
    print("A chave 'marca' está presente!")

if "cor" not in carro:
    print("A chave 'cor' ainda não foi definida.")

# 3. Usando condição composta com os dados do dicionário:
aluno = {
    "nome": "João",
    "nota": 8.5,
    "frequência": 92
}
# Verifica se o aluno atende aos dois critérios para aprovação.
if aluno["nota"] >= 7 and aluno["frequência"] >= 75:
    print("Aprovado!")
else:
    print("Reprovado.")

# 4. Modificando o dicionário com base em condição:
# Adiciona a chave "situação" com o valor adequado de acordo com a nota.
if aluno["nota"] >= 7:
    aluno["situação"] = "Aprovado"
else:
    aluno["situação"] = "Reprovado"

print(aluno)

# 5. ".get()" em dicionários:
pessoa = {
    'nome': 'Ana',
    'idade': 30
}
# Acessar uma chave que não existe diretamente causaria erro:
# print(pessoa["cidade"])  # ERRO!

# Usando .get() com valor padrão:
print(pessoa.get("cidade", "Não informada"))  # saída: Não informada