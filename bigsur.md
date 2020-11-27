# Resources for macOS 11 BigSur

The newest macOS November 2002 update introduces a new version - BigSur, which is a new major release of macOS.

These are some useful packages for usage after a clean install of the OS.

## Cascadia Code font for iTerm and VS Code

[download](https://github.com/microsoft/cascadia-code/releases)

This [link](https://www.hack-the-planet.net/2019/09/28/cascadia-font-for-macos-terminal/) shows a guide on how to set the font up.

[Installing the font in VS Code](https://github.com/microsoft/cascadia-code/wiki/Installing-Cascadia-Code).

## Python - virtual environments & separate package management

macOS BigSur still comes with the system installed Py2 and Py3 version of Python. However, these should be never used by user within development projects. The system-based python packages are just for app compatibility.

Solution for using Python for science/development projects is provided in several useful guides. It is essential to use `pyenv` and a python package manager, like `poetry` and `pipenv`. Below there are some useful guides for configuring your macOS with a proper python environment suitable for development/science.

### Webpages

1. [A student's guide to setting up Python on macOS
](https://sarimabbas.com/blog/python)
2. [Managing Multiple Python Versions With pyenv
](https://realpython.com/intro-to-pyenv/#why-not-use-system-python)
3. [Simple Python Version Management: pyenv
](https://github.com/pyenv/pyenv#homebrew-on-macos)
4. [A hygienic Python setup for Linux, Mac, and WSL
](https://read.acloud.guru/my-python-setup-77c57a2fc4b6)
5. [Requiring an active virtual environment for pip¶
](https://docs.python-guide.org/dev/pip-virtualenv/)

### Services

#### Pyenv

Download the latest release: [here](https://github.com/pyenv/pyenv/releases/tag/v1.2.21)

#### poetry

Download and documentation: [here](https://python-poetry.org/docs/)