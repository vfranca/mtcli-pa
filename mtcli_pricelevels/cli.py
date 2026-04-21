"""
Aplicativo CLI para calcular níveis  e projeções de price action
"""

import click
from .commands.bo import bo
from .commands.ln import ln
from .commands.tr import tr
from .commands.gp import gp


@click.group(
    "levels",
    help="Calcula níveis e projeções com base em Price Action (suporte, resistência, alvos).",
)
@click.version_option(package_name="mtcli-pricelevels")
def levels():
    """Calcula niveis e projecoes de price action"""
    pass


levels.add_command(bo)
levels.add_command(ln)
levels.add_command(tr)
levels.add_command(gp)
