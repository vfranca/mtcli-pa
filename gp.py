"""
Calcula o gap do dia
"""

import click
from os import getenv

digits = getenv("DIGITOS")
if digits == None:
    digits = 0


@click.command()
@click.argument("coy", envvar="coy", type=float)
@click.argument("ood", envvar="ood", type=float)
def gp(coy, ood):
    """Calcula o gap do dia"""
    gap = ood - coy
    click.echo("%.{0}f".format(digits) % gap)


if __name__ == "__main__":
    gp()
