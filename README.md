# 🚀 NotebookFusion

![PyPI version](https://img.shields.io/pypi/v/NotebookFusion.svg)
![Python versions](https://img.shields.io/pypi/pyversions/NotebookFusion.svg)
![License](https://img.shields.io/pypi/l/NotebookFusion.svg)

**NotebookFusion** makes it easy to embed live websites and YouTube videos directly inside Jupyter Notebook, JupyterLab, Google Colab, and VS Code notebook outputs.

No more switching browser tabs while coding — keep documentation, tutorials, dashboards, and media next to your notebook cells.

---

## ✨ Features

- **Website Rendering** — Display live HTTPS websites inside notebook output cells using `IFrame`
- **YouTube Embedding** — Automatically embed YouTube videos from standard YouTube URLs
- **Customizable Viewport** — Control width and height for both website and video embeds
- **Lightweight** — Minimal dependencies using IPython display utilities
- **Notebook Friendly** — Works with Jupyter Notebook, JupyterLab, Google Colab, and VS Code Notebook

---

## 📦 Installation

```bash
pip install NotebookFusion
```

For development:

```bash
pip install -r requirements_dev.txt
```

---

## 🚀 Quick Start

### Embed a YouTube Video

```python
from NotebookFusion.youtube import render_youtube_video

render_youtube_video("https://www.youtube.com/watch?v=h25pePMdoPA&t=712s")
```

### Render a Website

```python
from NotebookFusion.site import render_site

render_site("https://www.python.org")
```

---

## ⚙️ Advanced Usage

### Custom Website Size

```python
from NotebookFusion.site import render_site

render_site(
    "https://www.python.org",
    width="100%",
    height="600"
)
```

### Custom YouTube Size

```python
from NotebookFusion.youtube import render_youtube_video

render_youtube_video(
    "https://www.youtube.com/watch?v=h25pePMdoPA",
    width=900,
    height=500
)
```

---

## 📚 Module Summary

- `NotebookFusion.site.render_site(URL, width='100%', height='600')`
- `NotebookFusion.youtube.render_youtube_video(url, width=780, height=440)`

---

## 🧠 Why NotebookFusion?

- Read documentation and tutorials inside notebooks
- Watch tutorials without leaving your code environment
- Embed dashboards and live websites for demos and teaching
- Improve interactive learning workflows

---

## 🖥️ Supported Platforms

| Platform | Supported |
| --- | --- |
| Jupyter Notebook | ✅ |
| JupyterLab | ✅ |
| Google Colab | ✅ |
| VS Code Notebook | ✅ |

---

## 📂 Project Structure

```text
NotebookFusion/
├── LICENSE
├── README.md
├── requirements.txt
├── requirements_dev.txt
├── setup.py
├── pyproject.toml
└── src/
    └── NotebookFusion/
        ├── __init__.py
        ├── custom_exception.py
        ├── logger.py
        ├── site.py
        └── youtube.py
```

---

## 🛠️ Development Setup

```bash
git clone https://github.com/foysalpranto121/NotebookFusion.git
cd NotebookFusion

conda create -n notebookfusion_env python=3.10 -y
conda activate notebookfusion_env

pip install -r requirements_dev.txt
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

MIT License

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
