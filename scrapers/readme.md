<h1>Criar arquivo simples</h1>

- o nome do arquivo é a slug da Casa ```{{slug}}.py```
- é necessário a ter a função ```script_func``` igual ao exemplo no final:

<h1>Arquivos de diretório</h1>

Se for necessário ter uma ação diferente para cada esporte os arquivos de diretórios podem ser criados da seguinte forma:

- Nome do diretório é a slug da Casa ```/{{slug}}```
- No diretório é necessário criar o arquivo ```__init__.py```
- Cada arquivo do esporte será o slug do Esporte da Casa ```{{slug}}.py```
- Em cada arquivo de esporte é necessário ter a função ```script_func``` igual ao exemplo abaixo:


```python
from libs.register import *

def script_func(esporte) -> list[Bet]:
    #do something
    return []