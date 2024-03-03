# Lista para armazenar os itens
itens = []

# TODO: Solicite os itens ao usuário

for i in range(0, 3):
    item_nome = str(input())
    itens.append(item_nome)

# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")