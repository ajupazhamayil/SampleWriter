# SampleWriter

SampleWriter is a utility that automates the sample creation process using Google Gemini.

## Configuration

SampleWriter's behavior is controlled by the `config.ini` file.

- `sample_path_list`: The path to a file containing a list of existing sample directories that need to be updated. Output will be stored within the same parent directory as the input sample file.
- `header`: The path to a file containing the text to be added to the beginning of each new sample.
- `footer`: The path to a file containing the text to be added to the end of each new sample.
- `sample_pattern`: The path to a file containing a regular expression pattern. This pattern helps SampleWriter find the right section within the input samples to use as input prompt for the AI model.
- `training_prompt`: The path to a file containing the tone and style instructions for the GenAI model.
- `training_input`: The path to a directory containing old sample data for training the AI model.
- `training_output`: The path to a directory containing new sample data for training the AI model.
- `api_key_env`: The name of the environment variable storing the Google Gemini API key.
