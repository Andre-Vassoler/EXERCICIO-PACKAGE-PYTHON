# EXERCICIO
"""
Aumente os preços dos produtos a seguir em 10%
gere novos produtos poor deep copy (cópia profunda)
"""
"""
Ordene os produtos por nome decrescente( do maior para o menor)
Gere os produtos ordenados por nome por deep copy (cópia profunda)

Ordene os produtos por preço crescente (do menor para o maior)
Gere os produtos ordenados por preço por deep copy (cópia profunda)
"""
import copy

from package5 import produtos

novos_produtos = [
    {**p, "preco": round(p["preco"] * 1.10, 2)}
    for p in copy.deepcopy(produtos)
]

produtos_ordenados_por_nome_decrescente = sorted(
    copy.deepcopy(novos_produtos),
    key = lambda p: p["nome"], reverse=True
)

produtos_ordenados_por_numero = sorted(
    copy.deepcopy(novos_produtos),
    key = lambda p: p["preco"]
)

def imprimi(lista):
    for item in lista:
        print(f'{item["nome"]}: {item["preco"]}')
    print("")

print()
imprimi(produtos)
imprimi(novos_produtos)
imprimi(produtos_ordenados_por_nome_decrescente)
imprimi(produtos_ordenados_por_numero)