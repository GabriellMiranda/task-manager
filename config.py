"""
Configurações do projeto Task Manager
"""
import os
import sys
from pathlib import Path

# Adiciona src ao Python path automaticamente
PROJECT_ROOT = Path(__file__).parent
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

# Configurações do banco de dados
DATABASE_PATH = PROJECT_ROOT / "task_manager.db"

# Configurações gerais
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
