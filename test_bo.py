from click.testing import CliRunner
from pa import pa


run = CliRunner()


def test_calcula_rompimento_de_alta():
    res = run.invoke(pa, ["bo", "800", "400"])
    assert (
        res.output
        == "400 pts\n1600 2X\n1200 1X\n800 BOP\n668 0.33\n600 0.50\n536 0.66\n"
    )
