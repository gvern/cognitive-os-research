# Cognitive OS — Knowledge Modeling & Low‑Data Personalization

Research repo for two lines of work:
- **P‑A**: *User Knowledge Graphs for Personal Cognitive Systems*
- **P‑B**: *Low‑data Fine‑tuning for Personalized Cognitive Agents*

Quickstart:
```bash
conda env create -f environment.yml
conda activate cognitive-os
make reproduce_all
```

## 📄 Compile the papers

Prerequisites: a LaTeX distribution (TinyTeX/MacTeX/TeX Live). On macOS you can install TinyTeX via Homebrew:

```bash
brew install --cask tinytex
```

Build and open the PDFs (manual):

```bash
cd papers
pdflatex paper_PA.tex && open paper_PA.pdf
pdflatex paper_PB.tex && open paper_PB.pdf
```

Optional (with bibliography):

```bash
pdflatex paper_PA.tex && bibtex paper_PA || true && pdflatex paper_PA.tex && pdflatex paper_PA.tex
pdflatex paper_PB.tex && bibtex paper_PB || true && pdflatex paper_PB.tex && pdflatex paper_PB.tex
```

## 🛠️ Makefile targets

This repo provides a few helper targets for experiments and reports:

- `make baseline` — Build and evaluate a baseline KG (no incremental updates) using `config/kg.yaml`.
- `make experiments` — Run KG build/eval and fine-tuning/eval (LoRA) using configs in `config/`.
- `make eval` — Export result tables to `docs/tables/` (consumed by the LaTeX papers via `\input{}`).
- `make reproduce_all` — Run baseline + experiments + eval in sequence.
- `make viz` — Generate a simple KG visualization and open `docs/kg.png`.

Paper helpers:
- `make paper-pa` — Build `papers/paper_PA.pdf`.
- `make paper-pb` — Build `papers/paper_PB.pdf`.
- `make papers` — Build both papers.
- `make open-paper-pa` — Build then open PA.
- `make open-paper-pb` — Build then open PB.
- `make open-papers` — Build and open both.

Notes:
- Set a different Python with `PY=python` if needed, e.g., `make experiments PY=python`.
- See `docs/todo.md` for the writing checklist and expected figure/table filenames.
