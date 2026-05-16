# 🚀 NotebookFusion

![PyPI version](https://img.shields.io/pypi/v/NotebookFusion.svg)
![Python versions](https://img.shields.io/pypi/pyversions/NotebookFusion.svg)
![License](https://img.shields.io/pypi/l/NotebookFusion.svg)

**NotebookFusion** is a lightweight Python package that allows you to seamlessly render live websites and embed YouTube videos directly inside Jupyter Notebooks, JupyterLab, and Google Colab environments.

No more switching browser tabs while coding — view websites, tutorials, dashboards, or videos right beside your notebook cells.

---

# ✨ Features

- 🌐 Website Rendering → Display live HTTPS websites inside notebook output cells  
- ▶️ YouTube Embedding → Automatically embed YouTube videos from URLs  
- 📏 Customizable Viewport → Adjust width and height easily  
- ⚡ Lightweight & Fast → Minimal dependencies using IPython display tools  
- 📓 Notebook Friendly → Works on Jupyter Notebook, JupyterLab, Google Colab, VS Code  

---

# 📦 Installation

```bash
pip install NotebookFusion

development install:
pip install -r requirements_dev.txt

🚀 Quick Start

▶️ YouTube Video
from NotebookFusion.youtube import render_youtube_video

render_youtube_video("https://www.youtube.com/watch?v=h25pePMdoPA&t=712s")

🌐 Website Rendering
from NotebookFusion.site import render_site

render_site("https://www.google.com")


⚙️ Advanced Usage
Custom Website Size
from NotebookFusion.site import render_site

render_site(
    "https://www.python.org",
    width="100%",
    height="600px"
)
Custom YouTube Size
from NotebookFusion.youtube import render_youtube_video

render_youtube_video(
    "https://www.youtube.com/watch?v=h25pePMdoPA",
    width="900",
    height="500"
)
🧠 Why NotebookFusion?
Read documentation inside notebooks
Watch tutorials without leaving code
Embed dashboards and live websites
Improve interactive learning workflow
Build powerful notebook demos
🖥️ Supported Platforms
Platform	Supported
Jupyter Notebook	✅
JupyterLab	✅
Google Colab	✅
VS Code Notebook	✅
📂 Project Structure
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
🛠️ Development Setup
git clone https://github.com/yourusername/NotebookFusion.git
cd NotebookFusion

conda create -n notebookfusion_env python=3.10 -y
conda activate notebookfusion_env

pip install -r requirements_dev.txt
🤝 Contributing
Fork this repository
Create a new branch
Commit your changes
Open a Pull Request
📄 License

MIT License

⭐ Support

If you like this project, give it a ⭐ on GitHub


If you want, I can next :contentReference[oaicite:0]{index=0}.