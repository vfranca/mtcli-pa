from click.testing import CliRunner
from pa import pa


run = CliRunner()


def test_calcula_a_linha_de_canal():
    res = run.invoke(pa, ["ln", "500", "400"])
    assert res.output == "300\n"
