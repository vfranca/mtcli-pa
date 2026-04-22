"""
Registro do plugin mtcli-pricelevels no mtcli principal.
"""

from .cli import levels


def register(cli):
    """
    Registra o comando 'levels' no mtcli principal.
    """
    cli.add_command(levels, name="levels")
    cli.add_command(levels, name="pa")
