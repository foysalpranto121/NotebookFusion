import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

_version = "0.0.3"
REPO_NAME = "NotebookFusion"
AUTHOR_USER_NAME = "foysalpranto121"
AUTHOR_EMAIL = "foysalpranto2002@gmail.com"
SRC_REPO = "NotebookFusion"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package for enhanced Jupyter notebook functionality.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        "ensure>=1.0.2",
        "py-youtube>=1.1.7",
    ],
    python_requires=">=3.8",
)