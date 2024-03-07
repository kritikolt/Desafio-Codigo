capacidade_atual, aumento_percentual = map(int, input().split())

# TODO: Calcule a nova capacidade do disco de Mithril

nova_capacidade = capacidade_atual + int((capacidade_atual / 100 * aumento_percentual))

# TODO: Imprima a nova capacidade

print(nova_capacidade)