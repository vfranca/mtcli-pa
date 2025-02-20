from click.testing import CliRunner
from pa.pa import pa


run = CliRunner()


def test_calcula_do_gap_do_dia():
    res = run.invoke(pa, ["gp", "400", "800"])
    assert res.output == "400\n"


def test_calcula_gap_do_dia_com_variaveis_de_ambiente():
    res = run.invoke(pa, ["gp"])
    assert res.output == "-400\n"


def test_calcula_gap_do_dia_com_a_opcao_digitos():
    res = run.invoke(pa, ["gp", "--digitos", "1", "800", "400"])
    res.output == "-400.0\n"
