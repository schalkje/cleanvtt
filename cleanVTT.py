import re

def clean_file(input_file_path, output_file_path):
    try:
        # Read the input file
        with open(input_file_path, 'r') as input_file:
            file_contents = input_file.read()

        # Apply cleaning to the file contents
        cleaned_contents = clean_contents(file_contents)
        cleaned_contents = consolidate_tags(cleaned_contents)
        cleaned_contents = cleaned_contents.replace('><','>\n<')

        # Write the cleaned contents to the output file
        with open(output_file_path, 'w') as output_file:
            output_file.write(cleaned_contents)

        print("File cleaned successfully!")

    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print("An error occurred while cleaning the file:", str(e))

emptyNewLine = '\r\n';

def clean_contents(contents):
    cleaned_contents = contents.replace('dirty', 'clean')
    cleaned_contents = re.sub(r'WEBVTT[\r\n]', emptyNewLine, cleaned_contents)
    cleaned_contents = re.sub(r'NOTE duration:.*[\r\n]', emptyNewLine, cleaned_contents)
    cleaned_contents = re.sub(r'NOTE language:.*[\r\n]', emptyNewLine, cleaned_contents)
    cleaned_contents = re.sub(r'NOTE Confidence:.+\d', emptyNewLine, cleaned_contents)
    cleaned_contents = re.sub(r'NOTE recognizability.+\d', emptyNewLine, cleaned_contents)
    cleaned_contents = re.sub(r'[\r\n].+-.+-.+-.+-.+', emptyNewLine, cleaned_contents)
    cleaned_contents = re.sub(r'[\r\n].+ --> .+[\r\n]', emptyNewLine, cleaned_contents)
    cleaned_contents = re.sub(r'.[\r\n]. --> .+[\r\n]', emptyNewLine, cleaned_contents)
    cleaned_contents = re.sub(r'[\n](.)', ' \\1', cleaned_contents)
    cleaned_contents = re.sub(r'^ ', '', cleaned_contents)
    cleaned_contents = re.sub(r'[\r\n]', '', cleaned_contents)
    cleaned_contents = cleaned_contents.replace('>  <','>\r\n<')
    

    return cleaned_contents

def consolidate_tags(input_text):
    consolidated_tags = []
    consolidated_text = ""

    # Use regex to match the tags and content
    matches = re.findall(r'<v ([^>]*)>(.*?)</v>', input_text)

    prev_tag = None
    for tag, content in matches:
        if tag != prev_tag:
            if prev_tag is not None:
                consolidated_tags.append(f"</v>")
            consolidated_tags.append(f"<v {tag}>")
        consolidated_tags.append(content)
        prev_tag = tag

    consolidated_text = "".join(consolidated_tags)

    return consolidated_text

# Usage example
filename = 'green egg backloading'
input_file_path = 'examples/'+filename+'.vtt'  # Replace with the path to your input file
output_file_path = 'examples/'+filename+'.vtt.cleaned'  # Replace with the desired path for the cleaned output file

clean_file(input_file_path, output_file_path)