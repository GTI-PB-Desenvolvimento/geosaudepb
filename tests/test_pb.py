from geosaudepb.pb import Macroregiao


def test_all_macrorregiao():
    macrorregioes = Macroregiao.get_all()

    assert type(macrorregioes) is list
    assert len(macrorregioes) > 0

def test_get_macrorregiao():
    macro_1 = Macroregiao.get('1ª Macro')

    assert type(macro_1) is dict
    assert len(macro_1.keys()) > 0
