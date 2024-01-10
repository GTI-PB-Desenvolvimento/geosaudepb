from geosaudepb.pb import Gerencia, Macroregiao, Municipio, UnidadeSaude


def test_all_macrorregiao():
    macrorregioes = Macroregiao.get_all()

    assert type(next(macrorregioes)) is Macroregiao


def test_get_macrorregiao():
    macro = Macroregiao('1')

    assert type(macro) is Macroregiao
    assert macro.id == '1'
    assert macro.nome == '1ª Macro'
    assert next(macro.gerencias).macrorregiao.id == '1'


def test_all_gerencias():
    gerencias = Gerencia.get_all()

    assert type(next(gerencias)) is Gerencia


def test_get_gerencia():
    gerencia = Gerencia('1')

    assert gerencia.id == '1'
    assert gerencia.nome == '1ª Gerência'
    assert gerencia.macrorregiao.id == '1'
    assert next(gerencia.municipios).gerencia.id == '1'


def test_all_municipios():
    municipios = Municipio.get_all()

    assert type(next(municipios)) is Municipio


def municipio_asserts(municipio: Municipio):
    assert municipio.id == '94'
    assert municipio.nome == 'João Pessoa'
    assert municipio.ibge == '2507507'
    assert municipio.gerencia.id == '1'
    assert next(municipio.unidades_saude).municipio.id == '94'


def test_get_municipio_by_id():
    municipio = Municipio(id='94')
    municipio_asserts(municipio)


def test_get_municipio_by_name():
    municipio = Municipio(nome='João Pessoa')
    municipio_asserts(municipio)


def test_get_municipio_by_ibge():
    municipio = Municipio(ibge='2507507')
    municipio_asserts(municipio)


def test_all_unidades_saude():
    unidades = UnidadeSaude.get_all()

    assert type(next(unidades)) is UnidadeSaude


def unidade_saude_asserts(unidade: UnidadeSaude):
    assert unidade.id == '286'
    assert unidade.cnes == '2399350'
    assert unidade.nome == 'LACEN ESTADUAL LABORATORIO CENTRAL DE SAUDE PUBLICA'
    assert unidade.municipio.id == '94'


def test_get_unidade_saude_by_id():
    unidade = UnidadeSaude(id='286')
    unidade_saude_asserts(unidade)


def test_get_unidade_saude_by_cnes():
    unidade = UnidadeSaude(cnes='2399350')
    unidade_saude_asserts(unidade)


def test_get_unidade_saude_by_nome():
    unidade = UnidadeSaude(nome='LACEN ESTADUAL LABORATORIO CENTRAL DE SAUDE PUBLICA')
    unidade_saude_asserts(unidade)
