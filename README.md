# VTT Cleaner Project

This project contains a Python script to clean VTT files, removing unwanted tags and text.

## clean_file(input_file_path, output_file_path)

This function takes the path to an input file and the desired path for the cleaned output file. It performs the following steps:

1. Reads the input file contents.
2. Applies cleaning operations to the file contents.
3. Writes the cleaned contents to the output file.

### Parameters:
- `input_file_path` (str): Path to the input file.
- `output_file_path` (str): Path to the output file.

### Example usage:
```python
input_file_path = 'examples/green_egg_backloading.vtt'
output_file_path = 'examples/green_egg_backloading.vtt.cleaned'
clean_file(input_file_path, output_file_path)
```

## clean_contents(contents)

This function cleans the contents of a VTT file by performing several regex-based substitutions. The following cleaning operations are performed:

- Replaces occurrences of the word 'dirty' with 'clean'.
- Removes lines starting with 'WEBVTT'.
- Removes lines starting with 'NOTE duration:'.
- Removes lines starting with 'NOTE language:'.
- Removes lines with 'NOTE Confidence:' followed by a digit.
- Removes lines with 'NOTE recognizability' followed by a digit.
- Removes lines with timestamps in the format of '00:00:00.000 --> 00:00:01.000'.
- Adds a space at the beginning of lines that start with a letter or number.
- Removes line breaks.
- Replaces occurrences of '>  <' with '>\r\n<'.

### Parameters:
- `contents` (str): The string containing the contents of a VTT file.

### Returns:
- `cleaned_contents` (str): The cleaned contents of the VTT file.

## consolidate_tags(input_text)

This function consolidates consecutive text content lines enclosed in <v> tags with the same attributes. It uses regular expressions to match the tags and content.

### Parameters:
- `input_text` (str): The string containing the contents of a VTT file.

### Returns:
- `consolidated_text` (str): The consolidated text with consecutive text content lines enclosed in <v> tags.

