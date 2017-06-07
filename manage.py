#!/usr/bin/env python
import os
import sys

try:
    import dotenv
except ImportError:
    dotenv = None

if __name__ == "__main__":

    dotenv.read_dotenv()

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'BaseConfiguration')

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
