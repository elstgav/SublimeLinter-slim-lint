SublimeLinter-slim-lint
=======================

[![Release Version](https://img.shields.io/github/release/elstgav/SublimeLinter-slim-lint.svg)](https://github.com/elstgav/SublimeLinter-slim-lint/releases) [![Build Status](https://travis-ci.org/elstgav/SublimeLinter-slim-lint.svg?branch=master)](https://travis-ci.org/elstgav/SublimeLinter-slim-lint) [![Gratipay](https://img.shields.io/gratipay/elstgav.svg)](https://gratipay.com/~elstgav/)

This linter plugin for [SublimeLinter][docs] provides an interface to [slim-lint]. It will be used with files that have the “Ruby Slim” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `slim-lint` is installed on your system. To install `slim-lint`, do the following:

1. Install [Ruby](http://ruby-lang.org/).

2. Install `slim-lint` by typing the following in a terminal:

         gem install slim_lint

3. If you are using `rvm` or `rbenv`, ensure that they are loaded in your shell’s correct startup file. See [here](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#shell-startup-files) for more information.

**Note:** This plugin requires `slim-lint` 0.4.0 or later.

### Linter configuration
In order for `slim-lint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `slim-lint`, you can proceed to install the SublimeLinter-slim-lint plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

2. When the plugin list appears, type `slim-lint`. Among the entries you should see `SublimeLinter-slim-lint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

You can configure `slim-lint` options in the way you would from the command line, with `.slim-lint.yml` files. If a `.slim-lint.yml` file is not found in the file hierarchy starting with the linted file, your home directory will also be searched. For more information, see the [slim-lint page][slim-lint]. Default configuration file can be found [here](https://github.com/sds/slim-lint/blob/master/config/default.yml).

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
2. Hack on a separate branch created from the latest `master`.
3. Commit and push the branch.
4. Make a pull request.
5. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

* Indent is 4 spaces.
* Code should pass flake8 and pep257 linters.
* Vertical whitespace helps readability, don’t be afraid to use it.
* Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[slim-lint]:            https://github.com/sds/slim-lint
[docs]:                 http://sublimelinter.readthedocs.org
[installation]:         http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]:                   https://sublime.wbond.net/installation
[cmd]:                  http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]:             http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]:      http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]:      http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
