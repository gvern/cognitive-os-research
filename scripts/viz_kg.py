import networkx as nx, matplotlib.pyplot as plt
from pathlib import Path

infile = Path("outputs/kg/user_kg.graphml")
outfile = Path("docs/kg.png")
outfile.parent.mkdir(parents=True, exist_ok=True)

G = nx.read_graphml(infile)
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(7,5), constrained_layout=True)
nx.draw(G, pos, with_labels=True, node_size=1200, font_size=8)
plt.savefig(outfile, dpi=200)
print(f"Saved {outfile}")
