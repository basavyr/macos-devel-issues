# installing scipy on the M1 macbook air

issues with the installation process via the `pipenv` command. 

Solution: install the `BLAS` library provided by `brew`

 open_BLAS for M1 mac 

- installed via `homebrew`

Final installation guides

==> Pouring openblas--0.3.17.arm64_big_sur.bottle.tar.gz
==> Caveats
openblas is keg-only, which means it was not symlinked into /opt/homebrew,
because macOS provides BLAS in Accelerate.framework.

For compilers to find openblas you may need to set:
  export LDFLAGS="-L/opt/homebrew/opt/openblas/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/openblas/include"

For pkg-config to find openblas you may need to set:
  export PKG_CONFIG_PATH="/opt/homebrew/opt/openblas/lib/pkgconfig"

==> Summary
🍺  /opt/homebrew/Cellar/openblas/0.3.17: 23 files, 52.4MB
==> Caveats
==> openblas
openblas is keg-only, which means it was not symlinked into /opt/homebrew,
because macOS provides BLAS in Accelerate.framework.

For compilers to find openblas you may need to set:
  export LDFLAGS="-L/opt/homebrew/opt/openblas/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/openblas/include"

For pkg-config to find openblas you may need to set:
  export PKG_CONFIG_PATH="/opt/homebrew/opt/openblas/lib/pkgconfig"
