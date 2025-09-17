PY ?= python3
LATEX ?= pdflatex

.PHONY: baseline experiments eval reproduce_all viz

baseline:
	$(PY) -m src.knowledge_graph.build_kg --config config/kg.yaml --baseline
	$(PY) -m src.knowledge_graph.eval_kg --config config/kg.yaml --baseline

experiments:
	$(PY) -m src.knowledge_graph.build_kg --config config/kg.yaml
	$(PY) -m src.knowledge_graph.eval_kg --config config/kg.yaml
	$(PY) -m src.fine_tuning.finetune_lora --config config/ft_lora.yaml
	$(PY) -m src.fine_tuning.eval_ft --config config/ft_eval.yaml

eval:
	$(PY) experiments/export_tables.py --out docs/tables

reproduce_all: baseline experiments eval
	@echo "All done."

viz:
	$(PY) scripts/viz_kg.py
	@open docs/kg.png || true

# --- Paper build helpers ---
.PHONY: paper-pa paper-pb papers open-paper-pa open-paper-pb open-papers

paper-pa:
	@cd papers && $(LATEX) -interaction=nonstopmode paper_PA.tex >/dev/null

paper-pb:
	@cd papers && $(LATEX) -interaction=nonstopmode paper_PB.tex >/dev/null

papers: paper-pa paper-pb

open-paper-pa: paper-pa
	@cd papers && open paper_PA.pdf || true

open-paper-pb: paper-pb
	@cd papers && open paper_PB.pdf || true

open-papers: open-paper-pa open-paper-pb
