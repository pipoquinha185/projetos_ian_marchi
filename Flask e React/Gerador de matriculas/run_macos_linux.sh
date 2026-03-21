#!/bin/bash

echo "Iniciando o Backend (Flask)..."
# Abre um novo terminal para o Flask
osascript -e 'tell app "Terminal" to do script "cd \"'$(pwd)'/flask-server\" && source venv/bin/activate && python3 server.py"'

echo "Iniciando o Frontend (React)..."
# Abre um novo terminal para o React
osascript -e 'tell app "Terminal" to do script "cd \"'$(pwd)'/client\" && npm start"'

echo "Sistema rodando em janelas separadas!"