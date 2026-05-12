# NotebookFusion  🚀


![PyPI version](https://img.shields.io/pypi/v/NotebookFusion.svg)
![Python versions](https://img.shields.io/pypi/pyversions/NotebookFusion.svg)
![License](https://img.shields.io/pypi/l/NotebookFusion.svg)

NotebookFusion is a lightweight Python package that allows you to seamlessly render live websites and embed YouTube videos directly inside Jupyter Notebooks, JupyterLab, and Google Colab environments.

No more switching browser tabs while coding — view documentation, tutorials, dashboards, or videos right beside your notebook cells.

---

# ✨ Features

- 🌐 **Website Rendering**  
  Display live HTTPS websites directly inside notebook output cells.

- ▶️ **YouTube Video Embedding**  
  Automatically parse and embed YouTube videos from standard URLs.

- 📏 **Customizable Viewport**  
  Easily adjust width and height.

- ⚡ **Lightweight & Fast**  
  Built using standard IPython display utilities with minimal dependencies.

- 📓 **Notebook Friendly**
  - Jupyter Notebook
  - JupyterLab
  - Google Colab
  - VS Code Notebook

---

# 📦 Installation

Install via pip:

```bash
pip install NotebookFusion


```bash 
pip install -r requirements_dev.txt

---

# 🚀 Quick Start

## ▶️ Render a YouTube Video

```python
from NotebookFusion.youtube import render_youtube_video

render_youtube_video(
    "https://www.youtube.com/watch?v=h25pePMdoPA&t=712s"
)
```

---

## 🌐 Render a Website

```python
from NotebookFusion.site import render_site

render_site("https://www.google.com")
```

---

# ⚙️ Advanced Usage

## Custom Width & Height

```python
from NotebookFusion.site import render_site

render_site(
    "https://www.python.org",
    width="100%",
    height="600px"
)
```

---

## Embed YouTube with Custom Size

```python
from NotebookFusion.youtube import render_youtube_video

render_youtube_video(
    "https://www.youtube.com/watch?v=h25pePMdoPA",
    width="900",
    height="500"
)
```

---

# 🧠 Why NotebookFusion?

NotebookFusion helps Data Scientists, AI Engineers, Students, and Researchers by allowing them to:

- Read documentation without leaving notebooks
- Watch tutorials while coding
- Display dashboards or live web apps
- Improve notebook-based learning workflows
- Create interactive demo notebooks

---

# 🖥️ Supported Platforms

| Platform | Supported |
|----------|------------|
| Jupyter Notebook | ✅ |
| JupyterLab | ✅ |
| Google Colab | ✅ |
| VS Code Notebook | ✅ |

---

# 📂 Project Structure

```text
NotebookFusion/
│
├── NotebookFusion/
│   ├── __init__.py
│   ├── site.py
│   └── youtube.py
│
├── README.md
├── requirements.txt
├── setup.py
└── LICENSE
```

---

# 🛠️ Development Setup

Clone the repository:

```bash
git clone https://github.com/yourusername/NotebookFusion.git
```

Move into the project directory:

```bash
cd NotebookFusion
```

Create a virtual environment:

```bash
conda create -n notebookfusion_env python=3.10 -y
```

Activate the environment:

```bash
conda activate notebookfusion_env
```

Install development dependencies:

```bash
pip install -r requirements_dev.txt
```

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub!