#!/bin/bash

for file in *.c *.js *.py; do
  # Проверяем, существует ли файл
  if [ -e "$file" ]; then
    # Считываем первую строку из файла
    first_line=$(head -n 1 "$file")
    
    # Проверяем, начинается ли первая строка с символа комментария
    if [[ "$first_line" =~ ^[[:space:]]*[/#] ]]; then
      echo "Файл $file начинается с комментария: $first_line"
    else
      echo "Файл $file не начинается с комментария: $first_line"
    fi
  fi
done
