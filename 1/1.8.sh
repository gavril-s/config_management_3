#!/bin/bash

directory="$1"
extension="$2"

# Создаем имя архива на основе текущей даты и времени
archive_name="archive_$(date +'%Y%m%d%H%M%S').tar"

# Ищем файлы с заданным расширением в каталоге и его подкаталогах и архивируем их
find "$directory" -type f -name "*.$extension" -exec tar -rvf "$archive_name" {} \;

# Упаковываем архив
gzip "$archive_name"

echo "Files with .$extension extension have been archived into $archive_name.gz"
