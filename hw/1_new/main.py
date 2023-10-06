import os
import tarfile
import zipfile


class VShell:
    def __init__(self, filesystem_archive):
        self.archive = None
        self.current_dir = ""
        self.filesystem_archive = filesystem_archive
        self.load_filesystem()

    def load_filesystem(self):
        if tarfile.is_tarfile(self.filesystem_archive):
            self.archive = tarfile.open(self.filesystem_archive, 'r')
        elif zipfile.is_zipfile(self.filesystem_archive):
            self.archive = zipfile.ZipFile(self.filesystem_archive, 'r')
        else:
            raise ValueError("Unsupported archive format")

    def list_files(self):
        if isinstance(self.archive, tarfile.TarFile):
            all_members = self.archive.getmembers()
            files = [member.name for member in all_members if member.isfile()]
            return [file for file in files if file.startswith(self.current_dir)]
        elif isinstance(self.archive, zipfile.ZipFile):
            return [file for file in self.archive.namelist() if file.startswith(self.current_dir)]

    def change_directory(self, new_dir):
        if new_dir.startswith('/'):
            self.current_dir = new_dir
        else:
            # if-else ниже предназначен для теста на винде
            if self.filesystem_archive.split('.')[-1] == "tar":
                if self.current_dir != '':
                    self.current_dir = self.current_dir + '/' + new_dir
                else:
                    self.current_dir = self.current_dir + new_dir
            else:
                self.current_dir = os.path.join(self.current_dir, new_dir)

    def print_working_directory(self):
        print("/" + self.current_dir)

    def cat(self, filename):
        try:
            if self.filesystem_archive.split('.')[-1] == "tar":
                with self.archive.extractfile(self.current_dir + "/" + filename) as file:
                    content = file.read().decode("utf-8")
                    print(content)
            else:
                with self.archive.open(self.current_dir + "/" + filename) as file:
                    for line in file:
                        print(line.decode('utf-8').strip())
        except (FileNotFoundError, KeyError):
            print(f"File '{filename}' not found")


def main():
    archive_file = input("Enter the path to the filesystem archive: ")
    vshell = VShell(archive_file)

    while True:
        command = input(f"/{vshell.current_dir}> ")
        if command == "exit":
            break
        elif command == "pwd":
            vshell.print_working_directory()
        elif command == "ls":
            files = vshell.list_files()
            for file in files:
                print(file)
        elif command.startswith("cd "):
            new_dir = command.split(" ", 1)[1]
            vshell.change_directory(new_dir)
        elif command.startswith("cat "):
            filename = command.split(" ", 1)[1]
            vshell.cat(filename)
        else:
            print("Command not recognized")


if __name__ == "__main__":
    main()
