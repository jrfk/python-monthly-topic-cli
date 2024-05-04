# SPDX-FileCopyrightText: 2024-present Junya Fukuda <junya.fukuda.e@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from python_monthly_topic_cli.__about__ import __version__
from .main import run

@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="python-monthly-topic-cli")
def python_monthly_topic_cli():
    """Python Monthly Topics CLI."""
    run()
