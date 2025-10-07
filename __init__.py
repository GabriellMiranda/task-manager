"""
Task Manager Package
Configura automaticamente o Python path
"""
import sys
import os
from pathlib import Path

# Adiciona src ao Python path automaticamente
PROJECT_ROOT = Path(__file__).parent
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))
