import click

from nectar.server import run_server
from nectar.utils import cli_args

@click.group()
@click.version_option()
def cli():
    pass

@cli.command()
@click.argument("uri")
@click.option(
    "--iterations",
    "-i",
    metavar="ITERATIONS",
    prompt=True
)
@click.option(
    "--discount_factor",
    "-d",
    metavar="DISCOUNT_FACTOR",
    prompt=True
)
@click.option(
    "--learning_rate",
    "-l",
    metavar="LEARNING_RATE",
    prompt=True
)
def run (uri, iterations, discount_factor, learning_rate):
    """
    Run Nectar against an OpenAI Gym environment from the local URI
    using the specified number of iterations, discount factor, and
    learning rate.
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