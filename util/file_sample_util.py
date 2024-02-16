import re
from os import listdir
from os.path import isfile, join

class FileSampleUtil:
    def __init__(self, config: dict[str, str]):
        self.header_filename = config['header']
        self.footer_filename = config['footer']
        self.sample_pattern_filename = config['sample_pattern']

    def read_file(self, filename: str) -> str:
        with open(filename, 'r') as f:
            return f.read()

    def get_header(self) -> str:
        return self.read_file(self.header_filename)

    def get_footer(self) -> str:
        return self.read_file(self.footer_filename)

    def get_sample_pattern(self) -> str:
        return self.read_file(self.sample_pattern_filename)

    def read_sample_file(self, filename: str) -> str:
        with open(filename, 'r') as f:
            file_content = re.search(
                self.get_sample_pattern(),
                f.read(),
                flags=re.DOTALL
            ).group(1)
        return file_content

    def read_file_list(self, filename: str) -> list[str]:
        with open(filename, 'r') as f:
            return f.read().splitlines()

    def get_files_in_dir(self, dirfile: str) -> list[str]:
        with open(dirfile, 'r') as f:
            path = f.read()
            return [join(path, file) for file in listdir(path) if isfile(join(path, file))]

    def write_sample_file(self, filename: str, content: str) -> None:
        with open(filename, 'w') as f:
            f.write(self.get_header() + content + self.get_footer())
