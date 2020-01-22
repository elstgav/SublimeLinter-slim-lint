#
# linter.py
# Linter for SublimeLinter4, a code checking framework for Sublime Text 3
#
# Written by Gavin Elster
# Contributors: Richard Baptist
# Copyright (c) 2015 Gavin Elster
#
# License: MIT
#

"""This module exports the SlimLint plugin class."""

from SublimeLinter.lint import RubyLinter


class SlimLint(RubyLinter):
    """Provides an interface to slim-lint."""

    cmd = None
    tempfile_suffix = '.slim'

    version_args = '-S slim-lint --version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.5.0'

    regex = (
        r'^.+?:(?P<line>\d+) '
        r'(?:(?P<error>\[E\])|(?P<warning>\[W\])) '
        r'(?P<message>[^`]*(?:`(?P<near>.+?)`)?.*)'
    )

    defaults = {
        'selector': 'source.slim',
        '--config': '${folder}/.slim-lint.yml',
        'env': {
           'SLIM_LINT_RUBOCOP_CONF': '${folder}/.rubocop.yml'
        }
    }

    def cmd(self):
        """Build the command to run slim-lint."""
        settings = self.get_view_settings()

        command = ['ruby', '-S']

        if settings.get('use_bundle_exec', False):
            command.extend(['bundle', 'exec'])

        command.extend(['slim-lint'])

        return command
