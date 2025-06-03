import os
from invoke import task

@task
def ensure_submodule(c, path="airoh"):
    if not os.path.exists(path) or not os.path.exists(os.path.join(path, ".git")):
        c.run(f"git submodule update --init --recursive {path}")
    else:
        c.run(f"git submodule update --remote {path}")

@task
def install_local(c, path="airoh"):
    c.run(f"pip install -e {path}")

@task
def setup(c):
    """
    Setup all the requirements.
    """
    ensure_submodule(c, "airoh")
    install_local(c, "airoh")
    from airoh.utils import setup_env_python
    setup_env_python(c, "requirements.txt")
    print(f"✨ Setup complete!")

@task
def fetch(c):
    """
    Retrieve all data assets.
    """
    from airoh.datalad import import_file
    import_file(c, "papers")
