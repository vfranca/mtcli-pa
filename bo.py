"""
Calcula pullback e projeções de rompimento
"""

import click
import os


digits = os.getenv("DIGITOS")
if digits == None:
    digits = 0


@click.command()
@click.argument("final", type=float)
@click.argument("inicio", type=float)
def bo(final, inicio):
    """Calcula pullbacks e projecoes de rompimento"""
    tamanho = final - inicio
    click.echo("%.{0}f pts".format(digits) % abs(tamanho))
    projecao1 = final + tamanho
    projecao2 = final + tamanho * 2
    click.echo("%.{0}f 2X".format(digits) % projecao2)
    click.echo("%.{0}f 1X".format(digits) % projecao1)
    click.echo("%.{0}f BOP".format(digits) % final)
    niveis = [0.33, 0.50, 0.66]
    pullback = []
    i = 0
    for n in niveis:
        pullback.append(final - tamanho * n)
        click.echo("%.{0}f %.2f".format(digits) % (pullback[i], n))
        i += 1


if __name__ == "__main__":
    bo()
