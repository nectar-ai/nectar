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
    "--algorithm",
    "-a",
    metavar="ALGORITHM",
    prompt=True,
    type=click.Choice([
        "A2C",
        "A3C",
        "DDPG",
        "DDPPO",
        "DQN",
        "PPO",
        "SAC",
        "TD3"
    ], case_sensitive=False)
)
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
def run (uri, algorithm, iterations, discount_factor, learning_rate):
    """
    Run Nectar against an OpenAI Gym environment from the local URI
    using the specified number of iterations, discount factor, and
    learning rate.
    """
    click.echo(f"URI: {uri}\n"
    f"Algorithm: {algorithm}\n"
    f"Iterations: {iterations}\n"
    f"Discount Factor: {discount_factor}\n"
    f"Learning Rate: {learning_rate}\n"
    )

@cli.command()
@cli_args.HOST
@cli_args.PORT
def server(host, port):
    """
    Launch the Nectar server.
    The UI will be visible at http://localhost:5000 by default.
    """
    run_server(host, port)

if __name__ == "__main__":
    cli()
