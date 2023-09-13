#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

directory="$1"

# Проверяем, существует ли указанная директория
if [ ! -d "$directory" ]; then
  echo "Error: Directory '$directory' does not exist."
  exit 1
fi

# Ищем все файлы в указанной директории и её подкаталогах
# с расширением .txt (или другим текстовым расширением, которое вы хотите использовать)
find "$directory" -type f -name "*.txt" | while read file; do
  # Проверяем, пустой ли файл
  if [ ! -s "$file" ]; then
    echo "Empty text file: $file"
  fi
done
