.PHONY: bootstrap validate lint test docs format-check build clean

bootstrap:
	./scripts/bootstrap.sh

validate:
	docker build --tag exchange-interface-validator:local .
	docker run --rm exchange-interface-validator:local

lint:
	uv run ruff format --check scripts tests
	uv run ruff check scripts tests

test:
	uv run python -m unittest discover -s tests -v

docs:
	uvx --from zensical==0.0.74 zensical build --clean
	cp -R openapi schemas examples site/

format-check: lint

build:
	docker build --tag exchange-interface-validator:local .

clean:
	rm -rf .venv site
