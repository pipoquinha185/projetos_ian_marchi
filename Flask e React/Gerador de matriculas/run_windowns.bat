@echo off
echo Iniciando o Backend (Flask)...
start cmd /k "cd flask-server && venv\Scripts\activate && python server.py"

echo Iniciando o Frontend (React)...
start cmd /k "cd client && npm start"

echo Sistema rodando! Verifique as janelas abertas.
pause