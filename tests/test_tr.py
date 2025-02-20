from click.testing import CliRunner
from pa.pa import pa


run = CliRunner()


def test_calcula_uma_lateralidade():
    res = run.invoke(pa, ["tr", "800", "400"])
    assert res.output == "400 pt\n1200 1X\n800\n668 0.33\n536 0.66\n400\n0 1X\n"


def test_calcula_uma_lateralidade_com_opcao_digitos():
    res = run.invoke(pa, ["tr", "--digitos", "1", "800", "400"])
    assert (
        res.output
        == "400.0 pt\n1200.0 1X\n800.0\n668.0 0.33\n536.0 0.66\n400.0\n0.0 1X\n"
    )
