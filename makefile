DEFAULT: test

venv:
	python3 -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install pip pip-tools wheel

requirements.txt: venv requirements.in
	venv/bin/pip-compile

dev: requirements.txt
	venv/bin/pip-sync

test: dev
	venv/bin/pytest -sv

clean:
	rm -rf venv
