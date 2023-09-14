#!/bin/bash

file="$1"

# Извлекаем все слова из файла
identifiers=$(grep -oE '\b[a-zA-Z_][a-zA-Z0-9_]*\b' "$file")

# Удаляем повторяющиеся и сортируем
unique_identifiers=$(echo "$identifiers" | tr ' ' '\n' | sort -u)

echo "$unique_identifiers"
