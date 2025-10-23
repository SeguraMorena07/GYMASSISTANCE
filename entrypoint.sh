#!/bin/sh
echo "Esperando a que MySQL esté listo..."
sleep 15

echo "Iniciando Flask..."
flask run --host=0.0.0.0