import os
import zlib

def generate_dot_graph(repo_path, output_file):
    dot_file = open(output_file, 'w')
    dot_file.write("digraph G {\n")

    # Функция для поиска всех объектов в папке .git/objects
    def find_objects(directory):
        for root, _, files in os.walk(directory):
            for file in files:
                yield os.path.join(root, file)

    # Функция для извлечения хеш-суммы объекта
    def extract_object_hash(file_path):
        # Имя файла объекта состоит из первых двух символов хеша (подпапка) и остального хеша (имя файла)
        obj_hash = os.path.join(os.path.basename(os.path.dirname(file_path)), os.path.basename(file_path))
        obj_hash = obj_hash[:2] + obj_hash[3:]
        return obj_hash

    # Поиск объектов в .git/objects
    objects_directory = os.path.join(repo_path, '.git', 'objects')
    for obj_file in find_objects(objects_directory):
        # Извлечь хеш-сумму объекта
        obj_hash = extract_object_hash(obj_file)

        # Определение формы вершины в зависимости от типа объекта
        with open(obj_file, 'rb') as f:
            compressed_content = f.read()
            content = zlib.decompress(compressed_content)
            if content.startswith(b'commit'):
                shape = "ellipse"  # Если это коммит, используйте форму ellipse
                commit_info = content.decode()
                # Извлечь информацию о родительских коммитах
                parents = [line.split()[1] for line in commit_info.split('\n') if line.startswith('parent ')]
                for parent in parents:
                    dot_file.write(f'  "{obj_hash}" -> "{parent}" [label="parent"];\n')
            else:
                shape = "box"  # В противном случае, используйте форму box

        # Добавить вершину с хеш-суммой в файл dot
        dot_file.write(f'  "{obj_hash}" [label="{obj_hash[:12]}", shape={shape}];\n')

    dot_file.write("}\n")
    dot_file.close()

if __name__ == '__main__':
    repo_path = 'test_repo'  # Укажите путь к вашему локальному git-репозиторию
    output_file = 'git_graph.dot'

    generate_dot_graph(repo_path, output_file)
    print(f"Граф изменений сохранен в {output_file}")
