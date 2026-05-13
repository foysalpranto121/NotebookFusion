import setuptools
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

VERSION = "0.0.1"
REPO_NAME = "NotebookFusion"
AUTHOR_USER_NAME = "foysalpranto121"
AUTHOR_EMAIL = "foysalpranto2002@gmail.com"
SRC_REPO = "NotebookFusion"

setuptools.setup(
    name=SRC_REPO,
    version=VERSION,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package for notebooks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)
