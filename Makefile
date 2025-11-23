install:
	python3 -m venv .venv

project:
	python3 labyrinth_game/main.py

test:
	python3 -m pytest tests/ -v

# Команда для проверки кода Ruff
lint:
	ruff check .

# Автоисправление ошибок
lint-fix:
	ruff check --fix .

# Форматирование кода
format:
	ruff format .

# Команды для сборки (если понадобятся)
build:
	python3 setup.py sdist bdist_wheel

publish:
	twine check dist/*

package-install:
	pip install dist/*.whl

clean:
	rm -rf .venv
	rm -rf __pycache__
	rm -rf labyrinth_game/__pycache__
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info

# Умная активация venv
activate:
	@if [ -n "$$VIRTUAL_ENV" ]; then \
		echo "Виртуальное окружение уже активировано: $$VIRTUAL_ENV"; \
	else \
		echo "Для активации виртуального окружения выполните:"; \
		echo "source .venv/bin/activate"; \
		echo "Или:"; \
		echo "make activate-now"; \
	fi