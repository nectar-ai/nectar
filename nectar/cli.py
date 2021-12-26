import click

from nectar.server import run_server
from nectar.utils import cli_args

@click.group()
@click.version_option()
def cli():
    pass

@cli.command()
@click.argument("uri")
def run (uri):
    """
    Run Nectar against an OpenAI Gym environment from the given URI.
    For local runs, the run will block until it completes.
    If running locally (the default), the URI must be a local path.
    """
    # TODO: Add argument for experiment config and implement service method
    pass

@cli.command()
@cli_args.HOST
@cli_args.PORT
def server(host, port):
    """
    Launch the Nectar server.
    The UI will be visible at http://localhost:5000 by default.
    """
    run_server(host, port)