# py-todo

[![GitHub](https://img.shields.io/badge/@beatrix--chan-py--todo-181717?style=for-the-badge&logo=github)](https://github.com/beatrix-chan/py-todo) [![License](https://img.shields.io/github/license/beatrix-chan/py-todo?style=for-the-badge)](https://github.com/beatrix-chan/py-todo/blob/main/LICENSE)
<br />
![Python](https://img.shields.io/badge/python-yellow?style=for-the-badge&logo=python) [![Streamlit](https://img.shields.io/badge/Streamlit-white?style=for-the-badge&logo=streamlit)](https://streamlit.io/)<br />
![Code Duration](https://img.shields.io/badge/Coding_Duration-3_hours-faf0e6?style=for-the-badge)

A to-do list app built with Python and Streamlit.

<details>

<summary>Table of Contents</summary>

- [Tech Stack](#tech-stack)
- [Features](#features)
- [Getting Started](#getting-started)
    - [Setting up Python environment](#setting-up-python-environment)
        - [Installing `mamba` and default `conda-forge` channel](#installing-mamba-and-default-conda-forge-channel)
        - [Creating virtual environment](#creating-virtual-environment)
        - [Install Streamlit](#install-streamlit)
    - [Running `py-todo`](#running-py-todo)
- [What I have learnt](#what-i-have-learnt)
- [Contribution](#contribution)
- [Credits](#credits)

</details>

## Tech Stack

![Python,Streamlit,Anaconda](https://skills.syvixor.com/api/icons?perline=15&i=python,streamlit,anaconda)

## Features

- **Kanban-style** two-column board (To Do / Completed)
- **Toggle completion with checkboxes** to move tasks between columns
- **Live task counts** for each column
- **Quick actions**: Clear Completed and Clear All
- **Visual feedback** with toasts and balloons
- **Handy menu links**: About, Report a bug, Get help
- **Session-based storage** (resets on page reload)

## Getting Started

> [!IMPORTANT]
> **Prerequisite**: Python 3.13.9+

It is recommended to use a virtual environment. I personally uses [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main), which is a miniature version of Anaconda Distribution. I also use [`mamba`](https://github.com/mamba-org/mamba) as my package manager, and install packages via `conda-forge` channel. You may continue following along if you are using miniconda (assuming if you installed it on your system already; you may skip to [Creating virtual environment](#creating-virtual-environment) if you are already using `mamba` and `conda-forge`), or you may follow [Streamlit](https://docs.streamlit.io/get-started/installation)'s guide on installation.

### Setting up Python environment

#### Installing `mamba` and default `conda-forge` channel

Make sure you're in the *(base)* environment. Otherwise, run `conda activate base` first before pasting each of the following lines:

```bash
# Install mamba via conda-forge
conda install -c conda-forge mamba
# Update all packages via conda-forge channel in the base environment
mamba update --all
# Configurate conda-forge as default channel
conda config --add channels conda-forge
conda config --set channel_priority strict
# Reconfirm if conda-forge is default
conda config --show channels
```

#### Creating virtual environment

[Streamlit supports python version 3.9 to 3.13](https://docs.streamlit.io/get-started/installation/command-line#prerequisites).

```bash
# Create a virtual environment
conda create -n py-todo python=3.13
# Activate the environment
conda activate py-todo
```

#### Install Streamlit

```bash
# Install streamlit
mamba install streamlit
# Confirm installation
streamlit hello
```

> [!TIP]
> If you are new to using the terminal, press `CTRL`+`C` to terminate serving port. (**This might just be a Windows thing, not sure for Linux and macOS**)

### Running py-todo

```bash
# Make sure you're in the right environment
conda activate py-todo
# Run the app with streamlit
streamlit run app.py
```

This should now run on [localhost:8501](http://localhost:8501)! Enjoy!

## What I have learnt

Before i started on this project, I used to think that framework only applies to frontend languages like JavaScript (e.g. React, Angular, Express, Next.js, Vue.js, Vite.js) and CSS (e.g. Bootstrap, Bulma, Foundation, Pure, Skeleton). A Python framework gives you a bunch of ready-made tools and libraries to build web apps, websites, or other software. It’s like grabbing a starter kit, so you don’t waste time rewriting the same code over and over. You just dive into the parts that actually make your project different.[^1]

There are two types of Python Frameworks: Full-Stack Frameworks and Micro-Frameworks. Full-Stack Frameworks includes handling databases, sessions, routing, and rendering (i.e. comprehensive backend stuffs), while Micro-Frameworks are lightweight and flexible, and offers basic features to get started with building an application.[^2]

I learnt about [Streamlit](https://streamlit.io) from [@pikacodes's reel](https://www.youtube.com/shorts/tZDuQC36LM8) about Warp. Although there are more other Python frameworks that are available to choose, simple enough with good documentations and community supports like Django, Flask, FastAPI, etc. I felt like Streamlit is just a really good way to start myself to get familiar with Python frameworks even though it's meant for data apps. Thanks to Streamlit's super comprehensive [documentation](https://docs.streamlit.io/) and [Programmingempire's tutorial](https://www.programmingempire.com/how-to-create-a-to-do-list-using-streamlit/), I was able to build `py-todo` within two hours, and completely finished building the app in another hour.

[^1]: GeeksforGeeks, "Top 10 Python Frameworks [2025 Updated]", *GeeksforGeeks*. Accessed: Dec. 02, 2025. [Online]. Available: [https://www.geeksforgeeks.org/blogs/best-python-frameworks/](https://www.geeksforgeeks.org/blogs/best-python-frameworks/#what-is-python-frameworks)
[^2]: GeeksforGeeks, "Top 10 Python Frameworks [2025 Updated]", *GeeksforGeeks*. Accessed: Dec. 02, 2025. [Online]. Available: [https://www.geeksforgeeks.org/blogs/best-python-frameworks/](https://www.geeksforgeeks.org/blogs/best-python-frameworks/#types-of-python-frameworks)

## Contribution

You may contribute by opening [issues](https://github.com/beatrix-chan/py-todo/issues) or [fork](https://github.com/beatrix-chan/py-todo/fork) the repository and open pull request.

## Credits

**This project is not sponsored by anyone or any parties**

- [Streamlit](https://streamlit.io)
- [How to Create a To-Do List Using Streamlit? - Programmingempire](https://www.programmingempire.com/how-to-create-a-to-do-list-using-streamlit/)
