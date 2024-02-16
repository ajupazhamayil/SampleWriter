from generator.gen_ai_sample_generator import SampleCreator
from os.path import join, dirname, basename
from util.file_sample_util import FileSampleUtil as SampleUtil
from interface.source_interface import SourceInterface

class FileSource(SourceInterface):
    def __init__(self, config: dict[str, str]):
        self.sample_util = SampleUtil(config)
        self.sample_list = self.sample_util.get_files_in_dir(config['sample_path_list'])
        self.sample_creator = SampleCreator(config)

    def process(self) -> int:
        failure = False
        for file in self.sample_list:
            try:
                sample_content = self.sample_util.read_sample_file(file)
                print(sample_content)
                print()
                new_sample = self.sample_creator.generate_new_sample(sample_content)
                print(new_sample)
                print()
                new_sample_file = join(dirname(dirname(file)), basename(file))
                self.sample_util.write_sample_file(new_sample_file, new_sample)
                print()
                print()
            except Exception as ex:
                print(str(ex))
                print("An exception occured for the file " + str(file))
                failure = True
        if failure:
            return -1
        return 0
