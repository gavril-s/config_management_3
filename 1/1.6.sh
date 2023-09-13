#!/bin/bash

# Путь к директории, в которой нужно выполнять проверку
directory="/путь/к/директории"

# Перебираем файлы с расширением .c, .js и .py в указанной директории
for file in "$directory"/*.c "$directory"/*.js "$directory"/*.py; do
  # Проверяем, существует ли файл
  if [ -e "$file" ]; then
    # Считываем первую строку из файла
    first_line=$(head -n 1 "$file")
    
    # Проверяем, начинается ли первая строка с символа комментария (# или //)
    if [[ "$first_line" =~ ^[[:space:]]*[/#] ]]; then
      echo "File $file starts with a comment: $first_line"
    else
      echo "File $file does not start with a comment: $first_line"
    fi
  fi
done
