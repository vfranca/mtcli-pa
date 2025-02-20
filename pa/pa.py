"""
Aplicativo CLI para calcular níveis  e projeções de price action
"""

import click
from pa.bo import bo
from pa.ln import ln
from pa.tr import tr
from pa.gp import gp


@click.group()
def pa():
    """Calcula niveis e projecoes de price action"""
    pass


pa.add_command(bo)
pa.add_command(ln)
pa.add_command(tr)
pa.add_command(gp)


if __name__ == "__main__":
    pa()
