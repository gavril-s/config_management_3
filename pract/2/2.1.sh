#!/bin/bash

# Указываем имя пакета
package_name="matplotlib"

# Указываем путь к метаданным пакета
metadata_file=$(pip show $package_name | grep -i 'metadata-file' | cut -d: -f2 | tr -d ' ')

# Выводим содержимое метаданных
cat $metadata_file
