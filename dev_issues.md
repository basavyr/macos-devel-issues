# Development issues with Apple Silicon

## Setup `$PATH` 

[setup the path of a package](https://stackoverflow.com/questions/46391721/pipenv-command-not-found)

## Installing `Python` via `pyenv` on Apple Silicon **M1**

- Using the Python interpreter with Apple Silicon requires the installation of `Homebrew` and then installing `pyenv` using 

> brew install pyenv

- After the successful installation of Homebrew, the installation of `pyenv` is straightforward. However, there is an alternative approach of using `pyenv`, namely via [this method](https://github.com/pyenv/pyenv-installer) which is an automated installer.

> curl https://pyenv.run | bash

## Using `pyenv` to install Python version `3.8.6`

- When trying to install a custom version of Python which is natively supported on the M1 processor, some issues occur. 
- The following guides where followed for the straightforward installation of Python `3.8.6` via `pyenv`: 

> pyenv install 3.8.6

- However, several issues occur. See the attached log file for the details with regards to the failed installation process. ([file](./failed_pyenv.log))

## Resources and documentation for solving the issue

- Requires a separate command for `v3.8.6` -> [Python build fails on M1 Apple Silicon with arm64 homebrew · Issue #1768 · pyenv/pyenv](https://github.com/pyenv/pyenv/issues/1768)

> pyenv install --patch 3.8.6 <<(curl -sSL https://raw.githubusercontent.com/Homebrew/formula-patches/113aa84/python/3.8.3.patch\?full_index\=1)

Other useful guides for `pyenv`

* [Installing Python 3 on Mac OS X — The Hitchhiker's Guide to Python](https://docs.python-guide.org/starting/install3/osx/)
* [Pipenv & Virtual Environments — The Hitchhiker's Guide to Python](https://docs.python-guide.org/dev/virtualenvs/#virtualenvironments-ref)
* [pyenv: Multi-version Python development on Mac | by Dirk Avery | FAUN](https://faun.pub/pyenv-multi-version-python-development-on-mac-578736fb91aa)
* [pyenv/pyenv-installer: This tool is used to install `pyenv` and friends.](https://github.com/pyenv/pyenv-installer)
* [Install Python on macOS 11 M1 (Apple Silicon) using pyenv | by Tony Lai | Medium](https://laict.medium.com/install-python-on-macos-11-m1-apple-silicon-using-pyenv-12e0729427a9)
* [Install Homebrew on macOS 11 (Apple Silicon) | by Tony Lai | Medium](https://laict.medium.com/install-homebrew-on-macos-11-apple-silicon-630f37a74490)
* [formula-patches/python at master · Homebrew/formula-patches](https://github.com/Homebrew/formula-patches/tree/master/python)

**Observation** - Versions of Python higher than `3.9.0` should work on the M1 macs via `pyenv` without issues and extra arguments.