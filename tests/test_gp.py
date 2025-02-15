from click.testing import CliRunner
from pa import pa


run = CliRunner()


def test_calcula_do_gap_do_dia():
    res = run.invoke(pa, ["gp", "400", "800"])
    assert res.output == "400\n"


def test_calcula_gap_do_dia_com_variaveis_de_ambiente():
    res = run.invoke(pa, ["gp"])
    assert res.output == "-400\n"
