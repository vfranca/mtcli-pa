"""
Aplicativo CLI calcular níveis  e projeções de price action
"""

import click
from bo import bo
from ln import ln
from tr import tr


@click.group()
def pa():
    """Calcula niveis e projecoes de price action"""
    pass


pa.add_command(bo)
pa.add_command(ln)
pa.add_command(tr)


if __name__ == "__main__":
    pa()
