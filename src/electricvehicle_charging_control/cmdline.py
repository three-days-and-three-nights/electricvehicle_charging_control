import click
from electricvehicle_charging_control import __version__
from electricvehicle_charging_control.config import settings
from electricvehicle_charging_control.server import Server

@click.group(invoke_without_command=True)
@click.pass_context
@click.option('-V', '--version', is_flag=True, help='Show version and exit.')
def main(ctx, version):
    if version:
        click.echo(__version__)
    elif ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())

@main.command()
@click.option('-h', '--host', show_default=True, help=f'Host IP. Default: {settings.SERVER.HOST}')
@click.option('-p', '--port', show_default=True, type=int, help=f'Port. Default: {settings.SERVER.PORT}')
@click.option('--level', help='Log level')
def server(host, port, level):
    """Start server."""
    kwargs = {
        'LOGLEVEL': level,
        'HOST': host,
        'PORT': port,
    }
    for name, value in kwargs.items():
        if value:
            settings.set(name, value)

    Server().run()
