from geosaudepb.pb import Gerencia, Macroregiao


def test_all_macrorregiao():
    macrorregioes = Macroregiao.get_all()

    assert type(next(macrorregioes)) is Macroregiao


def test_get_macrorregiao():
    macro = Macroregiao('1')

    assert type(macro) is Macroregiao
    assert macro.id == '1'
    assert macro.nome == '1ª Macro'
    assert len([*macro.gerencias]) == 3


def test_all_gerencias():
    gerencias = Gerencia.get_all()

    assert type(next(gerencias)) is Gerencia


def test_get_gerencia():
    gerencia = Gerencia('1')

    assert gerencia.id == '1'
    assert gerencia.nome == '1ª Gerência'
    assert gerencia.macrorregiao.id == '1'
