from source.file_source import FileSource
from configparser import ConfigParser
from os.path import join, dirname

# Available input sources
available_sections = {
    'file' : FileSource
}

# Load the configuration file
config_file = "config.ini"
parser = ConfigParser()
parser.read(config_file)

for section in parser.sections():
    if section in available_sections:
        config_dict = dict(parser.items(section))
        source = available_sections[section](config_dict)
        if (source.process() == 0):
            print("Sample generation completed successfully")
        else:
            print("Something went wrong with the generation")
