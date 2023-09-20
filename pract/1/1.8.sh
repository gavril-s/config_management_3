#!/bin/bash

directory="$1"
extension="$2"

# Создаем имя архива на основе текущей даты и времени
archive_name="archive_$(date +'%Y%m%d%H%M%S').tar.gz"

# Ищем файлы с заданным расширением в каталоге и его подкаталогах и архивируем их
find "$directory" -type f -name "*.$extension" -exec tar -czf "$archive_name" {} \;

echo "Файлы .$extension упакованы в $archive_name.gz"
