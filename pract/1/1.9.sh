#!/bin/bash

input_file="$1"
output_file="$2"

# Заменяем последовательности из 4 пробелов на символ табуляции и записываем в выходной файл
sed 's/    /\t/g' "$input_file" > "$output_file"

echo "Пробелы заменены табами в '$input_file' и записаны в'$output_file'."
