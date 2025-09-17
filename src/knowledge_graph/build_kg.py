import argparse, json, yaml, networkx as nx, pathlib

def text_to_entities_relations(text: str):
    ents, rels = [], []
    if "goal:" in text.lower():
        ents.append(("Goal", "Improve Italian to B2"))
        rels.append(("User","has_goal","Improve Italian to B2"))
    if "project:" in text.lower():
        ents.append(("Project","Cognitive OS prototype"))
        rels.append(("User","works_on","Cognitive OS prototype"))
    return ents, rels

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--baseline", action="store_true")
    args = ap.parse_args()
    cfg = yaml.safe_load(open(args.config))

    data = json.load(open(cfg["data"]["input_json"]))

    # 1) Construire en MultiDiGraph
    G = nx.MultiDiGraph()
    G.add_node("User", type="Person")
    for note in data.get("notes", []):
        ents, rels = text_to_entities_relations(note["text"])
        for t, v in ents:
            G.add_node(v, type=t)
        for s, p, o in rels:
            # créer une clé d’arête unique
            G.add_edge(s, o, key=f"{s}|{p}|{o}", predicate=p)

    # 2) Dédupliquer → DiGraph simple (1 arête par (u,v))
    H = nx.DiGraph()
    for u, v, data in G.edges(data=True):
        if not H.has_edge(u, v):
            H.add_edge(u, v, **data)

    out = pathlib.Path("outputs/kg"); out.mkdir(parents=True, exist_ok=True)
    nx.write_graphml(H, out/"user_kg.graphml")  # propre pour Gephi
    nx.write_gexf(H, out/"user_kg.gexf")        # alternative Gephi

    print(f"Saved KG (dedup) to {out/'user_kg.graphml'} and {out/'user_kg.gexf'}")

if __name__ == "__main__":
    main()
