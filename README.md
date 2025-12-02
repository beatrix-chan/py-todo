# py-todo

[![GitHub](https://img.shields.io/badge/@beatrix--chan-py--todo-181717?style=for-the-badge&logo=github)](https://github.com/beatrix-chan/py-todo) ![Python](https://img.shields.io/badge/python-yellow?style=for-the-badge&logo=python) ![Streamlit](https://img.shields.io/badge/Streamlit-white?style=for-the-badge&logo=streamlit)

A to-do list app built mainly with Python.

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
- [Credits](#credits)

</details>

## Tech Stack

![Python,Streamlit,Anaconda](https://skills.syvixor.com/api/icons?perline=15&i=python,streamlit,anaconda)

## Features

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

## Credits

- [Streamlit](https://streamlit.io)
- [How to Create a To-Do List Using Streamlit? - Programmingempire](https://www.programmingempire.com/how-to-create-a-to-do-list-using-streamlit/)
