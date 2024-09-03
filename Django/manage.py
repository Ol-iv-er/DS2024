#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DJANGO.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it is installed and "
            "available on your PYTHONPATH environment variable"
            "forgot to acttivate a virtual enronment"
        ) from exc
    execute_from_command_line(sys.argv)