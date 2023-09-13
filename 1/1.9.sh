#!/bin/bash

if [ $# -ne 2 ]; then
  echo "Usage: $0 <input_file> <output_file>"
  exit 1
fi

input_file="$1"
output_file="$2"

# Проверяем, существует ли указанный входной файл
if [ ! -f "$input_file" ]; then
  echo "Error: Input file '$input_file' does not exist."
  exit 1
fi

# Заменяем последовательности из 4 пробелов на символ табуляции и записываем в выходной файл
sed 's/    /\t/g' "$input_file" > "$output_file"

echo "Spaces replaced with tabs in '$input_file' and saved to '$output_file'."
