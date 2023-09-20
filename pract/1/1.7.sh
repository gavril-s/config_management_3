#!/bin/bash

# Путь к директории
directory="."

# Создаем массив, чтобы хранить хэши
declare -A file_hashes

find "$directory" -type f | while read file; do
  # Вычисляем хэш файла
  hash=$(sha256sum "$file" | awk '{print $1}')
  
  # Если файл с таким хэшем уже был найден, то это дубликат
  if [[ -n "${file_hashes[$hash]}" ]]; then
    echo "Дубликат: $file и ${file_hashes[$hash]}"
  else
    # В противном случае, сохраняем текущий файл как файл с данным хэшем
    file_hashes[$hash]="$file"
  fi
done
