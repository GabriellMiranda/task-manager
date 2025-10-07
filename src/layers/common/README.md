# Common Layer

Esta layer contém o código comum compartilhado entre as funções Lambda do projeto Task Manager.

## Estrutura

```
python/
├── __init__.py
├── database.py          # Configuração do banco SQLite
├── utils.py             # Utilitários (hash de senhas)
├── repositories/         # Camada de acesso a dados
│   ├── __init__.py
│   └── users_repository.py
├── schemas/             # Validação com Pydantic
│   ├── __init__.py
│   └── users_schema.py
└── services/            # Lógica de negócio
    ├── __init__.py
    └── users_service.py
```

## Dependências

- pydantic>=2.0.0
- email-validator>=2.0.0

## Como usar

A layer é automaticamente incluída nas funções Lambda através do template.yaml:

```yaml
Layers:
  - !Ref CommonLayer
```

O código comum pode ser importado diretamente:

```python
from common.services.users_service import UsersService
from common.schemas.users_schema import UserSchema
```
