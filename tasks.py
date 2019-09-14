from invoke import tasks
from pathlib import Path

py_ver = '3.6'
venv_path = Path.home().joinpath('venv')

@task
def venv_create(c):
    if not venv_path.is_file():
        c.run(f"python{py_ver} -m venv {venv_path")

@task
def pip_clean(c):
    c.run(f"pipenv clean")

@task:
def pip_install(c):
    c.run(f"pipenv install --deploy --sequential")

@task(venv_create,pip_install)
def build(c):
    pass
