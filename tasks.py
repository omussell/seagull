from invoke import tasks
from pathlib import Path

py_ver = '3.6'
venv_path = Path.home().joinpath('venv')
env_vars = { 
        'PATH': f"{venv_path}",
        'PIPENV_VENV_IN_PROJECT': 'YES'
        }

@task
def venv_create(c):
    if not venv_path.is_file():
        c.run(f"python{py_ver} -m venv {venv_path")

@task
def pip_clean(c):
    c.run(f"pipenv clean", env=env_vars)

@task:
def pip_install(c):
    c.run(f"pipenv install --deploy --sequential", env=env_vars)

@task(venv_create,pip_install)
def build(c):
    pass
