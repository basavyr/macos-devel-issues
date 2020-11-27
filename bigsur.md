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

Official docs: [here](https://github.com/pyenv/pyenv)
Download the latest release: [here](https://github.com/pyenv/pyenv/releases/tag/v1.2.21)

#### poetry

Download and documentation: [here](https://python-poetry.org/docs/)

#### pipenv

[Basic Usage of Pipenv](https://pipenv.pypa.io/en/latest/basics/#)

[Further Configuration of pip and Virtualenv](https://docs.python-guide.org/dev/pip-virtualenv/)


Documentation:
 
[Installing Pyenv and Pipenv in a Testing Environment](https://medium.com/@chris_birch/installing-pyenv-and-pipenv-to-easily-manage-python-dependencies-19735ce5dfb0#:~:text=Pipenv%20combines%20Pip%20with%20virtual,of%20Python%20for%20each%20project.&text=pipenv%20install%20is%20used%20to,add%20them%20to%20the%20Pipfile.)

[Pipenv & Virtual Environments](https://pipenv.pypa.io/en/latest/install/#installing-packages-for-your-project)

[Installing Python packages in 2019: pyenv and pipenv
](https://gioele.io/pyenv-pipenv) - *The objective of this small guide is to describe how pyenv, pipenv and various other tools work together to install and manage Python packages. This guide is aimed at those who would like to have a look behind the scenes to understand how modern Python packaging tools work together.*


In this current build of macOS (referring to the local machine on which development takes place), `pyenv` and `pipenv` are configured so that oen can set different python versions for each project. Installing packages (e.g. `scipy`, `numpy`) is taken care of by `pipenv`. 

⚠️ **BigSur** issue: The latest macOS version has compatibility issues with the latest version of `numpy` and latest version of Python (that is 3.9).

ℹ️ As a result, the current system uses Python `3.8.6 ` and `numpy-1.18`

More useful information for setting up environments:

[Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)

[Official repo for `pyenv`🚀](https://github.com/pyenv/pyenv#advanced-configuration)


#### pipx

[pipx — Install and Run Python Applications in Isolated Environments](https://pipxproject.github.io/pipx/)
