#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 <command_name>"
  exit 1
fi

command_name="$1"

# Проверяем, существует ли файл с именем команды
if [ -f "$command_name" ]; then
  # Устанавливаем права доступа 755 (rwxr-xr-x) для команды
  chmod 755 "$command_name"
  
  # Копируем команду в /usr/local/bin
  cp "$command_name" /usr/local/bin/
  
  echo "Command '$command_name' has been registered."
else
  echo "Error: Command '$command_name' not found."
  exit 1
fi
