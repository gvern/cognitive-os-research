import argparse, json, yaml, networkx as nx, pathlib

def text_to_entities_relations(text: str):
    ents, rels = [], []
    if "goal:" in text.lower():
        ents.append(("Goal", "Improve Italian to B2"))
        rels.append(("User","has_goal","Improve Italian to B2"))
    if "project:" in text.lower():
        ents.append(("Project","Cognitive OS prototype"))
        rels.append(("Goal","supports","Cognitive OS prototype"))
    return ents, rels

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--baseline", action="store_true")
    args = ap.parse_args()
    cfg = yaml.safe_load(open(args.config))
    data = json.load(open(cfg["data"]["input_json"]))

    G = nx.MultiDiGraph(); G.add_node("User", type="Person")
    for note in data.get("notes", []):
        ents, rels = text_to_entities_relations(note["text"])
        for t, v in ents: G.add_node(v, type=t)
        for s,p,o in rels: G.add_edge(s,o, predicate=p)

    out = pathlib.Path("outputs/kg"); out.mkdir(parents=True, exist_ok=True)
    nx.write_graphml(G, out/"user_kg.graphml")
    print(f"Saved KG to {out/'user_kg.graphml'}")

if __name__ == "__main__":
    main()
