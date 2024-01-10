import json
from typing import Generator
from urllib.request import urlopen


class _Base:
    _data: dict = {}
    _data_url: str = 'https://raw.githubusercontent.com/GTI-PB-Desenvolvimento/geosaudepb/main/data/'
    json_name: str = ''

    @classmethod
    def get_data(cls):
        json_url = cls._data_url + cls.json_name

        if not cls._data:
            response = urlopen(json_url)
            if not response.status == 200:
                raise ConnectionError

            json_text = response.read()
            cls._data = json.loads(json_text.decode('utf-8'))

        return cls._data


class MuniciopioNotFound(Exception):
    ...


class Macroregiao(_Base):
    json_name = 'macroregioes.json'

    def __init__(self, id: str):
        self.nome = self.get_data()[id]
        self.id = id

    @property
    def gerencias(self) -> Generator:
        return (gerencia for gerencia in Gerencia.get_all() if gerencia.macrorregiao.id == self.id)

    @classmethod
    def get_all(cls) -> Generator:
        return (cls(macro_id) for macro_id in cls.get_data().keys())

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id="{self.id}", nome="{self.nome}" >'


class Gerencia(_Base):
    json_name = 'gerencias.json'

    def __init__(self, id):
        gerencia = self.get_data()[id]

        self.id = id
        self.nome = gerencia['nome']
        self.macrorregiao = Macroregiao(gerencia['macrorregiao_id'])

    @property
    def municipios(self) -> Generator:
        return (municipio for municipio in Municipio.get_all() if municipio.gerencia.id == self.id)

    @classmethod
    def get_all(cls) -> Generator:
        return (cls(gerencia_id) for gerencia_id in cls.get_data().keys())

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id="{self.id}", nome="{self.nome}" >'


class Municipio(_Base):
    json_name = 'municipios.json'

    def __init__(self, **kwargs):
        municipio_id, municipio = self._get_municipio(**kwargs)

        self.id = municipio_id
        self.nome = municipio['nome']
        self.ibge = municipio['ibge']
        self.gerencia = Gerencia(municipio['gerencia_id'])
        
    def _get_municipio(self, **kwargs):
        if id := kwargs.get('id'):
            return id, self.get_data()[id]

        ibge, nome = kwargs.get('ibge'), kwargs.get('nome')
        if ibge or nome:
            for municipio_id, municipio in self.get_data().items():
                if municipio['ibge'] == ibge:
                    return municipio_id, municipio

                if municipio['nome'] == nome:
                    return municipio_id, municipio

        raise MuniciopioNotFound

    @classmethod
    def get_all(cls) -> Generator:
        return (cls(id=municipio_id) for municipio_id in cls.get_data().keys())

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id="{self.id}", nome="{self.nome}" >'
