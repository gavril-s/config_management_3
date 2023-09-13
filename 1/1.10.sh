#!/bin/bash

directory="$1"

# Ищем все файлы в указанной директории и её подкаталогах
# с расширением .txt (или другим текстовым расширением, которое вы хотите использовать)
find "$directory" -type f -name "*.txt" | while read file; do
  # Проверяем, пустой ли файл
  if [ ! -s "$file" ]; then
    echo "Empty text file: $file"
  fi
done
