import os 
from pathlib import Path
import logging 
import shutil

logging.basicConfig(
    level=logging.INFO,
    format= "[%(asctime)s: %(levelname)s]: %(message)s"
    )


while True:
    project_name = input("Enter your project name: ")
    if project_name != "":
        break
    else:
        logging.info("Project name cannot be empty string. Please enter a valid project name.")



logging.info(f"Creating project by name: {project_name}")

# Remove previous generated structure
root = Path(".")
paths_to_remove = [root / '.github' / 'workflows', root / 'src' / project_name, root / 'tests']
for p in paths_to_remove:
    if p.exists():
        shutil.rmtree(p)
        logging.info(f"Removed directory: {p}")

files_to_remove = ['requirements.txt', 'setup.py', 'pyproject.toml', 'setup.cfg', 'tox.ini']
for f in files_to_remove:
    fp = root / f
    if fp.exists():
        fp.unlink()
        logging.info(f"Removed file: {f}")

# list of files:
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "requirements.txt",
    "setup.py",
    "pyproject.toml",
    'setup.cfg',
    "tox.ini"

]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as fp:
            pass
        logging.info(f"Created file: {filepath}")
