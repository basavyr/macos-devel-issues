commands for macos

For compilers to find zlib you may need to set:
  export LDFLAGS="-L/opt/homebrew/opt/zlib/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/zlib/include"

==> Summary
🍺  /opt/homebrew/Cellar/zlib/1.2.11: 12 files, 430.2KB
==> Caveats
==> openssl@1.1
A CA file has been bootstrapped using certificates from the system
keychain. To add additional certificates, place .pem files in
  /opt/homebrew/etc/openssl@1.1/certs

and run
  /opt/homebrew/opt/openssl@1.1/bin/c_rehash

openssl@1.1 is keg-only, which means it was not symlinked into /opt/homebrew,
because macOS provides LibreSSL.

If you need to have openssl@1.1 first in your PATH, run:
  echo 'export PATH="/opt/homebrew/opt/openssl@1.1/bin:$PATH"' >> ~/.zshrc

For compilers to find openssl@1.1 you may need to set:
  export LDFLAGS="-L/opt/homebrew/opt/openssl@1.1/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/openssl@1.1/include"

==> readline
readline is keg-only, which means it was not symlinked into /opt/homebrew,
because macOS provides BSD libedit.

For compilers to find readline you may need to set:
  export LDFLAGS="-L/opt/homebrew/opt/readline/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/readline/include"

==> sqlite
sqlite is keg-only, which means it was not symlinked into /opt/homebrew,
because macOS already provides this software and installing another version in
parallel can cause all kinds of trouble.

If you need to have sqlite first in your PATH, run:
  echo 'export PATH="/opt/homebrew/opt/sqlite/bin:$PATH"' >> ~/.zshrc

For compilers to find sqlite you may need to set:
  export LDFLAGS="-L/opt/homebrew/opt/sqlite/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/sqlite/include"

==> zlib
zlib is keg-only, which means it was not symlinked into /opt/homebrew,
because macOS already provides this software and installing another version in
parallel can cause all kinds of trouble.

For compilers to find zlib you may need to set:
  export LDFLAGS="-L/opt/homebrew/opt/zlib/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/zlib/include"
