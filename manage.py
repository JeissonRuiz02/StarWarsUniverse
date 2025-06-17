#!/usr/bin/env python
"""Management utility for Django administrative tasks.

This script sets up the environment and delegates commands to Django's
`execute_from_command_line` function. It is typically used to run commands
like `runserver`, `migrate`, or `createsuperuser`.

Usage:
    python manage.py <command>
"""

import os
import sys


def main():
    """Configures settings and executes command-line utility for Django.

    This function sets the default settings module for Django and delegates
    command execution to Django's command-line interface.

    Raises:
        ImportError: If Django isn't installed or not available in the
        current Python environment.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'starwars_api.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and available "
            "on your PYTHONPATH environment variable, and that you've "
            "activated your virtual environment."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
