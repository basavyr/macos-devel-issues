# Development environment for Python on the `M1` architecture


The current shell environment for the M1 MBA has the following configurations for the Python `pyenv` service:

```
export PATH=$PATH:/opt/homebrew/bin
export PATH=$PATH:~/.local/bin
eval "$(pyenv init --path)"
```

```
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

These commands help for the `pyenv` package to work (installed via Homebrew) when called within a shell instance.