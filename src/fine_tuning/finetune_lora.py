import argparse, yaml, pathlib
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    args = ap.parse_args()
    cfg = yaml.safe_load(open(args.config))
    out = pathlib.Path(cfg["train"]["save_dir"]); out.mkdir(parents=True, exist_ok=True)
    (out/'adapter.safetensors').write_bytes(b'FAKE')
    print(f"Saved adapter to {out/'adapter.safetensors'}")
if __name__ == "__main__":
    main()
