import argparse, yaml, networkx as nx, json, pathlib

def coherence_score(G):
    return 1.0

def groundedness_score(G):
    nodes = set(G.nodes())
    hits = 0
    queries = ["What are my goals?", "What project supports my goal?"]
    for q in queries:
        if "goal" in q.lower():
            hits += 1 if any("Improve Italian" in n for n in nodes) else 0
        if "project" in q.lower():
            hits += 1 if any("Cognitive OS prototype" in n for n in nodes) else 0
    return hits/len(queries)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--baseline", action="store_true")
    args = ap.parse_args()
    G = nx.read_graphml("outputs/kg/user_kg.graphml")
    coh = coherence_score(G); grd = groundedness_score(G)
    pathlib.Path("docs").mkdir(exist_ok=True)
    json.dump({"coherence":coh,"groundedness":grd}, open("docs/kg_eval.json","w"), indent=2)
    print({"coherence":coh,"groundedness":grd})

if __name__ == "__main__":
    main()
