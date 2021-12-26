import click

HOST = click.option(
    "--host",
    "-h",
    metavar="HOST",
    default="127.0.0.1",
    help="The network address to listen on (default: 127.0.0.1)."
)

PORT = click.option(
    "--port", 
    "-p", 
    metavar="PORT",
    default=5000, 
    help="The port to listen on (default: 5000)."
)