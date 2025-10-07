#!/usr/bin/env python3
"""
Script para testar criação de usuário
"""

import sys
import os

# Adiciona src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from common.services.users_service import UsersService
from common.schemas.users_schema import UserSchema

def handler(event, context):
    users_service = UsersService()
    user_data = UserSchema(**event)
    user_id = users_service.create_user(user_data.model_dump())
    return {"user_id": user_id, "message": "Usuário criado com sucesso"}

if __name__ == "__main__":
    user = {
        "name": "Gabriel Silva",
        "email": "gabriel@email.com",
        "password": "senha123"
    }
    
    print("🚀 Testando criação de usuário...")
    result = handler(user, None)
    print(f"✅ {result}")
