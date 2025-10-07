# Task Manager API

API serverless para gerenciamento de tarefas usando AWS Lambda e API Gateway.

## 🏗️ Arquitetura

- **AWS Lambda**: Funções serverless para lógica de negócio
- **API Gateway**: Endpoints REST para a API
- **SQLite**: Banco de dados local (arquivo)
- **Python 3.12**: Runtime da aplicação

## 📋 Endpoints

### POST /users
Cria um novo usuário no sistema.

**Request:**
```json
{
  "name": "João Silva",
  "email": "joao@email.com",
  "password": "senha123"
}
```

**Response:**
```json
{
  "user_id": 1,
  "message": "Usuário criado com sucesso"
}
```

## 🚀 Deploy

### Pré-requisitos
- AWS CLI configurado
- SAM CLI instalado
- Conta AWS com permissões adequadas

### Deploy Local (Desenvolvimento)
```bash
# Instalar dependências
pip install -e .

# Executar localmente
python src/handlers/users.py
```

### Deploy AWS (Produção)
```bash
# Build da aplicação
sam build -t template.yaml

# Deploy para ambiente dev
sam deploy --guided

# Deploy para ambiente específico
sam deploy --parameter-overrides Environment=dev

# Deploy para staging
sam deploy --parameter-overrides Environment=staging

# Deploy para produção
sam deploy --parameter-overrides Environment=prod
```

## 🛠️ Comandos SAM Úteis

```bash
# Build da aplicação
sam build -t template.yaml

# Build com container (para dependências nativas)
sam build -t template.yaml --use-container

# Deploy guiado (primeira vez)
sam deploy --guided

# Deploy rápido (usando samconfig.toml)
sam deploy

# Deploy com parâmetros específicos
sam deploy --parameter-overrides Environment=dev

# Testar localmente
sam local start-api -t template.yaml

# Invocar função localmente
sam local invoke CreateUserFunction -t template.yaml

# Validar template
sam validate -t template.yaml

# Listar recursos do stack
aws cloudformation list-stack-resources --stack-name task-manager-api-dev

# Ver logs da Lambda
sam logs -n CreateUserFunction --stack-name task-manager-api-dev --tail
```

## 🧪 Testando a API

### Teste Local
```bash
# Build do projeto
sam build -t template.yaml

# Iniciar API localmente
sam local start-api -t template.yaml

# A API estará disponível em http://127.0.0.1:3000
# Teste com:
curl -X POST http://127.0.0.1:3000/users \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "João Silva",
    "email": "joao@email.com",
    "password": "senha123"
  }'
```

### Teste em Produção
Após o deploy, você receberá a URL da API. Teste com:

```bash
curl -X POST https://your-api-url.amazonaws.com/dev/users \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "João Silva",
    "email": "joao@email.com",
    "password": "senha123"
  }'
```

## 📁 Estrutura do Projeto

```
task-manager/
├── src/
│   ├── handlers/
│   │   └── users.py          # Handler Lambda para usuários
│   ├── common/
│   │   ├── services/         # Lógica de negócio
│   │   ├── repositories/     # Acesso a dados
│   │   ├── schemas/          # Validação com Pydantic
│   │   ├── database.py       # Configuração SQLite
│   │   └── utils.py          # Utilitários
├── template.yaml             # Template SAM
├── samconfig.toml           # Configurações SAM
└── requirements.txt         # Dependências Python
```

## 🔧 Configurações

### Variáveis de Ambiente
- `ENVIRONMENT`: Ambiente (dev/staging/prod)
- `DATABASE_PATH`: Caminho do arquivo SQLite
- `PYTHONPATH`: Caminho dos módulos Python

### Parâmetros do Template
- `Environment`: Nome do ambiente (dev/staging/prod)

## 📊 Monitoramento

Acesse o AWS CloudWatch para:
- Logs da Lambda function
- Métricas de performance
- Alertas e dashboards

## 🔒 Segurança

- Senhas são criptografadas com hash SHA-256 + salt
- CORS configurado para permitir requisições
- Validação de entrada com Pydantic
- Constraints de banco para dados únicos

## 🛠️ Desenvolvimento

### Estrutura de Código
- **Handlers**: Pontos de entrada das Lambda functions
- **Services**: Lógica de negócio
- **Repositories**: Acesso a dados
- **Schemas**: Validação e serialização

### Adicionando Novos Endpoints
1. Crie o handler em `src/handlers/`
2. Adicione o service em `src/common/services/`
3. Crie o repository em `src/common/repositories/`
4. Defina o schema em `src/common/schemas/`
5. Atualize o `template.yaml` com o novo endpoint
6. Faça build e deploy:
   ```bash
   sam build -t template.yaml
   sam deploy --parameter-overrides Environment=dev
   ```