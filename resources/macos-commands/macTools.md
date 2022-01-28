# Tools for macOS

Checking architecture of libraries, packages and binaries on macOS.

Check arch of an application launcher from the command line [source](https://gitlab.com/gnachman/iterm2/-/issues/9389#note_474761536)

```shell
lipo -archs iTerm.app/Contents/MacOS/ShellLauncher
x86_64
```

[`lipo`](https://ss64.com/osx/lipo.html) is a command line tool for manipulating universal binaries.
