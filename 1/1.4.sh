#!/bin/bash

file="$1"

# Извлекаем все слова (идентификаторы) из файла
identifiers=$(grep -oE '\b[a-zA-Z_][a-zA-Z0-9_]*\b' "$file")

# Удаляем повторяющиеся идентификаторы и сортируем их
unique_identifiers=$(echo "$identifiers" | tr ' ' '\n' | sort -u)

# Выводим уникальные идентификаторы
echo "$unique_identifiers"