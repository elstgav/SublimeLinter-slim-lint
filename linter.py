#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Gavin Elster
# Copyright (c) 2015 Gavin Elster
#
# License: MIT
#

"""This module exports the SlimLint plugin class."""

import os
from SublimeLinter.lint import RubyLinter, util


class SlimLint(RubyLinter):

    """Provides an interface to slim-lint."""

    syntax = 'ruby slim'
    cmd = 'slim-lint'
    tempfile_suffix = '-'
    config_file = ('--config', '.slim-lint.yml', '~')

    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = ' >= 0.4.0'

    regex = (
        r'^.+?:(?P<line>\d+) '
        r'(?:(?P<error>\[E\])|(?P<warning>\[W\])) '
        r'(?P<message>[^`]*(?:`(?P<near>.+?)`)?.*)'
    )

    def build_args(self, settings):
        """
        Return a list of args to add to cls.cmd.

        We hook into this method to find the rubocop config and set it as an
        environment variable for the rubocop linter to pick up.
        """

        if self.filename:
            config = util.find_file(
                os.path.dirname(self.filename),
                '.rubocop.yml',
                aux_dirs='~'
            )
            if config:
                os.environ["RUBOCOP_CONFIG"] = config

        return super().build_args(settings)
