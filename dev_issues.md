# Development issues with Apple Silicon

## Installing `Python` via `pyenv` on Apple Silicon **M1**

- Using the Python interpreter with Apple Silicon requires the installation of `Homebrew` and then installing `pyenv` using 

> brew install pyenv

- After the successful installation of Homebrew, the installation of `pyenv` is straightforward. However, there is an alternative approach of using `pyenv`, namely via [this method](https://github.com/pyenv/pyenv-installer) which is an automated installer.

> curl https://pyenv.run | bash

## Using `pyenv` to install Python version `3.8.6`

- When trying to install a custom version of Python which is natively supported on the M1 processor, some issues occur. 
- The following guides where followed for the straightforward installation of Python `3.8.6` via `pyenv`: 

> pyenv install 3.8.6

- However, several issues occur. See the attached log file for the details with regards to the failed installation process.