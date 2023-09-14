#!/bin/bash

directory="$1"

# Ищем все файлы в указанной директории и её подкаталогах
# с расширением .txt
find "$directory" -type f -name "*.txt" | while read file; do
  # Проверяем, пустой ли файл
  if [ ! -s "$file" ]; then
    echo "Пустой файл: $file"
  fi
done
