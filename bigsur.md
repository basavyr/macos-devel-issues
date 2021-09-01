# Resources for macOS 11 BigSur

## Homebrew

[set-up path for homebrew](https://apple.stackexchange.com/questions/148901/why-does-my-brew-installation-not-work)

The newest macOS November 2002 update introduces a new version - BigSur, which is a new major release of macOS.

These are some useful packages for usage after a clean install of the OS.

## Cascadia Code font for iTerm and VS Code

[download](https://github.com/microsoft/cascadia-code/releases)

This [link](https://www.hack-the-planet.net/2019/09/28/cascadia-font-for-macos-terminal/) shows a guide on how to set the font up.

[Installing the font in VS Code](https://github.com/microsoft/cascadia-code/wiki/Installing-Cascadia-Code).

## VS Code - BigSur update (macOS 11)

With the latest version of macOS (BigSur), the Visual Studio Code editor presents some issues regarding UI stability. More precisely, there is some lagging while using the text editor and the *integrated terminal*. A few issues were opened on GitHub (see these two tickets [1](https://github.com/microsoft/vscode/issues/107103), [2](https://github.com/microsoft/vscode/issues/105446)).

The solution which helped the current development environment for this machine was to use the following command ([source](https://github.com/microsoft/vscode/issues/105446#issuecomment-727537602)):

```shell
codesign --remove-signature /Applications/Visual\ Studio\ Code.app/Contents/Frameworks/Code\ Helper\ \(Renderer\).app
```

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

[Installing pyenv on macOS](https://binx.io/blog/2019/04/12/installing-pyenv-on-macos/)


[Managing Multiple Python Versions With pyenv](https://realpython.com/intro-to-pyenv/)

[Setting up a Python environment in 2020](https://dev.to/py3course/setting-up-a-python-environment-in-2020-3e9e)

[Python Environment 101 - How are pyenv and pipenv different and when you should be using them](https://towardsdatascience.com/python-environment-101-1d68bda3094d#f3ad)

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


## Pipenv issues
___

### Numpy

Issues with the process of installing (which was also mentioned above) was solved by installing an older version, together with an older version of python itself.

It is considered that latest version of Python (that is `3.9`) it is having compatibility issues with BigSur. As a result, this might cause `numpy` package to fail when trying to run python scripts with the package imported.

### Matplotlib

When using `pipenv` to install the `matplotlib` package (which is used for plotting data and creating complex graphs), the installation process fails. Even when attempting to install different versions of `matplotlib`, the installation process would still not finish successfully. 
**Potential reason**: the pipenv package manager (that takes advantage of virtual environments within the python paradigm) was installed **via Homebrew**. Many threads on github indicate that the package for macOS managed by Homebrew is deflective with improper support.

🌟 Solution: use `pipenv` by installing it with `pip`. Since the virtual environment was already set up to work with `py-3.8.6`, the pip (that is pip3 actually) replaced the Homebrew version of pipenv. [This issue](https://github.com/pypa/pipenv/issues/1169) discusses about other similar situations where Homebrew version of `pipenv` fails to work properly when installing packages.

Furthermore, the installation process still failed, but the error message indicate the fact that a `jpeg` library was missing. Using [this guide](https://stackoverflow.com/questions/64884415/cant-install-matplotlib-on-macos-big-sur), the solution is to install the `libjpeg` service via Homebrew.

*TL;DR:*

* ✅ use `pipenv` installed via `pip`, and not via Homebrew.
* ⚠️ make sure the `libjpeg` service is available on the machine (it can be installed via Homebrew).

It is worth mentioning that these solutions were only tested on macOS BigSur.

#### December Update

[This commit](https://github.com/basavyr/python-pyenv-pipenv/commit/faf07dcbc65b82aae0e419599315b176480f9a00) which is part of a dedicated project for creating python scripts within virtual environments contains information with regards to the packages required for numerical computations (e.g., using `numpy`) or data visualization (e.g., using `matplotlib`).

In the last clean install of macOS 11 BigSur, followed by the proper python development environment setup (that is `pyenv` with `pipenv`), some issues on the installation process of (multiple versions) of `matplotlib` occurred. Solution was the installation of another python package, namely `cppy`. **All the packages were installed via `pipenv` (while `pipenv` was installed with `pip` and not via Homebrew).**

The repository referenced above contains a [file](https://github.com/basavyr/python-pyenv-pipenv/blob/main/code/collage-maker/py_pckgs_info) in which all the necessary packages for a proper setup that allows numerical computations can be achieved.

The `matplotlib` package fails to execute `plt.show()` command if the version of package is below `3.3.3` (latest at the moment of BigSur clean install). More details about the fix in [this GitHub post](https://github.com/matplotlib/matplotlib/issues/18953).

### Issues with scientific packages from Python

Using `pyenv` and `pipenv` within macOS 11 BigSur, there were issues when trying to install `seaborn` package. Due to other dependencies (i.e., numpy, pandas, matplotlib, and scipy) that were also failed during pre-installation phase, the process became practically problematic.

Several issues are mentioned with regards to the installation process of scipy and other scientific packages specific to Python. As a result, working with advanced data visualization methods for a Python project was impossible within *virtual environments*. This problem was reported on several GitHub issues (e.g., [1](https://github.com/scipy/scipy/issues/13102), [2](https://github.com/numpy/numpy/issues/17784), [3](https://github.com/pypa/pipenv/issues/4564)).

**Solution**: Use the scientific packages that come with [**Anaconda**](https://www.anaconda.com/).

The Anaconda *toolkit* was installed via Homebrew. This package comes with the `conda` command, which can be used for creating environments and installing&removing packages.

Some useful guides for a proper setting of `conda` environment alongside `pyenv`.

1. [Remove anaconda environment prefix from ubuntu terminal command prompt](https://stackoverflow.com/questions/42674401/remove-anaconda-environment-prefix-from-ubuntu-terminal-command-prompt)
2. [Installing anaconda with pyenv, unable to configure virtual environment](https://stackoverflow.com/questions/58044214/installing-anaconda-with-pyenv-unable-to-configure-virtual-environment/58045893#:~:text=Both%20pyenv%20and%20conda%20are,using%20these%20two%20tools%20together.)
3. [How do I prevent Conda from activating the base environment by default?](https://stackoverflow.com/questions/54429210/how-do-i-prevent-conda-from-activating-the-base-environment-by-default/57974390#57974390)
4. [Adding python version and pyenv virtualenv name to bash prompt?](https://stackoverflow.com/questions/49655329/adding-python-version-and-pyenv-virtualenv-name-to-bash-prompt)
5. [Anaconda on MacOS Big Sur](https://aungzanbaw.medium.com/anaconda-on-macos-big-sur-8ae860a74c7a)

Some useful guides for `conda` (from the Documentation):

1. [Managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#using-pip-in-an-environment)

Some GitHub issues that can be used for `pyenv` in order to properly show the current virtual environment, even if it is installed alongside `conda`.

* [Show current pyenv python version in bash prompt, and also color virtual envs differently
](https://gist.github.com/frnhr/dba7261bcb6970cf6121)
* [Question regarding prompt changing #135
](https://github.com/pyenv/pyenv-virtualenv/issues/135) -> this issue was related to `pyenv` behavior, where the current virtual environment would not show up, even if the `cwd` was a tree which had a `.python-version` file inside.