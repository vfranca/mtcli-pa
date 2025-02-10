"""
Calcula o gap do dia
"""

import click
from os import getenv

d = getenv("DIGITOS")


@click.command()
@click.argument("coy", envvar="coy", type=float)
@click.argument("ood", envvar="ood", type=float)
def gp(coy, ood):
    """Calcula o gap do dia"""
    gap = ood - coy
    click.echo("%.{0}f".format(d) % gap)


if __name__ == "__main__":
    gp()
