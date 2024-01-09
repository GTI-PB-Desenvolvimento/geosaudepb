from geosaudepb.pb import Macroregiao


def test_all_macrorregiao():
    macrorregioes = Macroregiao.get_all()

    assert type(next(macrorregioes)) is Macroregiao

def test_get_macrorregiao():
    macro_1 = Macroregiao('1')

    assert type(macro_1) is Macroregiao
    assert macro_1.id == '1'
    assert macro_1.nome == '1ª Macro'
