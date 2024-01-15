# Macrorregião

## Parâmetros

- **id** = informa qual macrorregião deverá ser retornada.

```python
from geosadepb.pb import Macroregiao

macro = Macroregiao('1') 
print(macro) # <Macroregiao id="1", nome="1ª Macro" >
```

## Atributos

- **nome:** Nome da macrorregião.
```python
print(macro.nome) # 1ª Macro
```

- **id:** id da macrorregião.
```python
print(macro.id) # 1
```

- **gerencias**: Retorna um gerador das [Gerencias](docs/pb/gerencias.md) pertencentes a macroregão.
```python
print(list(macro.gerencias)) # [<Gerencia id="1", nome="1ª Gerência" >, ...]
```

## Métodos

- **get_all (Método de classe)**: Retorna uma lista de todas as macrorregiões.
```python
print(list(macro.get_all())) # [<Gerencia id="1", nome="1ª Gerência" >, ...]
```
