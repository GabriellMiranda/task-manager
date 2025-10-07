#!/usr/bin/env python3
"""
Script para gerenciar o banco de dados SQLite do Task Manager
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.common.database import init_database, reset_database, get_db

def show_tables():
    """Mostra todas as tabelas e seus dados"""
    with get_db() as conn:
        cursor = conn.cursor()
        
        # Mostrar tabelas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        
        print("📊 Tabelas no banco de dados:")
        for table in tables:
            table_name = table[0]
            print(f"\n🔹 {table_name.upper()}")
            
            # Contar registros
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = cursor.fetchone()[0]
            print(f"   Registros: {count}")
            
            # Mostrar estrutura
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = cursor.fetchall()
            print("   Colunas:")
            for col in columns:
                print(f"     - {col[1]} ({col[2]})")

def main():
    """Função principal"""
    if len(sys.argv) < 2:
        print("""
🔧 Gerenciador do Banco de Dados Task Manager

Uso: python manage_db.py <comando>

Comandos disponíveis:
  init     - Inicializa o banco de dados
  reset    - Remove e recria o banco (CUIDADO!)
  show     - Mostra informações das tabelas
  help     - Mostra esta ajuda
        """)
        return
    
    command = sys.argv[1].lower()
    
    if command == "init":
        init_database()
    elif command == "reset":
        confirm = input("⚠️  Tem certeza que quer apagar todos os dados? (sim/não): ")
        if confirm.lower() in ['sim', 's', 'yes', 'y']:
            reset_database()
        else:
            print("❌ Operação cancelada")
    elif command == "show":
        show_tables()
    elif command == "help":
        main()
    else:
        print(f"❌ Comando '{command}' não reconhecido")
        main()

if __name__ == "__main__":
    main()
