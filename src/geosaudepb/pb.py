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



class Macroregiao(_Base):
    json_name = 'macroregioes.json'

    def __init__(self, id: str):
        self.nome = self.get_data()[id]
        self.id = id

    @property
    def gerencias(self) -> Generator:
        pass

    @classmethod
    def get_all(cls) -> Generator:
        return (cls(macro_id) for macro_id in cls.get_data().keys())

    def __repr__(self) -> str:
        return f'<Macroregiao id="{self.id}", nome="{self.nome}" >'
