import os
import tarfile
import zipfile

def unpack_filesystem(filesystem_path):
    extension = filesystem_path.split('.')[-1]
    if extension == 'tar':
        with tarfile.open(filesystem_path) as filesystem:
            filesystem.extractall()
    elif extension == 'zip':
        with zipfile.open(filesystem_path) as filesystem:
            filesystem.extractall()
    else:
        raise ValueError(f"Unsupported archive format")

def pwd():
    print(os.getcwd())

def ls():
    for file in os.listdir():
        print(file)

def cd(dir):
    os.chdir(dir)

def cat(filename):
    with open(filename) as file:
        print(file.read())

def main():
    filesystem_path = input("Enter the path for filesystem archive: ")
    unpack_filesystem(filesystem_path)
    current_dir = os.getcwd()

    while True:
        try:
            command = input(f"{current_dir} $ ")
            if command == 'pwd':
                pwd()
            elif command == 'ls':
                ls()
            elif command.startswith('cd '):
                dir = command.split()[1]
                cd(dir)
                current_dir = os.getcwd()
            elif command.startswith('cat '):
                filename = command.split()[1]
                cat(filename)
            elif command == 'exit':
                break
            else:
                print(f"Unsupported command")
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    main()