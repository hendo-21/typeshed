from typing import reveal_type

import networkx as nx


def main() -> None:
    g: nx.Graph[int] = nx.Graph()
    g.add_edge(1, 2, weight=1)
    g.add_edge(2, 3, weight=2)
    g.add_edge(1, 3, weight=3)

    tree = nx.minimum_spanning_tree(g)  # algorithms/tree/mst.pyi
    reveal_type(tree)
    for n in tree.nodes:
        n.upper()

    core = nx.k_core(g)  # algorithms/core.pyi
    reveal_type(core)
    for n in core.nodes:
        n.upper()

    comp = nx.complement(g)  # algorithms/operators/unary.pyi
    reveal_type(comp)
    for n in comp.nodes:
        n.upper()
