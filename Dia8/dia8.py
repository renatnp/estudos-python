# --- 1. Criando e acessando dicionários ---
pessoa = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "São Paulo"
}

print(pessoa)               # Mostra o dicionário completo.
print(pessoa["nome"])       # Acessa o valor da chave 'nome'.
print(pessoa["idade"])      # Acessa o valor da chave 'idade'.

# --- 2. Adicionando, alterando e removendo dados ---
pessoa["profissão"] = "Programadora"   # Adiciona nova chave e valor.
pessoa["idade"] = 26                   # Altera o valor da chave 'idade'.
del pessoa["cidade"]                   # Remove a chave 'cidade'.
print(pessoa)

# --- 3. Acessando chaves, valores e pares ---
print(pessoa.keys())     # Mostra todas as chaves.
print(pessoa.values())   # Mostra todos os valores.
print(pessoa.items())    # Mostra todos os pares (chave, valor).

# --- 4. Percorrendo um dicionário com for ---
# .items() retorna uma lista de tuplas (chave, valor).
# Usa-se duas variáveis para "desempacotar" cada par diretamente.
for chave, valor in pessoa.items():
    print(f"{chave} = {valor}")
"""
Obs.:
Se fosse usado apenas "for item in pessoa.items()", receberíamos cada tupla inteira:
('nome', 'Ana'), depois ('idade', 26), etc.

Mas usando: for chave, valor in pessoa.items():
estamos dizendo ao Python: “pegue cada tupla, separe o 1° elemento como 'chave' e o 2° como 'valor'”.
Isso torna o código mais legível e direto.
"""
# --- 5. Comparação com listas aninhadas ---
lista = ["Ana", 25]                       # Lista comum (posição importa)
dicionario = {"nome": "Ana", "idade": 25}  # Dicionário (mais claro e nomeado)

# --- 6. Lista com dicionários ---
# Pode-se armazenar vários dicionários dentro de uma lista.

cadastro = []  # Lista onde cada elemento será um dicionário (uma pessoa)

for i in range(3):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    cidade = input(f"Digite a cidade de {nome}: ")

    # Criamos um dicionário com os dados da pessoa
    pessoa = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    }

    # Adicionamos esse dicionário à lista
    cadastro.append(pessoa)

# Mostrando os dados:
print("\n--- Pessoas cadastradas ---")
for pessoa in cadastro:
    print(f"{pessoa['nome']} tem {pessoa['idade']} anos e mora em {pessoa['cidade']}.")
