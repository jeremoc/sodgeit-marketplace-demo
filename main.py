import os
import click

class FileChecker:
    def __init__(self):
        pass

    def _file_exists_in_project(self, filename: str, start_path: str ="./") -> bool:
        for dirpath, dirnames, filenames in os.walk(start_path):
            for file in filenames:
                print(file)
                if file == filename:
                    return True
        return False

    def run(self):
        @click.command()
        @click.argument('file_name')
        @click.option('--start_path', default='./', help='Path for start searching project')
        def cli(file_name, start_path):
            if not os.path.exists(start_path):
                print(f"ERROR: Start path '{start_path}' does not exist!")
                exit(1)

            if self._file_exists_in_project(filename=file_name, start_path=start_path):
                print(f"SUCCESS: File '{file_name}' found in project!")
                exit(0)
            else:
                print(f"ERROR: Could not find '{file_name}' in directory '{start_path}'")
                exit(1)

        cli()

if __name__ == "__main__":
    checker = FileChecker()
    checker.run()
