from geosaudepb.pb import Gerencia, Macroregiao, Municipio


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


def test_all_municipios():
    municipios = Municipio.get_all()

    assert type(next(municipios)) is Municipio


def municipio_asserts(municipio):
    assert municipio.id == '94'
    assert municipio.nome == 'João Pessoa'
    assert municipio.ibge == '2507507'
    assert municipio.gerencia.id == '1'


def test_get_municipio_by_id():
    municipio = Municipio(id='94')
    municipio_asserts(municipio)


def test_get_municipio_by_name():
    municipio = Municipio(nome='João Pessoa')
    municipio_asserts(municipio)


def test_get_municipio_by_ibge():
    municipio = Municipio(ibge='2507507')
    municipio_asserts(municipio)
