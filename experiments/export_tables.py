import argparse, json, pathlib, pandas as pd
def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--out', required=True); args = ap.parse_args()
    out = pathlib.Path(args.out); out.mkdir(parents=True, exist_ok=True)
    kg = json.load(open('docs/kg_eval.json')) if pathlib.Path('docs/kg_eval.json').exists() else {}
    ft = json.load(open('docs/ft_eval_report.json')) if pathlib.Path('docs/ft_eval_report.json').exists() else {}
    pd.DataFrame([{**{"coherence": None, "groundedness": None, "alignment_score": None, "forgetting_index": None}, **kg, **ft}]).to_csv(out/'summary.csv', index=False)
    print(f"Wrote {out/'summary.csv'}")
if __name__ == '__main__':
    main()
