"""
Calcula projeções e níveis em lateralidade
"""

import click
import os


digits = os.getenv("DIGITOS")
if digits == None:
    digits = 0


@click.command()
@click.argument("maxima", type=float)
@click.argument("minima", type=float)
def tr(maxima, minima):
    """Calcula projecoes e niveis em lateralidade"""
    tamanho = maxima - minima
    click.echo("%.{0}f pt".format(digits) % abs(tamanho))
    projecao_acima = maxima + tamanho
    click.echo("%.{0}f 1X".format(digits) % projecao_acima)
    click.echo("%.{0}f".format(digits) % maxima)
    niveis = [0.33, 0.66]
    nivel = []
    i = 0
    for n in niveis:
        nivel.append(maxima - tamanho * n)
        click.echo("%.{0}f %.2f".format(digits) % (nivel[i], n))
        i += 1
    click.echo("%.{0}f".format(digits) % minima)
    projecao_abaixo = minima - tamanho
    click.echo("%.{0}f 1X".format(digits) % projecao_abaixo)


if __name__ == "__main__":
    tr()
