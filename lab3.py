import networkx as nx

n = 70
p = 0.35

G = nx.erdos_renyi_graph(n, p)

avg_degree_graph = sum(dict(G.degree()).values()) / n

avg_degree_theory = (n - 1) * p

print(f"Средняя степень по графу:     {avg_degree_graph:.4f}")
print(f"Средняя степень по формуле:   {avg_degree_theory:.4f}")
print(f"Разница:                      {abs(avg_degree_graph - avg_degree_theory):.4f}")
