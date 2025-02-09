"""
Calcula linhas de canal
"""

import click
import os


digits = os.getenv("DIGITOS")


@click.command()
@click.argument("preco1", type=float)
@click.argument("preco2", type=float)
def ln(preco1, preco2):
    """Calcula linhas de canal"""
    dif = preco2 - preco1
    linha = preco2 + dif
    click.echo("%.{0}f".format(digits) % abs(linha))


if __name__ == "__main__":
    ln()
