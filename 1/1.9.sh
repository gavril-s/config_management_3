#!/bin/bash

input_file="$1"
output_file="$2"

# Заменяем последовательности из 4 пробелов на символ табуляции и записываем в выходной файл
sed 's/    /\t/g' "$input_file" > "$output_file"

echo "Spaces replaced with tabs in '$input_file' and saved to '$output_file'."
