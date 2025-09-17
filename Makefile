.PHONY: baseline experiments eval reproduce_all
baseline:
	python -m src.knowledge_graph.build_kg --config config/kg.yaml --baseline
	python -m src.knowledge_graph.eval_kg --config config/kg.yaml --baseline

experiments:
	python -m src.knowledge_graph.build_kg --config config/kg.yaml
	python -m src.knowledge_graph.eval_kg --config config/kg.yaml
	python -m src.fine_tuning.finetune_lora --config config/ft_lora.yaml
	python -m src.fine_tuning.eval_ft --config config/ft_eval.yaml

eval:
	python experiments/export_tables.py --out docs/tables

reproduce_all: baseline experiments eval
