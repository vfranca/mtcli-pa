from click.testing import CliRunner
from pa.pa import pa


run = CliRunner()


def test_calcula_rompimento_de_alta():
    res = run.invoke(pa, ["bo", "800", "400"])
    assert res.output == "400 pt\n1200 1X\n800\n668 0.33\n600 0.50\n536 0.66\n"


def test_calcula_rompimento_de_baixa():
    res = run.invoke(pa, ["bo", "400", "800"])
    assert res.output == "400 pt\n0 1X\n400\n532 0.33\n600 0.50\n664 0.66\n"


def test_calcula_rompimento_com_a_opcao_digitos():
    res = run.invoke(pa, ["bo", "--digitos", "1", "800", "400"])
    assert (
        res.output == "400.0 pt\n1200.0 1X\n800.0\n668.0 0.33\n600.0 0.50\n536.0 0.66\n"
    )
