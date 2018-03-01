#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    open_source = '{{ cookiecutter.open_source }}'.lower()
    if not open_source == 'y' or open_source == 'yes':
        remove_file('LICENSE')
