from click.testing import CliRunner
from pa.pa import pa


run = CliRunner()


def test_calcula_a_linha_de_canal():
    res = run.invoke(pa, ["ln", "500", "400"])
    assert res.output == "300\n"


def test_calcula_um_canal_com_a_opcao_digitos():
    res = run.invoke(pa, ["ln", "--digitos", "1", "600", "400"])
    assert res.output == "200.0\n"
