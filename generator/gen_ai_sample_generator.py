from util.file_sample_util import FileSampleUtil
import google.generativeai as genai
from os import getenv
from os import listdir
from os.path import basename, dirname, isfile, join

class SampleCreator:
    OLD_SAMPLE = "Old Sample "
    NEW_SAMPLE = "New Sample "

    def __init__(self, config: dict[str, str]):
        genai.configure(api_key=getenv(config['api_key_env']))
        self.model = genai.GenerativeModel(
            model_name = self.get_model(),
            generation_config = self.get_generation_config(),
            safety_settings = self.get_safety_config()
        )
        self.sample_util = FileSampleUtil(config)
        self.prompt_parts = []
        self.prepare_prompt_parts(config)

    def prepare_prompt_parts(self, config: dict[str, str]) -> list[str]:
        input_path = config['training_input']
        training_input_list = [join(input_path, file) for file in listdir(input_path) if isfile(join(input_path, file))]
        self.prompt_parts.append(self.sample_util.read_file(config['training_prompt']))
        for file in training_input_list:
            old_sample = file
            new_sample = join(config['training_output'], basename(file))
            self.prompt_parts.append(self.OLD_SAMPLE + self.sample_util.read_sample_file(old_sample))
            self.prompt_parts.append(self.NEW_SAMPLE + self.sample_util.read_sample_file(new_sample))
        return self.prompt_parts

    def get_model(self) -> str:
        return "gemini-pro"

    def get_safety_config(self) -> list[str]:
        return [
            {
              "category": "HARM_CATEGORY_HARASSMENT",
              "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
              "category": "HARM_CATEGORY_HATE_SPEECH",
              "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
              "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
              "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
              "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
              "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
        ]

    def get_generation_config(self) -> dict[str, str]:
        # Update these parameters for better results.
        # Refer: https://cloud.google.com/vertex-ai/generative-ai/docs/text/test-text-prompts
        return {
          "temperature": 0.9,
          "top_p": 1,
          "top_k": 1,
          "max_output_tokens": 2048,
        }

    def generate_new_sample(self, old_content: str) -> str:
        self.prompt_parts.extend([self.OLD_SAMPLE + old_content, self.NEW_SAMPLE])
        return self.model.generate_content(self.prompt_parts).text
