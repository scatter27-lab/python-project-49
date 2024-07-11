install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

flake8:
	poetry run flake8

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pipx install dist/*.whl

lint:
	poetry run flake8 brain_games
