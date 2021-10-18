# -*- coding: utf-8 -*-

import unittest

import click
from coverage import coverage, CoverageException

from project import main


@click.group()
def cli_main():
    pass


@cli_main.command("run")
def main():
    main.execute()


@click.group()
def cli_tests():
    pass


@cli_tests.command("test")
def test():
    """ Runs the test without generating a coverage report """

    tests = unittest.TestLoader().discover(".", pattern="tests*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    return True if result.wasSuccessful() else False


@cli_tests.command("coverage")
def cov():
    """ Runs the unit tests and generates a coverage report on success """

    coverage_ = coverage(branch=True, include=["./project/*"])
    coverage_.start()

    tests = unittest.TestLoader().discover(".", pattern="tests*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if result.wasSuccessful():
        try:
            coverage_.stop()
            coverage_.save()
            coverage_.report()
            coverage_.html_report()
            coverage_.erase()

        except CoverageException as error:
            print(error)


cli = click.CommandCollection(sources=[cli_main, cli_tests])
if __name__ == "__main__":
    cli()
