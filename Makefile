.PHONY: run

run:
	@echo "Running..."
	@pipenv run python main.py

test:
	@echo "Testing..."
	@mypy .
	@pipenv run python -m unittest -v
