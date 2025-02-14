from click.testing import CliRunner
from pa import pa


run = CliRunner()


def test_calcula_uma_lateralidade():
    res = run.invoke(pa, ["tr", "800", "400"])
    assert (
        res.output
        == "400 pt\n1200 1X\n800\n668 0.33\n536 0.66\n400\n0 1X\n"
    )
