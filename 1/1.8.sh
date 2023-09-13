#!/bin/bash

if [ $# -ne 2 ]; then
  echo "Usage: $0 <directory> <extension>"
  exit 1
fi

directory="$1"
extension="$2"

# Проверяем, существует ли указанный каталог
if [ ! -d "$directory" ]; then
  echo "Error: Directory '$directory' does not exist."
  exit 1
fi

# Создаем имя архива на основе текущей даты и времени
archive_name="archive_$(date +'%Y%m%d%H%M%S').tar"

# Ищем файлы с заданным расширением в каталоге и его подкаталогах и архивируем их
find "$directory" -type f -name "*.$extension" -exec tar -rvf "$archive_name" {} \;

# Упаковываем архив
gzip "$archive_name"

echo "Files with .$extension extension have been archived into $archive_name.gz"
