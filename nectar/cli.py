import click
from nectar.server import _run_server

@click.group()
@click.version_option()
def cli():
    pass

@cli.command()
def run ():
    _run_server()